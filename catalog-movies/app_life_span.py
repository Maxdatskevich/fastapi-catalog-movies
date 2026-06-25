from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.api_v1.films.crud import storage_movie


@asynccontextmanager
async def lifespan(app: FastAPI):
    # действия до запуска приложения
    storage_movie.init_storage_movie_from_state()
    # ставим эту функцию на паузу на время работы приложегния
    yield
    # выполняем завершение работы
    # закрываем соединение, сохраняем, сохраняем файлы
