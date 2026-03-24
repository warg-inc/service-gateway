from src.application.dto.user import UserResponseDTO
from src.infrastructure.clients.grpc.base import BaseGRPCClient
from src.infrastructure.clients.grpc.mappers.user_mapper import user_from_proto
from src.protos.generated import user_pb2_grpc, user_pb2


class AuthGRPCClient(BaseGRPCClient):
    def __init__(self, channel):
        self.stub = user_pb2_grpc.UserServiceStub(channel)

    async def get_user(self, user_id: str) -> UserResponseDTO:
        request = user_pb2.GetUserRequest(user_id=user_id)

        response: user_pb2.GetUserResponse = await self._call(self.stub.GetUser, request)

        return user_from_proto(response)