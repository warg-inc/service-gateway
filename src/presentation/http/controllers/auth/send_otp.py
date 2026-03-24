from fastapi import(
    APIRouter,

)

from src.presentation.http.schemas.auth.send_otp import(
    SendOtpResponseSchema,
    SendOtpRequestSchema,
    PhoneSendOtpRequestSchema,
    EmailSendOtpRequestSchema,
)


def create_send_otp_router() -> APIRouter:
    router = APIRouter()

    @router.post("/send-otp", response_model=SendOtpResponseSchema)
    async def send_otp(data: SendOtpRequestSchema):
        match data:
            case PhoneSendOtpRequestSchema(identifier=phone):
                print(f"{phone=}")
                return SendOtpResponseSchema(success=True)
            case EmailSendOtpRequestSchema(identifier=email):
                print(f"{email=}")
                return SendOtpResponseSchema(success=True)
            case _:
                return SendOtpResponseSchema(success=False)

    return router

