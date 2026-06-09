# МОДУЛЬ c ЗАВИСИМОСтями ПОДКЛЮЧЕНИЯ К БД
from fastapi import HTTPException
from starlette import status

from .crud import (
    storage_movie,
)
from schemas.movie import SMovie


def find_movie(movie_id: int) -> SMovie:
    movie_details: SMovie | None = storage_movie.get_by_movie_id(movie_id)
    if movie_details:
        return movie_details

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Film id {movie_id!r} not found",
    )
