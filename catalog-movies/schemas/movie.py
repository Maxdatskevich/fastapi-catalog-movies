import random
from pydantic import BaseModel, Field
from typing import Annotated, Optional
from annotated_types import Len


# классы, которые описывают структуру данных
# Pydantic для автоматической генерации документации Swagger и OpenAPI.
class Movie(BaseModel):
    id: int
    title_f: str
    description_f: str
    year_f: int | None = None  # год выпуска
    director_f: str | None = None  # режиссер
    budget_f: int | None = None  # бюджет


class MovieAdd(Movie):
    """
    Модель для добавления нового фильма
    """

    id: Optional[int] = random.randint(5, 1000)
    title_f: Annotated[str, Len(1, 50)]
    description_f: Annotated[str, Len(1, 300)]
