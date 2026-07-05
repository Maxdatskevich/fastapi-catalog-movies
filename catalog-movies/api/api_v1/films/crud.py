import logging
import random

from pydantic import BaseModel, ValidationError

from schemas.movie import (
    SMovie,
    SMovieCreate,
    SMovieUpdate,
    SMoviePartitionUpdate,
    SMovieRead,
)
from core.config import MOVIES_STORAGE_FILEPATH

log_crud = logging.getLogger(__name__)

# МОДУЛЬ С ФУНКЦИЯМИ ДЛЯ РАБОТЫ С БД
movies_dict = [
    SMovieCreate(
        id=1,
        title_f="Интерстеллар",
        description_f="Фантастический эпос про задыхающуюся Землю, космические полеты и парадоксы времени. «Оскар» за спецэффекты",
        # year_f=2014,
        # director_f="Кристофер Нолан",
        # budget_f=165000000,
    ),
    SMovieCreate(
        title_f="Побег из Шоушенка",
        description_f="Несправедливо осужденный банкир готовит побег из тюрьмы. Тим Роббинс в выдающейся экранизации Стивена Кинга",
        # year_f=1994,
        # director_f="Фрэнк Дарабонт",
        # budget_f=25000000,
    ),
    SMovieCreate(
        title_f="Джентльмены",
        description_f="Гангстеры всех мастей делят нелегальный бизнес. Закрученная экшен-комедия Гая Ричи с Мэттью Макконахи",
        # year_f=2019,
        # director_f="Гай Ричи",
        # budget_f=22000000,
    ),
    SMovieCreate(
        title_f="Властелин колец: Возвращение короля",
        description_f="Арагорн штурмует Мордор, а Фродо устал бороться с чарами кольца. Эффектный финал саги, собравший 11 «Оскаров»",
        # year_f=2003,
        # director_f="Питер Джексон",
        # budget_f=94000000,
    ),
    SMovieCreate(
        title_f="Зеленая миля",
        description_f="В тюрьме для смертников появляется заключенный с божественным даром. Мистическая драма по роману Стивена Кинга",
        # year_f=1999,
        # director_f="Фрэнк Дарабонт",
        # budget_f=60000000,
    ),
]


class MoviesDictStorage(BaseModel):
    movies_dict: dict[int, SMovie] = {}

    def init_storage_movie_from_state(self) -> None:
        try:
            data_movie = MoviesDictStorage.from_state()
            print("data_movie = ", data_movie)
            # Извлеченные данные из файла movies.json.
            log_crud.warning("Recovered data from movies.json file.")
        except ValidationError:
            self.save_state()
            log_crud.warning("Rewriting movies.json due to validation error.")
            return
        self.movies_dict.update(data_movie.movies_dict)
        # Данные из файла хранилища
        log_crud.warning("Recovered data from storage file.")

    def get(self) -> list[SMovie]:
        return list(self.movies_dict.values())  # список из значений словаря

    def save_state(self) -> None:
        MOVIES_STORAGE_FILEPATH.write_text(
            self.model_dump_json(indent=2, ensure_ascii=False)
        )
        log_crud.info("Saved new movie to movies.json file.")

    @classmethod
    def from_state(cls) -> "MoviesDictStorage":
        if not MOVIES_STORAGE_FILEPATH.exists():
            log_crud.info("Movies.json file doesn't exists.")

            return MoviesDictStorage()
        return cls.model_validate_json(MOVIES_STORAGE_FILEPATH.read_text())

    def get_by_movie_id(self, movie_id: int) -> SMovie | None:
        return self.movies_dict.get(movie_id)  # ключ из словаря

    def create(self, movie_data_in: SMovieCreate) -> SMovie:
        if movie_data_in.id is None:
            new_id = random.randint(1, 1000)
            movie_data_in.id = new_id

        new_movie = SMovie(
            **movie_data_in.model_dump(),  # превращение Pydantic-модели в словарь
        )
        self.movies_dict[new_movie.id] = new_movie
        return new_movie

    def delete_by_id(self, movie_id: int) -> None:
        # self.save_state()
        self.movies_dict.pop(movie_id, None)

    def delete(self, movie: SMovie) -> None:
        self.delete_by_id(movie.id)

    def update_data_movie(
        self,
        movie: SMovie,
        movie_descr_in: SMovieUpdate,
    ) -> SMovie:
        for field_name, value in movie_descr_in:
            setattr(movie, field_name, value)
        # self.save_state()
        return movie

    def update_partial(
        self, movie: SMovie, movie_in: SMoviePartitionUpdate
    ) -> SMovieRead:
        # print(movie_in.model_dump(exclude_unset=True).items())
        # print(movie_in.model_dump(exclude_unset=True))
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        return movie


"""
SMovie = 
SMovie(
    year_f=1999,
    director_f="Фрэнк Дарабонт",
    budget_f=60000000,
    title_f="Зеленая миля",
    description_f="В тюрьме для смертников появляется заключенный с божественным даром. Мистическая драма по роману Стивена Кинга",
)

SMovie_descr_in = SMovieUpdate(title_f="new", description_f="new")
"""

# new_data = MoviesDictStorage()
# for i in movies_dict:
#     new_data.create(i)

storage_movie = MoviesDictStorage()
