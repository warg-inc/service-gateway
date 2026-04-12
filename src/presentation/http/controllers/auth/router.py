from fastapi import(
    APIRouter,
)

from src.presentation.http.controllers.auth.send_otp import create_send_otp_router
from src.presentation.http.controllers.auth.register_user import create_register_user_router


def create_auth_router() -> APIRouter:
    router = APIRouter(prefix="/auth", tags=["Auth"])
    router.include_router(create_send_otp_router())
    router.include_router(create_register_user_router())

    return router
