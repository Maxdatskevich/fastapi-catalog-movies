import random
from pydantic import BaseModel, Field
from typing import Annotated, Optional
from annotated_types import Len


# классы, которые описывают структуру данных
# Pydantic для автоматической генерации документации Swagger и OpenAPI.
# 1. Базовый класс (общие поля)
class MovieBase(BaseModel):

    title_f: Annotated[
        str,
        Len(min_length=1, max_length=50),
    ]
    description_f: Annotated[
        str,
        Len(min_length=1, max_length=300),
    ]
    year_f: int | None = None  # год выпуска
    director_f: str | None = None  # режиссер
    budget_f: int | None = None  # бюджет


# 2. Класс для создания (ничего не добавляет, просто копирует базу п.1)
class MovieCreate(MovieBase):
    """
    Модель для добавления нового фильма
    """

    id: int | None = None


class MovieUpdateData(BaseModel):
    """
    Модель для обновления описания к фильму
    """

    title_f: Annotated[
        str,
        Len(min_length=1, max_length=50),
    ]
    description_f: Annotated[
        str,
        Len(min_length=3, max_length=300),
    ]


# 3. Класс для чтения
class MovieRead(MovieCreate):
    """
    Модель фильма
    """
