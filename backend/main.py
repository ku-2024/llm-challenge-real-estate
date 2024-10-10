from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.query import *
from app.database import get_db, init_db
from sqlalchemy.ext.asyncio import AsyncSession
import os

# # Lifespan 핸들러 정의
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # 애플리케이션 시작 시 실행할 코드
#     await init_db()  # 데이터베이스 테이블 생성
#     yield
#     # 애플리케이션 종료 시 실행할 코드 (리소스 해제 작업 등)

# FastAPI 애플리케이션 인스턴스에 lifespan 이벤트 핸들러 연결
app = FastAPI()#(lifespan=lifespan)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/init-db")
async def initialize_database():
    await init_db()
    return {"message": "Database initialized successfully"}

@app.post("/insertdata")
async def insert_data(db: AsyncSession = Depends(get_db)):
    """
    Inserts apartment-related data into the database from CSV files.

    This function performs the following actions:
    1. Inserts apartment information (`apt_info`) from a specified CSV file.
    2. Iterates through all the CSV files in the 'apt_review' directory and inserts apartment reviews (`apt_review`).
    3. Inserts apartment trade data (`apt_trade`) into the database.

    Param:
        None

    Returns:
        dict: A dictionary with a status code and a message indicating success.
    """
    # apt_info 데이터 먼저 삽입
    await insert_apt_info(db, './data/apartment_data.csv')

    # apt_review 데이터 삽입
    review_dir = 'data/apt_review'
    for filename in os.listdir(review_dir):
        file_path = os.path.join(review_dir, filename)
        if os.path.isfile(file_path) and file_path.endswith('.csv'):
            await insert_apt_reviews(db, file_path)
    
    review_sum_dir = 'data/apt_review_summ'
    for filename in os.listdir(review_sum_dir):
        file_path = os.path.join(review_sum_dir, filename)
        if os.path.isfile(file_path) and file_path.endswith('.csv'):
            await insert_apt_review_summary(db, file_path)

    # apt_trade 데이터 삽입
    await insert_apt_trades(db)
    return {"status": 200, "message": "Data insertion successful"}

@app.get("/getdata/{apt_code}")
async def get_data(apt_code:str, db: AsyncSession = Depends(get_db)):
    """
    Retrieves apartment data based on apartment code and name.

    Params:
        apt_name (str): The name of the apartment.

    Returns:
        Any: The requested apartment data.
    """

    return await get_apt_data(apt_code, db)

@app.get("/get/all-name-sq")
async def get_all_names_and_sq(db: AsyncSession = Depends(get_db)):
    """
    Retrieves all apartment names along with their square footage data.

    Params:
        None

    Returns:
        Any: A list of all apartment names with corresponding square footage data.
    """

    return await get_all_name_sq(db)

@app.get("/get/all-name-code")
async def get_all_names_and_code(page: int, size: int,  db: AsyncSession = Depends(get_db)):
    """
    Retrieves all apartment names along with their unique codes.

    Params:
        None

    Returns:
        Any: A list of all apartment names with their corresponding codes.
    """    
    return await get_all_name_code(db = db, page = page, page_size = size)

@app.get("/get/name-price")
async def get_all_names_and_code(db: AsyncSession = Depends(get_db)):
    """
    Retrieves all apartment names and price.

    Params:
        None

    Returns:
        Any: A list of all apartment names and price.
    """    
    return await get_region_apt_data(db)

@app.get("/get/review_summary/{apt_code}")
async def get_apt_review_summary(apt_code: str, db: AsyncSession = Depends(get_db)):
    """
    Retrieves a summary of apartment reviews based on apartment code and category.

    Params:
        apt_code (str): The code of the apartment.
        category (int): The category of the apartment review.

    Returns:
        Any: A summary of the apartment reviews.
    """
    return await get_review_summary(apt_code, db)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000, reload=True)