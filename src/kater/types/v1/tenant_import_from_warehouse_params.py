# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TenantImportFromWarehouseParams"]


class TenantImportFromWarehouseParams(TypedDict, total=False):
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

    source: Optional[str]

    attribute_columns: Optional[Dict[str, str]]
    """Mapping of attribute names to warehouse column names for attribute import"""

    tenant_group_column: Optional[str]
    """Column name for tenant group (optional)"""

    tenant_name_column: Optional[str]
    """Column name for tenant display name (optional)"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
