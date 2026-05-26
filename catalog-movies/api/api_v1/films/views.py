import random

from starlette.requests import Request

from .crud import MOVIES
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
# def add_new_film(
#     year_f: int = None,
#     director_f: str = None,
#     budget_f: int = None,
# ) -> Movie:
#     new_id = random.randint(5, 1000)
#     return Movie(
#         id=new_id,
#         title_f=title_f,
#         description_f=description_f,
#         year_f=year_f,
#         director_f=director_f,
#         budget_f=budget_f,
#     )
@router.post("/add_new_film", response_model=Movie, status_code=status.HTTP_201_CREATED)
def add_new_film(
    new_film: MovieAdd,
) -> Movie:
    res = Movie(**new_film.model_dump())
    print(res)
    return Movie(**new_film.model_dump())
