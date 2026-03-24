from pydantic import BaseModel



class UserResponseDTO(BaseModel):
    id: str
    name: str