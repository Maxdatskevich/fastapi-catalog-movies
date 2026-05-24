from fastapi import APIRouter
from .api_v1 import router as api_v1_router

# МОДУЛЬ ДЛЯ ХРАНЕНИЯ ВСЕЙ БИЗНЕС ЛОГИКИ

router = APIRouter(
    prefix="/api",
)

router.include_router(api_v1_router)
