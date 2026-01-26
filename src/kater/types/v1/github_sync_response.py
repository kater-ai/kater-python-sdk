# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["GitHubSyncResponse"]


class GitHubSyncResponse(BaseModel):
    """Response for sync operation."""

    last_sync_at: str

    message: str

    success: bool
