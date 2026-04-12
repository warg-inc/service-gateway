from fastapi import APIRouter, Depends

from src.application.dto.user import RegisterUserRequestDTO, RegisterUserResponseDTO
from src.infrastructure.clients.grpc.container import GRPCClients
from src.presentation.http.controllers.users.users_grpc import get_grpc_clients
from src.presentation.http.schemas.auth.register_user import RegisterResponseSchema, RegisterRequestSchema


def create_register_user_router() -> APIRouter:
    router = APIRouter()

    @router.post("/register_user", response_model=RegisterResponseSchema)
    async def register_user(data: RegisterRequestSchema, grpc_clients: GRPCClients = Depends(get_grpc_clients)) -> RegisterResponseSchema:
        dto = RegisterUserRequestDTO(
            email=str(data.email),
            surname=data.surname,
            name=data.name,
            password=data.password
        )

        response: RegisterUserResponseDTO = await grpc_clients.auth.register_user(dto)

        return RegisterResponseSchema(success=response.success)
    return router