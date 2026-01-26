# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .batch_tenant_error import BatchTenantError
from .batch_tenant_success import BatchTenantSuccess

__all__ = ["BatchCreateResponse"]


class BatchCreateResponse(BaseModel):
    """Response model for batch tenant creation."""

    failed: List[BatchTenantError]
    """Failed tenant creations"""

    succeeded: List[BatchTenantSuccess]
    """Successfully created tenants"""
