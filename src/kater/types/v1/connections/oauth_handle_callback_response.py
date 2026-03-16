# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["OAuthHandleCallbackResponse"]


class OAuthHandleCallbackResponse(BaseModel):
    """Response after successful OAuth callback."""

    connected_at: datetime

    connection_status: str

    mcp_id: str
