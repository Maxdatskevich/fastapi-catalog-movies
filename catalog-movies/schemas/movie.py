import random

from pydantic import BaseModel, Field
from typing import Annotated, Optional
from annotated_types import Len

DescriptionTitle = Annotated[
    str,
    Len(min_length=1, max_length=50),
]

DescriptionString = Annotated[
    str,
    Len(min_length=1, max_length=300),
]


# классы, которые описывают структуру данных
# Pydantic для автоматической генерации документации Swagger и OpenAPI.


# 1. Базовый класс с полями, которые есть во всех схемах (кроме id)
class SMovieBase(BaseModel):

    title_f: DescriptionTitle
    description_f: DescriptionString
    # year_f: int | None = None
    # director_f: str | None = None
    # budget_f: int | None = None


# 2. Схема для создания (POST) — не содержит id
class SMovieCreate(SMovieBase):
    """
    Схема для добавления нового фильма
    """

    id: int = None


# 3. Схема для частичного обновления (PATCH) — все поля опциональны
class SMoviePartitionUpdate(SMovieBase):
    """
    Схема для частичного обновления данных о фильме
    """

    title_f: DescriptionTitle | None = None
    description_f: DescriptionString | None = None
    # year_f: int | None = None
    # director_f: str | None = None
    # budget_f: int | None = None


# 4. Схема для обновления описания
class SMovieUpdate(BaseModel):
    """
    Схема для обновления описания к фильму
    """

    description_f: DescriptionString


# 5. Схема для чтения (GET, POST, PUT) — содержит id
class SMovieRead(SMovieBase):
    """
    Схема для чтения выборочных данных
    """

    # id: int = None


# 6. Схема для хранения доп инфо (GET, POST, PUT) — содержит id
class SMovie(SMovieBase):
    """
    Схема фильма
    """

    id: int
    notes: str = "Опционное поле для админа"
