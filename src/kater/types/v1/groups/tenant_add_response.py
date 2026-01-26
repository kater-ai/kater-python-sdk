# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["TenantAddResponse"]


class TenantAddResponse(BaseModel):
    """Response model for add tenants operation."""

    added: List[str]
    """Tenant IDs that were successfully added"""

    already_in_group: List[str]
    """Tenant IDs that were already members"""

    not_found: List[str]
    """Tenant IDs that don't exist"""
