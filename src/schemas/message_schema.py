from pydantic import BaseModel


class MessageResponseSchema(BaseModel):
    """
    The Message Response schema represents the simplest response that is possible to return
    """

    message: str
