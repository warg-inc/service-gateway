from dataclasses import dataclass

from src.infrastructure.clients.grpc.auth_grpc_client import AuthGRPCClient


@dataclass(frozen=True)
class GRPCClients:
    auth: AuthGRPCClient