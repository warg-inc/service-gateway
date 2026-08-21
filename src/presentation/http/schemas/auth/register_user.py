from pydantic import BaseModel, EmailStr, Field




class RegisterRequestSchema(BaseModel):
    email: EmailStr
    surname: str = Field(min_length=1, max_length=100)
    name: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=6, max_length=100)


class RegisterResponseSchema(BaseModel):
    success: bool