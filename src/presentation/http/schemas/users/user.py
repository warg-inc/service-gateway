from pydantic import BaseModel


class UserResponseSchemas(BaseModel):
    id: str
    name: str