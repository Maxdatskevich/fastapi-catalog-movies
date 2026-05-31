import random
from typing import Annotated
from fastapi.params import Depends
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


# response_model=Movie — указывает, что ответ должен быть сериализован по модели Movie
@router.get("/{movie_id}", response_model=Movie)
def get_movie_details(
    movie: Annotated[Movie, Depends(find_movie)],
) -> Movie:
    return movie


@router.post("/add_new_film", response_model=Movie, status_code=status.HTTP_201_CREATED)
def add_new_film(
    new_film: MovieAdd,
) -> Movie:

    return Movie(**new_film.model_dump())


@router.delete(
    "/delete/{movie_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie with movie_id not found",
            "content": {
                "aplication/json": {"example": {"detail": "Movie 'movie_id' not found"}}
            },
        },
    },
)
def delete_movie_by_id(
    movie: Annotated[Movie, Depends(find_movie)],
) -> None:
    storage_movie.delete(movie)
    print('{"ok": True}')
