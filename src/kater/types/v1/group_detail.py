# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["GroupDetail", "Tenant"]


class Tenant(BaseModel):
    """Tenant information in group responses."""

    id: str
    """Tenant ID"""

    name: Optional[str] = None
    """Human-readable tenant name"""

    tenant_key: str
    """Unique tenant identifier"""


class GroupDetail(BaseModel):
    """Response model for a single group (with full tenant list)."""

    id: str
    """Group ID"""

    created_at: datetime
    """Creation timestamp"""

    description: Optional[str] = None
    """Group description"""

    name: str
    """Group name"""

    tenants: List[Tenant]
    """Tenants in this group"""

    updated_at: datetime
    """Last update timestamp"""
