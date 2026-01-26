# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ImportFromWarehouseParams"]


class ImportFromWarehouseParams(TypedDict, total=False):
    connection_id: Required[str]
    """Warehouse connection ID to query"""

    database: Required[str]
    """Database name containing the tenant table"""

    schema: Required[str]
    """Schema name containing the tenant table"""

    table: Required[str]
    """Table name containing tenant data"""

    tenant_key_column: Required[str]
    """Column name for tenant key"""

    tenant_group_column: Optional[str]
    """Column name for tenant group (optional)"""

    tenant_name_column: Optional[str]
    """Column name for tenant display name (optional)"""
