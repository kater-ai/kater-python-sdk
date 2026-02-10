# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ImportTenantsResponse", "Error"]


class Error(BaseModel):
    """Error for a single tenant during import."""

    code: str
    """Error code"""

    message: str
    """Error message"""

    tenant_key: str
    """Tenant key that failed"""


class ImportTenantsResponse(BaseModel):
    """Response model for tenant import operation."""

    total_found: int
    """Unique tenant keys found in source"""

    total_imported: int
    """New tenants created"""

    total_updated: int
    """Existing tenants updated"""

    errors: Optional[List[Error]] = None
    """Tenant-specific errors"""

    groups_created: Optional[List[str]] = None
    """Groups that were auto-created"""
