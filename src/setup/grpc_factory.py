import grpc

from src.infrastructure.clients.grpc.auth_grpc_client import AuthGRPCClient
from src.infrastructure.clients.grpc.container import GRPCClients
from src.setup.config.config import Settings, get_settings



def create_channels(settings: Settings):
    options = [
        ("grpc.keepalive_time_ms", 10_000),
        ("grpc.keepalive_timeout_ms", 5_000),
        ("grpc.keepalive_permit_without_calls", True),
        ("grpc.http2.max_pings_without_data", 0),
    ]

    auth_channel = grpc.aio.insecure_channel(
        f"{settings.auth_grpc_host}:{settings.auth_grpc_port}",
        options=options,
    )

    return auth_channel


def create_grpc_clients(settings: Settings):
    auth_channel = create_channels(settings)

    clients = GRPCClients(auth=AuthGRPCClient(auth_channel))

    return clients, (auth_channel,)