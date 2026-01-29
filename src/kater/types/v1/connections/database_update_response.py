# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..connection import Connection

__all__ = ["DatabaseUpdateResponse"]


class DatabaseUpdateResponse(BaseModel):
    """Response for database/schema updates that may involve a rename PR."""

    connection: Connection
    """Updated connection"""

    pr_number: Optional[int] = None
    """GitHub PR number"""

    pr_status: Optional[str] = None
    """PR status: 'open' or 'merged'"""

    pr_url: Optional[str] = None
    """GitHub PR URL (if rename PR created)"""
