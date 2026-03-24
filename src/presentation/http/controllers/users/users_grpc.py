from fastapi import (
    APIRouter,
    Depends,
    Request
)

from src.application.dto.user import UserResponseDTO
from src.infrastructure.clients.grpc.container import GRPCClients
from src.presentation.http.schemas.users.user import UserResponseSchemas

def get_grpc_clients(request: Request) -> GRPCClients:
    return request.app.state.grpc_clients

def create_users_grpc_router() -> APIRouter:
    router = APIRouter(prefix="/grpc")

    @router.get("/users/{user_id}", response_model=UserResponseSchemas)
    async def get_user_by_id(
        user_id: str,
        grpc_clients: GRPCClients = Depends(get_grpc_clients)
    ):
        user: UserResponseDTO = await grpc_clients.auth.get_user(user_id)

        return UserResponseSchemas(
            id=user.id,
            name=user.name
        )

    return router

