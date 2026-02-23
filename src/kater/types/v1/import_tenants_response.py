# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ImportTenantsResponse", "AttributeError", "Error"]


class AttributeError(BaseModel):
    """Error for a single attribute during import."""

    attribute: str
    """Attribute name that failed"""

    error: str
    """Error message"""

    tenant_key: str
    """Tenant key for which attribute processing failed"""

    value: str
    """Value that caused the error"""


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

    attribute_errors: Optional[List[AttributeError]] = None
    """Non-fatal attribute validation errors during import"""

    errors: Optional[List[Error]] = None
    """Tenant-specific errors"""

    groups_created: Optional[List[str]] = None
    """Groups that were auto-created"""
