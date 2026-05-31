from pydantic import BaseModel

from schemas.movie import Movie, MovieAdd

# МОДУЛЬ С ФУНКЦИЯМИ ДЛЯ РАБОТЫ С БД

MOVIES = [
    Movie(
        id=1,
        title_f="Интерстеллар",
        description_f="Фантастический эпос про задыхающуюся Землю, космические полеты и парадоксы времени. «Оскар» за спецэффекты",
        year_f=2014,
        director_f="Кристофер Нолан",
        budget_f=165000000,
    ),
    Movie(
        title_f="Побег из Шоушенка",
        description_f="Несправедливо осужденный банкир готовит побег из тюрьмы. Тим Роббинс в выдающейся экранизации Стивена Кинга",
        year_f=1994,
        director_f="Фрэнк Дарабонт",
        budget_f=25000000,
    ),
    Movie(
        title_f="Джентльмены",
        description_f="Гангстеры всех мастей делят нелегальный бизнес. Закрученная экшен-комедия Гая Ричи с Мэттью Макконахи",
        year_f=2019,
        director_f="Гай Ричи",
        budget_f=22000000,
    ),
    Movie(
        title_f="Властелин колец: Возвращение короля",
        description_f="Арагорн штурмует Мордор, а Фродо устал бороться с чарами кольца. Эффектный финал саги, собравший 11 «Оскаров»",
        year_f=2003,
        director_f="Питер Джексон",
        budget_f=94000000,
    ),
    Movie(
        title_f="Зеленая миля",
        description_f="В тюрьме для смертников появляется заключенный с божественным даром. Мистическая драма по роману Стивена Кинга",
        year_f=1999,
        director_f="Фрэнк Дарабонт",
        budget_f=60000000,
    ),
]


class MoviesStorage(BaseModel):
    movie: dict[str, Movie] = {}

    def get(self) -> list[Movie]:
        return list(self.movie.values())  # список из значений словаря

    def get_by_movie_id(self, movie_id: int) -> Movie | None:
        return self.movie.get(movie_id)  # ключи из словаря

    def create(self, movie_data_in: MovieAdd) -> Movie:
        movie = Movie(
            **movie_data_in.model_dump(),  # превращение Pydantic-модели в словарь
        )
        self.movie[movie.id] = movie  # добавляем запись в словарь
        return movie

    def delete_by_id(self, movie_id: int) -> None:
        deleted = self.movie.pop(movie_id, None)
        print(deleted)
        return {"ok": True}

    def delete(self, movie: Movie) -> None:
        self.delete_by_id(movie.id)


storage_movie = MoviesStorage()
for i in MOVIES:
    storage_movie.create(MovieAdd(**i.model_dump()))
