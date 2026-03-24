from typing import(
    Literal,
    Annotated,
    Union,
)

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)


class PhoneSendOtpRequestSchema(BaseModel):
    model_config = ConfigDict(extra='forbid', populate_by_name=True)

    type: Literal['phone']
    identifier: int

class EmailSendOtpRequestSchema(BaseModel):
    model_config = ConfigDict(extra='forbid', populate_by_name=True)

    type: Literal['email']
    identifier: EmailStr

class SendOtpResponseSchema(BaseModel):
    model_config = ConfigDict(extra='forbid', populate_by_name=True)

    success: bool


SendOtpRequestSchema = Annotated[
    Union[PhoneSendOtpRequestSchema, EmailSendOtpRequestSchema],
    Field(discriminator='type'),
]
