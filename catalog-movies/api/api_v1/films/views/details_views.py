from typing import Annotated

from fastapi.params import Depends
from starlette import status
from starlette.requests import Request

from api.api_v1.films.crud import storage_movie
from api.api_v1.films.dependencies import find_movie
from schemas.movie import (
    MovieRead,
    MovieUpdateData,
)
from fastapi import APIRouter

router = APIRouter(
    prefix="/{movie_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie with id 'movie_id' not found",
            "content": {
                "aplication/json": {"example": {"detail": "Movie 'movie_id' not found"}}
            },
        },
    },
)

MovieData = Annotated[
    MovieRead,
    Depends(find_movie),
]


# response_model=Movie — указывает, что ответ должен быть сериализован по модели Movie
@router.get("/", response_model=MovieRead)
def get_movie_details(
    movie: MovieData,
) -> MovieRead:
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie_by_id(
    movie: MovieData,
) -> None:
    storage_movie.delete(movie)
    print('{"ok": True}')


@router.put("/", response_model=MovieRead)
def update_movie_description(
    movie: MovieData,
    movie_data_in: MovieUpdateData,
):
    return storage_movie.update_data_movie(
        movie=movie,
        movie_descr_in=movie_data_in,
    )
