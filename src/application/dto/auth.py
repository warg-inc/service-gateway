from dataclasses import dataclass



@dataclass(frozen=True)
class LoginUserRequestDTO:
    email: str
    password: str


@dataclass(frozen=True)
class LoginUserResponseDTO:
    access_token: str
    refresh_token: str
