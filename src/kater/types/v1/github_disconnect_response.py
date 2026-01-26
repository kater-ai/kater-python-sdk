# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["GitHubDisconnectResponse"]


class GitHubDisconnectResponse(BaseModel):
    """Response for disconnecting GitHub."""

    message: str

    success: bool
