# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["GroupListResponse", "GroupListResponseItem"]


class GroupListResponseItem(BaseModel):
    """Response model for a group in list responses (with tenant count)."""

    id: str
    """Group ID"""

    created_at: datetime
    """Creation timestamp"""

    description: Optional[str] = None
    """Group description"""

    name: str
    """Group name"""

    tenant_count: int
    """Number of tenants in this group"""

    updated_at: datetime
    """Last update timestamp"""


GroupListResponse: TypeAlias = List[GroupListResponseItem]
