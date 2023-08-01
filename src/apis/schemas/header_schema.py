from pydantic import BaseModel


class HeaderSchema(BaseModel):
    """
    The Message Response scheme represents the simplest response that is possible to return
    """

    message: str
