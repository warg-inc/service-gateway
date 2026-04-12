from src.application.dto.user import RegisterUserRequestDTO, RegisterUserResponseDTO
from src.infrastructure.clients.grpc.base import BaseGRPCClient
from src.protos.generated import user_pb2_grpc, user_pb2, auth_pb2_grpc, auth_pb2


class AuthGRPCClient(BaseGRPCClient):
    def __init__(self, channel):
        self.user_stub = user_pb2_grpc.UserServiceStub(channel)
        self.auth_stub = auth_pb2_grpc.AuthServiceStub(channel)

    async def register_user(self, dto: RegisterUserRequestDTO) -> RegisterUserResponseDTO:
        request = auth_pb2.RegisterRequest(
            email=dto.email,
            surname=dto.surname,
            name=dto.name,
            password=dto.password
        )

        response: auth_pb2.RegisterResponse = await self._call(self.auth_stub.RegisterUser, request)

        return RegisterUserResponseDTO(success=response.success)