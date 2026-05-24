# МОДУЛЬ c ЗАВИСИМОСтями ПОДКЛЮЧЕНИЯ К БД
from fastapi import HTTPException
from starlette import status

from .crud import MOVIES
from schemas.movie import Movie


def find_movie(movie_id: int) -> Movie:
    movie_details: Movie | None = next(
        (movie for movie in MOVIES if movie.id == movie_id), None
    )
    if movie_details:
        return movie_details

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Film id {movie_id!r} not found",
    )
