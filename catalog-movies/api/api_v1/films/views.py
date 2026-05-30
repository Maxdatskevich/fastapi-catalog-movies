import random

from starlette.requests import Request

from .crud import storage_movie
from .dependencies import find_movie
from schemas.movie import (
    Movie,
    MovieAdd,
)
from fastapi import (
    APIRouter,
    status,
    Form,
)

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
    return storage_movie


@router.get("/{movie_id}")
def get_movie_details(request: Request, movie_id: int) -> Movie:
    print("movie_id = ", movie_id)
    res = find_movie(movie_id)
    return res


@router.post("/add_new_film", response_model=Movie, status_code=status.HTTP_201_CREATED)
def add_new_film(
    new_film: MovieAdd,
) -> Movie:
    res = Movie(**new_film.model_dump())
    return Movie(**new_film.model_dump())
