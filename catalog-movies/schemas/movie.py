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
# 1. Базовый класс (общие поля)
class MovieBase(BaseModel):
    id: int | None = None
    title_f: DescriptionTitle


# 2. Класс для создания (ничего не добавляет, просто копирует базу п.1)
class MovieCreate(BaseModel):
    """
    Модель для добавления нового фильма
    """

    title_f: DescriptionTitle
    description_f: DescriptionString
    year_f: int | None = None  # год выпуска
    director_f: str | None = None  # режиссер
    budget_f: int | None = None  # бюджет


class MoviePartitionUpdate(MovieCreate):
    """
    Модель для частичного обновления данных о фильме
    """

    title_f: DescriptionTitle
    description_f: DescriptionString
    year_f: int | None = None  # год выпуска
    director_f: str | None = None  # режиссер
    budget_f: int | None = None  # бюджет


class MovieUpdateData(MovieCreate):
    """
    Модель для обновления описания к фильму
    """

    title_f: DescriptionTitle
    description_f: DescriptionString


# 3. Класс для чтения
class MovieRead(MovieCreate):
    """
    Модель фильма
    """

    id: int
