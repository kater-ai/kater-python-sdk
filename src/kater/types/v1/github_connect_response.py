# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["GitHubConnectResponse"]


class GitHubConnectResponse(BaseModel):
    """Response for starting OAuth flow."""

    authorization_url: str

    state: str
