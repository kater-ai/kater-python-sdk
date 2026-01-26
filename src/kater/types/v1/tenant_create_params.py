# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TenantCreateParams"]


class TenantCreateParams(TypedDict, total=False):
    tenant_key: Required[str]
    """Unique tenant identifier within the client"""

    connection_id: Optional[str]
    """Connection ID (required for DATABASE tenancy type)"""

    database_name: Optional[str]
    """Database name (required for DATABASE tenancy type)"""

    group_names: Optional[SequenceNotStr[str]]
    """List of group names to associate with the tenant"""

    tenant_name: Optional[str]
    """Human-readable tenant name"""
