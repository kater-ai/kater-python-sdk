# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..tenant import Tenant
from ...._models import BaseModel

__all__ = ["BatchTenantSuccess"]


class BatchTenantSuccess(BaseModel):
    """Successful tenant operation in batch response."""

    tenant_id: str
    """Tenant ID"""

    tenant: Optional[Tenant] = None
    """Response model for a single tenant."""
