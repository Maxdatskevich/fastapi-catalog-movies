from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
)
from schemas.movie import Movie

app = FastAPI(title="Catalog movies")

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
        id=2,
        title_f="Побег из Шоушенка",
        description_f="Несправедливо осужденный банкир готовит побег из тюрьмы. Тим Роббинс в выдающейся экранизации Стивена Кинга",
        year_f=1994,
        director_f="Фрэнк Дарабонт",
        budget_f=25000000,
    ),
    Movie(
        id=3,
        title_f="Джентльмены",
        description_f="Гангстеры всех мастей делят нелегальный бизнес. Закрученная экшен-комедия Гая Ричи с Мэттью Макконахи",
        year_f=2019,
        director_f="Гай Ричи",
        budget_f=22000000,
    ),
    Movie(
        id=4,
        title_f="Властелин колец: Возвращение короля",
        description_f="Арагорн штурмует Мордор, а Фродо устал бороться с чарами кольца. Эффектный финал саги, собравший 11 «Оскаров»",
        year_f=2003,
        director_f="Питер Джексон",
        budget_f=94000000,
    ),
    Movie(
        id=5,
        title_f="Зеленая миля",
        description_f="В тюрьме для смертников появляется заключенный с божественным даром. Мистическая драма по роману Стивена Кинга",
        year_f=1999,
        director_f="Фрэнк Дарабонт",
        budget_f=60000000,
    ),
]


@app.get("/")
def read_root(
    request: Request,
    name: str = "text",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello {name}",
        "docs": str(docs_url),
    }


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


@app.get("/all_movies/")
def get_all_movies(
    request: Request,
) -> list:
    return MOVIES


@app.get("/movie/{movie_id}")
def get_movie_details(request: Request, movie_id: int) -> Movie:
    res = find_movie(movie_id)
    return res
