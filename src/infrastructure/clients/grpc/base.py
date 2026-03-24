import grpc



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

            if code == grpc.StatusCode.NOT_FOUND:
                raise Exception("Resource not found")

            if code == grpc.StatusCode.UNAVAILABLE:
                raise Exception("Service unavailable")

            raise Exception(f"gRPC error: {code.name}")


