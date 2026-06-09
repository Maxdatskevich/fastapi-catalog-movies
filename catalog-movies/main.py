from fastapi import (
    FastAPI,
)
from starlette.requests import Request

from api.api_v1 import router as api_v1_router
from api import router as api_router

app = FastAPI(title="Catalog movies_dict")

app.include_router(api_v1_router)
app.include_router(api_router)


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
        "message": f"Hello friend 😎",
        "docs": str(docs_url),
    }
