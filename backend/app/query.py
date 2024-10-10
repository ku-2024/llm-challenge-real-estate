# app/query.py
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.models import AptReview, AptTrade, AptInfo, AptReviewSummary
from fastapi import HTTPException

async def insert_apt_info(session: AsyncSession, filename: str):
    info_df = pd.read_csv(filename, na_values=['nan', 'NaN', 'NAN', ''])
    info_df = info_df.where(pd.notnull(info_df), None)
    
    for index, row in info_df.iterrows():
        info = AptInfo(
            apt_code = row['apt_code'],
            apt_name = row['apt_name'] if pd.notnull(row['apt_name']) else None,
            total_households = row['total_households'] if pd.notnull(row['total_households']) else None,
            completion_date = row['completion_date'] if pd.notnull(row['completion_date']) else None,
            district = row['district'] if pd.notnull(row['district']) else None,
            total_buildings = int(row['total_buildings']) if pd.notnull(row['total_buildings']) else None,
            land_address = row['land_address'] if pd.notnull(row['land_address']) else None,
            road_address = row['road_address'] if pd.notnull(row['road_address']) else None,
            latitude = str(row['latitude']) if pd.notnull(row['latitude']) else None,
            longitude = str(row['longitude']) if pd.notnull(row['longitude']) else None,
            construction_company = row['construction_company'] if pd.notnull(row['construction_company']) else None,
            heating_type = row['heating_type'] if pd.notnull(row['heating_type']) else None,
            max_floor = int(row['max_floor']) if pd.notnull(row['max_floor']) else None,
            min_floor = int(row['min_floor']) if pd.notnull(row['min_floor']) else None,
            parking_per_household = str(row['parking_per_household']) if pd.notnull(row['parking_per_household']) else None,
            area_list = row['area_list'] if pd.notnull(row['area_list']) else None,
        )
        session.add(info)
    await session.commit()

async def insert_apt_reviews(session: AsyncSession, filename: str):
    review_df = pd.read_csv(filename)
    for _, row in review_df.iterrows():
        review = AptReview(
            apt_code=row['apt_code'],
            category=row['category'],
            review=row['review']
        )
        session.add(review)
    await session.commit()

async def insert_apt_review_summary(session: AsyncSession, filename: str):
    review_df = pd.read_csv(filename)
    for _, row in review_df.iterrows():
        review = AptReviewSummary(
                        apt_code = row['apt_code'],
                        create_date=pd.Timestamp.now().strftime('%Y-%m-%d'),
                        category=row['category'], 
                        review=row['review'])
        session.add(review)
    await session.commit()



async def insert_apt_trades(session: AsyncSession):
    trade_df = pd.read_csv('data/apt_trade/Apt_transaction_result.csv')
    for _, row in trade_df.iterrows():
        trade = AptTrade(
            apt_code = row['apt_code'],
            # apt_name=row['apt_name'],
            apt_sq=row['apt_sq'],
            avg_price=row['avg_price'],
            top_avg_price=row['top_avg_price'],
            bottom_avg_price=row['bottom_avg_price'],
            recent_avg=row['recent_avg'],
            recent_top=row['recent_top'],
            recent_bottom=row['recent_bottom'],
            trade_trend=row['trade_trend'],
            price_trend=row['price_trend']
        )
        session.add(trade)
    await session.commit()

async def get_apt_data(apt_code: str, db: AsyncSession):
    reviews = await db.execute(
        select(AptInfo.apt_name, 
               AptReview.category, 
               AptReview.review
        ).join(AptReview, AptInfo.apt_code == AptReview.apt_code
        ).filter( AptInfo.apt_code == apt_code
        ).order_by(AptReview.category)
    )
    reviews = reviews.mappings().all()
    # print(reviews)
    review_list = [{'category': review.category, 'review': review.review} for review in reviews]
    apt_name = (await db.execute(select(AptInfo.apt_name).filter(AptInfo.apt_code == apt_code))).scalar_one_or_none()
    result = await db.execute(select(AptInfo.apt_name, 
                                     AptInfo.apt_code, 
                                     AptTrade.apt_sq, 
                                     AptTrade.top_avg_price, 
                                     AptTrade.bottom_avg_price, 
                                     AptTrade.avg_price
                                    ).filter(AptInfo.apt_code==apt_code
                                    ).order_by(AptTrade.apt_sq))
    trades = result.mappings().all()
    trade_list = [
        {
            'apt_sq': trade.apt_sq,
            'avg_price': trade.avg_price,
            'top_avg_price': trade.top_avg_price,
            'bottom_avg_price': trade.bottom_avg_price,
        }
        for trade in trades
    ]
    return {'status':200,
            'data':{'apt_code': apt_code, 'apt_name': apt_name, 'reviews': review_list, 'trades': trade_list}}

async def get_all_name_sq(db: AsyncSession):
    result = await db.execute(
        select(AptInfo.apt_name, AptInfo.apt_code, AptTrade.apt_sq
        ).join(AptTrade, AptInfo.apt_code == AptTrade.apt_code)
    )
    results = result.all()
    return {'status':200,
            'data':[{'apt_code':apt_code, 'apt_name': apt_name, 'apt_sq': f"{apt_sq}㎡"} for apt_name, apt_code, apt_sq in results]}


async def get_all_name_code(db: AsyncSession, page: int = 1, page_size: int = 10):
    if page < 1:
        raise HTTPException(status_code=400, detail="Page number must be greater than 0")
    
    offset = (page - 1) * page_size
    
    # 총 개수 조회
    total_query = select(func.count()).select_from(AptInfo)
    total = await db.scalar(total_query)
    
    # 페이지 데이터 조회
    query = (
        select(AptInfo.apt_name, AptInfo.apt_code, AptInfo.latitude, AptInfo.longitude, AptInfo.land_address, AptInfo.road_address)
        .offset(offset)
        .limit(page_size)
    )
    
    result = await db.execute(query)
    results = result.all()
    
    if not results and page > 1:
        # 요청한 페이지가 데이터 범위를 벗어난 경우
        raise HTTPException(status_code=404, detail="Page not found")
    
    return {
        'status': 200,
        'data': [{'apt_name': r.apt_name, 'apt_code': r.apt_code, 'latitude': r.latitude, 'longitude': r.longitude, 'land_address': r.land_address, 'loa_address': r.land_address} for r in results],
        'total': total,
        'page': page,
        'page_size': page_size
    }


async def get_region_apt_data(db: AsyncSession):
    result = await db.execute(
        select(AptInfo.apt_name, AptInfo.apt_code, AptTrade.avg_price, AptTrade.top_avg_price, AptTrade.bottom_avg_price, AptTrade.apt_sq
        ).join(AptTrade, AptInfo.apt_code == AptTrade.apt_code)
    )
    results = result.mappings().all()
    print(results)
    return {
        'status': 200,
        'data': [{'apt_name': row['apt_name'], 'apt_code': row['apt_code'] ,'apt_sq': row['apt_sq'], 'avg_price': row['avg_price']} for row in results]
    }


async def get_review_summary(apt_code: str, db: AsyncSession):
    result = await db.execute(
        select(AptInfo.apt_name, AptInfo.apt_code, AptReviewSummary.category, AptReviewSummary.review
        ).join(AptReviewSummary, AptReviewSummary.apt_code == AptInfo.apt_code).filter(AptReviewSummary.apt_code==apt_code).order_by(AptReviewSummary.category)
                                    )
    
    results = result.mappings().all()
    print(results)
    return {
        'status': 200,
        'data': [{'apt_name': row['apt_name'], 'apt_code': row['apt_code'] ,'category': row['category'], 'review': row['review']} for row in results]
    }