# МОДУЛЬ c ЗАВИСИМОСтями ПОДКЛЮЧЕНИЯ К БД
import logging

from fastapi import (HTTPException,
    BackgroundTasks,
                     )
from starlette import status

from .crud import (
    storage_movie,
)
from schemas.movie import SMovie

# создаём логгер(объект для записи логов) с именем, соответствующим имени текущего модуля(dependencies.py)
log = logging.getLogger(__name__)

def find_movie(movie_id: int) -> SMovie:
    movie_details: SMovie | None = storage_movie.get_by_movie_id(movie_id)
    if movie_details:
        return movie_details

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Film id {movie_id!r} not found",
    )


def save_storage_movies(
    background_tasks: BackgroundTasks
):
    # код перед входом в функции views.py
    yield
    # код после входа в функции views.py
    log.info("Inside save_storage_movies")
    background_tasks.add_task(storage_movie.save_state)