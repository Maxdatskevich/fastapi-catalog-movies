from starlette.requests import Request

from .crud import MOVIES
from .dependencies import find_movie
from schemas.movie import Movie
from fastapi import (
    APIRouter,
    status,
    Form,
)

from typing import Annotated
from annotated_types import Len

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


@router.post("/add_new_film", response_model=Movie, status_code=status.HTTP_201_CREATED)
def add_new_film(
    id: int,
    title_f: Annotated[str, Len(min_length=2, max_length=50), Form()],
    description_f: Annotated[str, Len(min_length=5, max_length=300), Form()],
) -> Movie:
    return Movie(id=id, title_f=title_f, description_f=description_f)


"""
id: int  # уникальный номер
    title_f: str  # название
    description_f: str  # описание
    year_f: int | None  # год выпуска
    director_f: str | None  # режиссер
    budget_f: int | None  # бюджет

"""
