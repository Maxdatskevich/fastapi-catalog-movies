from starlette.requests import Request

from api.api_v1.films.crud import storage_movie
from api.api_v1.films.dependencies import save_storage_movies
from schemas.movie import (
    SMovie,
    SMovieCreate,
    SMovieRead,
)
from fastapi import (
    APIRouter,
    status,
    BackgroundTasks,
    Depends,
)

# endpoints (контроллеры).
# МОДУЛЬ С ЗАВИСИМОСТЯМИ. ОБРАБАТЫВАЕМ http ЗАПРОСЫ, ОТДАЕМ ОТВЕТ ИЗ crud

router = APIRouter(
    prefix="/movies_dict",
    tags=["movies_dict"],
    dependencies=[Depends(save_storage_movies)]
)


# @router.get("/")
# def get_films(
#     request: Request,
# ) -> dict:
#     return {
#         "message": f"Hello! this is API for films",
#         "docs": "main films",
#     }


@router.get(
    "/all_movies_dict",
    response_model=list[SMovie],
)
def get_all_movies_dict() -> list:
    return storage_movie.get()


@router.post(
    "/add_new_film", response_model=SMovieRead, status_code=status.HTTP_201_CREATED
)
def add_new_film(
    new_film: SMovieCreate,
) -> SMovie:
    new_movie = storage_movie.create(new_film)
    return new_movie
