# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .batch_tenant_error import BatchTenantError
from .batch_tenant_success import BatchTenantSuccess

__all__ = ["BatchDeleteResponse"]


class BatchDeleteResponse(BaseModel):
    """Response model for batch tenant deletions."""

    failed: List[BatchTenantError]
    """Failed tenant deletions"""

    succeeded: List[BatchTenantSuccess]
    """Successfully deleted tenants"""
