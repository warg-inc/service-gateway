import grpc

from src.application.exceptions.grpc_exceptions import (
    NotFoundError,
    ServiceUnavailableError,
    AlreadyExistsError,
    InvalidArgumentError,
    UnauthenticatedError,
    GRPCError,
)


class BaseGRPCClient:
    DEFAULT_TIMEOUT = 3.0

    async def _call(self, rpc, request, timeout=None):
        try:
            return await rpc(
                request,
                timeout=timeout or self.DEFAULT_TIMEOUT
            )

        except grpc.aio.AioRpcError as e:
            code = e.code()
            details = e.details()

            if code == grpc.StatusCode.NOT_FOUND:
                raise NotFoundError(details)

            if code == grpc.StatusCode.UNAVAILABLE:
                raise ServiceUnavailableError(details)

            if code == grpc.StatusCode.ALREADY_EXISTS:
                raise AlreadyExistsError(details)

            if code == grpc.StatusCode.INVALID_ARGUMENT:
                raise InvalidArgumentError(details)

            if code == grpc.StatusCode.UNAUTHENTICATED:
                raise UnauthenticatedError(details)

            # 🔥 fallback
            raise GRPCError(f"{code.name}: {details}")
