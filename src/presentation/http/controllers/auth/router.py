from fastapi import(
    APIRouter,
)

from src.presentation.http.controllers.auth.send_otp import create_send_otp_router


def create_auth_router() -> APIRouter:
    router = APIRouter(prefix="/auth", tags=["Auth"])
    router.include_router(create_send_otp_router())

    return router
