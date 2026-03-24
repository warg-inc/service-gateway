from src.application.dto.user import UserResponseDTO
from src.protos.generated import user_pb2




def user_from_proto(response: user_pb2.GetUserResponse) -> UserResponseDTO:
    return UserResponseDTO(
        id=response.user_id,
        name=response.name,
    )