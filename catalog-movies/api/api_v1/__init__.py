from fastapi import (
    APIRouter,
    Request,
)

# первая версия API
router = APIRouter(
    prefix="/v1",
)


@router.get("/")
def api_v1_init(
    request: Request,
):
    return {
        "message": f"Hello! this is API_v1",
        "docs": "API_v1",
    }
