class GRPCError(Exception):
    pass


class NotFoundError(GRPCError):
    pass


class ServiceUnavailableError(GRPCError):
    pass


class AlreadyExistsError(GRPCError):
    pass


class InvalidArgumentError(GRPCError):
    pass


class UnauthenticatedError(GRPCError):
    pass
