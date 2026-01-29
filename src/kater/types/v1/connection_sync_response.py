# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConnectionSyncResponse"]


class ConnectionSyncResponse(BaseModel):
    """Response for syncing views.

    Returned after successfully creating a PR with merged ViewSchema files,
    or indicating that all views are already up to date.
    """

    views_updated: int
    """Number of views in the PR"""

    message: Optional[str] = None
    """Status message"""

    pr_number: Optional[int] = None
    """GitHub PR number"""

    pr_url: Optional[str] = None
    """GitHub PR URL"""
