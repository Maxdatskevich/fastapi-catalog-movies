from starlette.requests import Request

from .crud import MOVIES
from .dependencies import find_movie
from schemas.movie import Movie
from fastapi import APIRouter

# endpoints (контроллеры).
# МОДУЛЬ С ЗАВИСИМОСТЯМИ. ОБРАБАТЫВАЕМ http ЗАПРОСЫ, ОТДАЕМ ОТВЕТ ИЗ crud

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("/")
def get_films(
    request: Request,
) -> dict:
    return {
        "message": f"Hello! this is API for films",
        "docs": "main films",
    }


@router.get("/all_movies")
def get_all_movies(
    request: Request,
) -> list:
    return MOVIES


@router.get("/{movie_id}")
def get_movie_details(request: Request, movie_id: int) -> Movie:
    res = find_movie(movie_id)
    return res
