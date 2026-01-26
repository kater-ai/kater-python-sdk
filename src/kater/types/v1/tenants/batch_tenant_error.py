# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatchTenantError"]


class BatchTenantError(BaseModel):
    """Failed tenant operation in batch response."""

    code: str
    """Error code"""

    message: str
    """Error message"""

    index: Optional[int] = None
    """Index in request array (for create operations)"""

    tenant_id: Optional[str] = None
    """Tenant ID (for update/delete operations)"""

    tenant_key: Optional[str] = None
    """Tenant key (for create operations)"""
