import grpc

from contextlib import asynccontextmanager
from fastapi import FastAPI


from src.presentation.http.controllers.root_router import create_root_router
from src.setup.config.config import get_settings
from src.setup.grpc_factory import create_grpc_clients


@asynccontextmanager
async def lifespan(app: FastAPI):
    clients, channels = create_grpc_clients(get_settings())

    app.state.grpc_clients = clients

    yield

    for ch in channels:
        await ch.close()



def create_web_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(create_root_router())

    return app