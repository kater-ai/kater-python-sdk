# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ConnectionUpdateCredentialsResponse"]


class ConnectionUpdateCredentialsResponse(BaseModel):
    """Response for credential update."""

    connection_id: str
    """Connection ID"""

    success: bool
    """Whether the credential update was successful"""
