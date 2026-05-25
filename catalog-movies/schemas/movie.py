from pydantic import BaseModel


# классы, которые описывают структуру данных
# Pydantic для автоматической генерации документации Swagger и OpenAPI.
class Movie(BaseModel):
    id: int  # уникальный номер
    title_f: str  # название
    description_f: str  # описание
    year_f: int | None = None  # год выпуска
    director_f: str | None = None  # режиссер
    budget_f: int | None = None  # бюджет
