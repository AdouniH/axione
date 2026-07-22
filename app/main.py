from fastapi import FastAPI

from app.api.v1.router import api_router
from app.db.base import init_db


app = FastAPI(title="Axione API")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


app.include_router(api_router, prefix="/api/v1")
