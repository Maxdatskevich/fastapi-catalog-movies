from typing import Annotated

from fastapi.params import Depends
from starlette import status

from api.api_v1.films.crud import storage_movie
from api.api_v1.films.dependencies import find_movie
from schemas.movie import (
    SMovie,
    SMovieUpdate,
    SMoviePartitionUpdate,
    SMovieRead,
)
from fastapi import (APIRouter,
                     BackgroundTasks,
                     )

router = APIRouter(
    prefix="/{movie_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "movie with id 'movie_id' not found",
            "content": {
                "aplication/json": {"example": {"detail": "movie 'movie_id' not found"}}
            },
        },
    },
)

SMovieCheck = Annotated[
    SMovie,
    Depends(find_movie),
]


# response_model=SMovie — указывает, что ответ должен быть сериализован по модели SMovie
@router.get("/", response_model=SMovieRead)
def get_movie_details(
    movie: SMovieCheck,
) -> SMovieRead:
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie_by_id(
    movie: SMovieCheck,
) -> None:
    storage_movie.delete(movie)
    print('{"ok": True}')
    return


@router.put("/", response_model=SMovieRead)
def update_movie_description(
    movie_id: SMovieCheck,
    new_data_in: SMovieUpdate,
):
    updt_movie = storage_movie.update_data_movie(
        movie=movie_id,
        movie_descr_in=new_data_in,
    )
    return updt_movie


@router.patch("/", response_model=SMovieRead)
def update_movie_partitional(
    movie: SMovieCheck,
    new_data_in: SMoviePartitionUpdate,
) -> SMovie:
    new_movie = storage_movie.update_partial(
        movie=movie,
        movie_in=new_data_in,
    )
    return new_movie
