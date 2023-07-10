from pydantic import BaseModel


class HeaderRequest(BaseModel):
    """
    Mia Platform required headers
    """

    USERID_HEADER_KEY: str
    GROUPS_HEADER_KEY: str
    CLIENTTYPE_HEADER_KEY: str
    BACKOFFICE_HEADER_KEY: str
