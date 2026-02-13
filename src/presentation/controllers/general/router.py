from fastapi import APIRouter
from .health import create_health_router

def create_general_router() -> APIRouter:
    router = APIRouter(tags=["General"])
    router.include_router(create_health_router())

    return router