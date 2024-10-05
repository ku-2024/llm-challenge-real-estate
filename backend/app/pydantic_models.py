# app/pydantic_models.py
from pydantic import BaseModel
from typing import Optional

class AptInfoCreate(BaseModel):
    apt_code: str
    apt_name: Optional[str] = None
    total_households: Optional[int] = None 
    completion_date: Optional[str] = None 
    # location: Optional[str] = None 
    district: Optional[str] = None 
    total_buildings: Optional[int] = None
    land_address: Optional[str] = None
    road_address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    construction_company: Optional[str] = None
    heating_type: Optional[str] = None
    max_floor: Optional[int] = None
    min_floor: Optional[int] = None
    parking_per_household: Optional[float] = None
    area_list:Optional[str] = None
    class Config:
        orm_mode = True

class AptReviewCreate(BaseModel):
    id: Optional[int] = None
    apt_code: str
    category: Optional[str] = None
    review: Optional[str] = None

    class Config:
        orm_mode = True

class AptTradeCreate(BaseModel):
    id: Optional[int] = None
    apt_code: str
    apt_sq: Optional[int] = None
    avg_price: Optional[str] = None
    top_avg_price: Optional[str] = None
    bottom_avg_price: Optional[str] = None
    recent_avg: Optional[str] = None
    recent_top: Optional[str] = None
    recent_bottom: Optional[str] = None
    trade_trend: Optional[str] = None
    price_trend: Optional[str] = None

    class Config:
        orm_mode = True

class AptReviewSummary(BaseModel):
    id: Optional[int] = None
    apt_code: str
    category: Optional[str] = None
    review: Optional[str] = None
    create_date: Optional[str] = None

    class Config:
        orm_mode = True