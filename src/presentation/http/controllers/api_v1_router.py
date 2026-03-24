from fastapi import APIRouter

from .auth.router import create_auth_router
from .general.router import create_general_router
from .users.router import create_users_router


def create_api_v1_router() -> APIRouter:
    router = APIRouter(prefix="/api/v1")

    router.include_router(create_general_router())
    router.include_router(create_auth_router())
    router.include_router(create_users_router())

    return router
