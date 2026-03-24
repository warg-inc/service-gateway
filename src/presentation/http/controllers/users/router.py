from fastapi import (
    APIRouter
)

from src.presentation.http.controllers.users.users_grpc import create_users_grpc_router


def create_users_router() -> APIRouter:
    router = APIRouter(prefix="/users", tags=["Users"])

    router.include_router(create_users_grpc_router())

    return router
