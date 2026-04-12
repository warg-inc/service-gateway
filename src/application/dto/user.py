from dataclasses import dataclass

@dataclass(frozen=True)
class RegisterUserRequestDTO:
    email: str
    surname: str
    name: str
    password: str


@dataclass(frozen=True)
class RegisterUserResponseDTO:
    success: bool