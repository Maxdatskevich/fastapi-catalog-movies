import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MOVIES_STORAGE_FILEPATH = BASE_DIR / "movies.json"

LOG_LEVEl = logging.INFO
LOG_FORMAT: str = (
    "[%(asctime)s] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)
