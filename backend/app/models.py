# app/models.py
from sqlalchemy import Column, String, Integer, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AptInfo(Base):
    __tablename__ = 'apt_info'
    apt_code = Column(String(255), primary_key=True)
    apt_name = Column(String(255), nullable=True)
    total_households = Column(String(255), nullable=True)
    completion_date = Column(String(255), nullable=True)
    district = Column(String(255), nullable=True)
    total_buildings = Column(Integer, nullable=True)
    land_address = Column(String(255), nullable=True)
    road_address = Column(String(255), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    construction_company = Column(String(255), nullable=True)
    heating_type = Column(String(255), nullable=True)
    max_floor = Column(Integer, nullable=True)
    min_floor = Column(Integer, nullable=True)
    parking_per_household = Column(Float, nullable=True)
    area_list = Column(String(255), nullable=True)
    
class AptReview(Base):
    __tablename__ = 'apt_review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    apt_code = Column(String(255), ForeignKey('apt_info.apt_code'))
    category = Column(String(255))
    review = Column(Text(255))

class AptTrade(Base):
    __tablename__ = 'apt_trade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    apt_code = Column(String(255), ForeignKey('apt_info.apt_code'))
    apt_sq = Column(Integer)
    avg_price = Column(String(255))
    top_avg_price = Column(String(255))
    bottom_avg_price = Column(String(255))
    recent_avg = Column(String(255))
    recent_top = Column(String(255))
    recent_bottom = Column(String(255))
    trade_trend = Column(String(255))
    price_trend = Column(String(255))



class AptReviewSummary(Base):
    __tablename__ = 'apt_review_summary'
    id = Column(Integer, primary_key=True, autoincrement=True)
    apt_code = Column(String(255), ForeignKey('apt_info.apt_code'))
    category = Column(String(255))
    review = Column(Text(255))
    create_date = Column(String(255))