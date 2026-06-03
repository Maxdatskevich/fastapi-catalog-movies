from typing import Annotated

from fastapi.params import Depends
from starlette import status
from starlette.requests import Request

from api.api_v1.films.crud import storage_movie
from api.api_v1.films.dependencies import find_movie
from schemas.movie import (
    MovieRead,
    MovieUpdateData,
    MoviePartitionUpdate,
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

MovieCheck = Annotated[
    MovieRead,
    Depends(find_movie),
]


# response_model=Movie — указывает, что ответ должен быть сериализован по модели Movie
@router.get("/", response_model=MovieRead)
def get_movie_details(
    movie: MovieCheck,
) -> MovieRead:
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie_by_id(
    movie: MovieCheck,
) -> None:
    storage_movie.delete(movie)
    print('{"ok": True}')


@router.put("/", response_model=MovieRead)
def update_movie_description(
    movie_id: MovieCheck,
    movie_data_in: MovieUpdateData,
):
    return storage_movie.update_data_movie(
        movie=movie_id,
        movie_descr_in=movie_data_in,
    )


@router.patch("/", response_model=MovieRead)
def update_movie_partitional(
    movie: MovieCheck,
    movie_data_in: MoviePartitionUpdate,
) -> MovieRead:
    return storage_movie.update_partial(
        movie=movie,
        movie_in=movie_data_in,
    )
