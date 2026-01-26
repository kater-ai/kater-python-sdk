# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["TenantUpdateParams"]


class TenantUpdateParams(TypedDict, total=False):
    connection_id: Optional[str]
    """Connection ID for database association (required with database_name)"""

    database_name: Optional[str]
    """Database name for association (required with connection_id)"""

    group_names: Optional[SequenceNotStr[str]]
    """New list of group names (replaces all existing associations)"""

    tenant_name: Optional[str]
    """New human-readable tenant name"""
