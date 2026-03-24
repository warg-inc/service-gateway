from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache



class Settings(BaseSettings):
    auth_grpc_host: str
    auth_grpc_port: int

    debug: bool = False
    secret_key: str = "default-secret"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        extra="ignore",
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()