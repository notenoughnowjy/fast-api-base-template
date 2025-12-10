from fastapi import FastAPI

from app.core.config import settings
from app.database import Base, engine
from api.v1.api import api_router

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# API v1 라우터 등록
app.include_router(api_router, prefix="/api/v1")
