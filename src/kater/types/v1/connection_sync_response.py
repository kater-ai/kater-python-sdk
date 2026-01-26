# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ConnectionSyncResponse"]


class ConnectionSyncResponse(BaseModel):
    """Response for syncing views.

    Returned after successfully creating a PR with merged ViewSchema files.
    """

    pr_number: int
    """GitHub PR number"""

    pr_url: str
    """GitHub PR URL"""

    views_updated: int
    """Number of views in the PR"""
