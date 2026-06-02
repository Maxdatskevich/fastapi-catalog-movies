import random

from pydantic import BaseModel

from schemas.movie import (
    MovieRead,
    MovieCreate,
    MovieUpdateData,
)

# МОДУЛЬ С ФУНКЦИЯМИ ДЛЯ РАБОТЫ С БД

MOVIES = [
    MovieRead(
        id=1,
        year_f=2014,
        director_f="Кристофер Нолан",
        budget_f=165000000,
        title_f="Интерстеллар",
        description_f="Фантастический эпос про задыхающуюся Землю, космические полеты и парадоксы времени. «Оскар» за спецэффекты",
    ),
    MovieRead(
        year_f=1994,
        director_f="Фрэнк Дарабонт",
        budget_f=25000000,
        title_f="Побег из Шоушенка",
        description_f="Несправедливо осужденный банкир готовит побег из тюрьмы. Тим Роббинс в выдающейся экранизации Стивена Кинга",
    ),
    MovieRead(
        year_f=2019,
        director_f="Гай Ричи",
        budget_f=22000000,
        title_f="Джентльмены",
        description_f="Гангстеры всех мастей делят нелегальный бизнес. Закрученная экшен-комедия Гая Ричи с Мэттью Макконахи",
    ),
    MovieRead(
        year_f=2003,
        director_f="Питер Джексон",
        budget_f=94000000,
        title_f="Властелин колец: Возвращение короля",
        description_f="Арагорн штурмует Мордор, а Фродо устал бороться с чарами кольца. Эффектный финал саги, собравший 11 «Оскаров»",
    ),
    MovieRead(
        year_f=1999,
        director_f="Фрэнк Дарабонт",
        budget_f=60000000,
        title_f="Зеленая миля",
        description_f="В тюрьме для смертников появляется заключенный с божественным даром. Мистическая драма по роману Стивена Кинга",
    ),
]


class MoviesStorage(BaseModel):
    movies: dict[int, MovieRead] = {}

    def get(self) -> list[MovieRead]:
        return list(self.movies.values())  # список из значений словаря

    def get_by_movie_id(self, movie_id: int) -> MovieRead | None:
        return self.movies.get(movie_id)  # ключ из словаря

    def create(self, movie_data_in: MovieCreate) -> MovieRead:
        if movie_data_in.id is None:
            new_id = random.randint(1, 1000)
        else:
            new_id = movie_data_in.id
        new_movie = MovieRead(
            id=new_id,
            **movie_data_in.model_dump(
                exclude={"id"},
            ),  # превращение Pydantic-модели в словарь
        )
        self.movies[new_movie.id] = new_movie
        return new_movie

    def delete_by_id(self, movie_id: int) -> None:
        deleted = self.movies.pop(movie_id, None)

    def delete(self, movie: MovieRead) -> None:
        self.delete_by_id(movie.id)

    def update_data_movie(
        self,
        movie: MovieRead,
        movie_descr_in: MovieUpdateData,
    ) -> MovieRead:
        for field_name, value in movie_descr_in:
            setattr(movie, field_name, value)
        return movie


"""
movie = 
MovieRead(
    year_f=1999,
    director_f="Фрэнк Дарабонт",
    budget_f=60000000,
    title_f="Зеленая миля",
    description_f="В тюрьме для смертников появляется заключенный с божественным даром. Мистическая драма по роману Стивена Кинга",
)

movie_descr_in = MovieUpdateData(title_f="new", description_f="new")
"""


storage_movie = MoviesStorage()
for i in MOVIES:
    storage_movie.create(MovieCreate(**i.model_dump()))
