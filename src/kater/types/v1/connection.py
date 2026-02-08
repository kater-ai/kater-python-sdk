# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Connection",
    "Database",
    "DatabaseSchema",
    "WarehouseMetadata",
    "WarehouseMetadataSnowflakeMetadata",
    "WarehouseMetadataPostgresqlMetadata",
    "WarehouseMetadataDatabricksMetadata",
    "WarehouseMetadataClickhouseMetadata",
    "WarehouseMetadataMssqlMetadata",
]


class DatabaseSchema(BaseModel):
    """Schema info from ConnectionSchema."""

    id: str
    """Schema ID"""

    database_object_name: str
    """Actual name of the schema in the warehouse"""

    name: str
    """Schema name"""

    description: Optional[str] = None
    """Schema description"""

    label: Optional[str] = None
    """Human-readable label"""


class Database(BaseModel):
    """Database info from ConnectionSchema."""

    id: str
    """Database ID"""

    database_object_name: str
    """Actual name of the database in the warehouse"""

    name: str
    """Database name"""

    schemas: List[DatabaseSchema]
    """Schemas in this database"""

    description: Optional[str] = None
    """Database description"""

    label: Optional[str] = None
    """Human-readable label"""

    timezone: Optional[str] = None
    """Timezone for the database"""


class WarehouseMetadataSnowflakeMetadata(BaseModel):
    auth_method: Literal["username_password", "key_pair"]
    """Authentication method"""

    role: str
    """Snowflake role"""

    snowflake_account_id: str
    """Snowflake account identifier"""

    warehouse: str
    """Snowflake compute warehouse name"""

    warehouse_type: Literal["snowflake"]


class WarehouseMetadataPostgresqlMetadata(BaseModel):
    host: str
    """Database host address"""

    port: int
    """Database port (default: 5432)"""

    warehouse_type: Literal["postgresql"]


class WarehouseMetadataDatabricksMetadata(BaseModel):
    http_path: str
    """Databricks SQL warehouse HTTP path"""

    server_hostname: str
    """Databricks server hostname"""

    warehouse_type: Literal["databricks"]


class WarehouseMetadataClickhouseMetadata(BaseModel):
    host: str
    """ClickHouse host address"""

    port: int
    """ClickHouse port (default: 8443)"""

    warehouse_type: Literal["clickhouse"]


class WarehouseMetadataMssqlMetadata(BaseModel):
    host: str
    """SQL Server host address"""

    port: int
    """SQL Server port (default: 1433)"""

    warehouse_type: Literal["mssql"]


WarehouseMetadata: TypeAlias = Annotated[
    Union[
        WarehouseMetadataSnowflakeMetadata,
        WarehouseMetadataPostgresqlMetadata,
        WarehouseMetadataDatabricksMetadata,
        WarehouseMetadataClickhouseMetadata,
        WarehouseMetadataMssqlMetadata,
    ],
    PropertyInfo(discriminator="warehouse_type"),
]


class Connection(BaseModel):
    """Response model for a single connection.

    All data comes from the database (source of truth).
    For YAML-compatible output with 'kater_id', use the /schema endpoint instead.
    """

    id: str
    """Connection ID"""

    created_at: datetime
    """Creation timestamp"""

    credential_id: str
    """Credential ID"""

    databases: List[Database]
    """Databases in this connection"""

    name: str
    """Connection name"""

    updated_at: datetime
    """Last update timestamp"""

    warehouse_metadata: WarehouseMetadata
    """Warehouse-specific configuration"""

    warehouse_type: str
    """Warehouse type (snowflake, postgresql, etc.)"""

    approval_pr_url: Optional[str] = None
    """GitHub PR URL for approving the connection (None if already approved)"""

    description: Optional[str] = None
    """Connection description"""

    is_pending_approval: Optional[bool] = None
    """True if this connection is awaiting PR approval"""

    label: Optional[str] = None
    """Human-readable label"""

    query_timeout: Optional[int] = None
    """Query timeout in seconds"""

    query_timezone_conversion: Optional[str] = None
    """Timezone conversion mode (do_not_convert, convert_to_utc)"""
