# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["BatchUpdateParams", "Tenant"]


class BatchUpdateParams(TypedDict, total=False):
    tenants: Required[Iterable[Tenant]]
    """List of tenant updates"""


class Tenant(TypedDict, total=False):
    """Single tenant update in a batch operation."""

    tenant_id: Required[str]
    """Tenant ID to update"""

    connection_id: Optional[str]
    """Connection ID for database association (required with database_name)"""

    database_name: Optional[str]
    """Database name for association (required with connection_id)"""

    group_names: Optional[SequenceNotStr[str]]
    """New list of group names (replaces all existing associations)"""

    tenant_name: Optional[str]
    """New human-readable tenant name"""
