import random
from pydantic import BaseModel, Field
from typing import Annotated, Optional
from annotated_types import Len


# классы, которые описывают структуру данных
# Pydantic для автоматической генерации документации Swagger и OpenAPI.
class MovieBase(BaseModel):
    id: int | None = None
    title_f: str = Field(..., min_length=3)
    description_f: str = Field(..., min_length=3)
    year_f: int | None = None  # год выпуска
    director_f: str | None = None  # режиссер
    budget_f: int | None = None  # бюджет


class MovieAdd(MovieBase):
    """
    Модель для добавления нового фильма
    """

    title_f: Annotated[str, Len(1, 50)]
    description_f: Annotated[str, Len(1, 300)]


class Movie(MovieBase):
    """
    Модель фильма
    """
