# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ......_models import BaseModel

__all__ = ["CredentialCreateResponse"]


class CredentialCreateResponse(BaseModel):
    """Response model after creating a credential (never contains the API key)."""

    connected_at: datetime

    connection_status: str

    mcp_id: str
