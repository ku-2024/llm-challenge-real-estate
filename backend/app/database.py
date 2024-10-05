# app/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.config import SQLALCHEMY_DATABASE_URL
from sqlalchemy import text
# 비동기 엔진 생성
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 비동기 세션 로컬 생성
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# 세션 가져오기
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    # 루트 연결을 위한 엔진 생성
    root_engine = create_async_engine(f"{SQLALCHEMY_DATABASE_URL}")

    async with root_engine.begin() as conn:
        # 기존 데이터베이스 삭제
        await conn.execute(text("DROP DATABASE IF EXISTS budongsan"))
        
        # 새 데이터베이스 생성
        await conn.execute(text("CREATE DATABASE budongsan"))

    # 새로 생성된 데이터베이스에 연결
    engine = create_async_engine(f"{SQLALCHEMY_DATABASE_URL}")

    async with engine.begin() as conn:
        # 테이블 생성
        await conn.run_sync(Base.metadata.create_all)

    await root_engine.dispose()
    await engine.dispose()