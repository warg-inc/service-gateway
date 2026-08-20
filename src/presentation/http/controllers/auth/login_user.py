from fastapi import APIRouter, Depends, HTTPException, status

from src.application.dto.auth import LoginUserResponseDTO, LoginUserRequestDTO
from src.infrastructure.clients.grpc.container import GRPCClients
from src.presentation.http.controllers.users.users_grpc import get_grpc_clients
from src.presentation.http.schemas.auth.login_user import LoginRequestSchema, LoginResponseSchema
from src.application.exceptions.grpc_exceptions import UnauthenticatedError


def create_login_user_router() -> APIRouter:
    router = APIRouter()

    @router.post("/login_user", response_model=LoginResponseSchema)
    async def login_user(data: LoginRequestSchema, grpc_clients: GRPCClients = Depends(get_grpc_clients)) -> LoginResponseSchema:
        dto = LoginUserRequestDTO(
            email=str(data.email),
            password=data.password
        )

        try:
            response: LoginUserResponseDTO = await grpc_clients.auth.login_user(dto)
        except UnauthenticatedError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")            

        return LoginResponseSchema(
            access_token=response.access_token,
            refresh_token=response.refresh_token
        )

    return router
