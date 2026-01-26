# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Tenant", "Database", "Group"]


class Database(BaseModel):
    """Database information in tenant responses."""

    id: str
    """Database ID"""

    name: str
    """Database name"""


class Group(BaseModel):
    """Group information in tenant responses."""

    id: str
    """Group ID"""

    name: str
    """Group name"""


class Tenant(BaseModel):
    """Response model for a single tenant."""

    id: str
    """Tenant ID"""

    created_at: datetime
    """Creation timestamp"""

    databases: List[Database]
    """Associated databases"""

    groups: List[Group]
    """Associated groups"""

    name: Optional[str] = None
    """Human-readable tenant name"""

    tenant_key: str
    """Unique tenant identifier"""

    updated_at: datetime
    """Last update timestamp"""
