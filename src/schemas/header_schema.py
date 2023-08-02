from pydantic import BaseModel, Field


class HeaderSchema(BaseModel):
    """
    TODO: add description
    """

    miauserid: str = 'miauserid'
    miausergroups: str = 'miausergroups'
    miaclienttype: str = 'miaclienttype'
    client_type: str = Field(
        default='client-type',
        alias='client-type'
    )
    x_request_id: str = Field(
        default='x-request-id',
        alias='x-request-id'
    )
