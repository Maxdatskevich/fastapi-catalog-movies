from fastapi import (
    APIRouter,
    Request,
)
from .api_v1 import router as api_v1_router
from .api_v1.films.views import router as films_router

# МОДУЛЬ ДЛЯ ХРАНЕНИЯ ВСЕЙ БИЗНЕС ЛОГИКИ


router = APIRouter(
    prefix="/api",
)
router.include_router(api_v1_router)
router.include_router(films_router)


@router.get("/")
def api_init(
    request: Request,
):
    return {
        "message": f"Hello! this is my first API",
        "docs": "main API",
    }
