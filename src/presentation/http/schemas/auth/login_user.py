from pydantic import BaseModel, EmailStr, Field




class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
