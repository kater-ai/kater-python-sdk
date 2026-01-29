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
    "WarehouseMetadataPostgresMetadata",
    "WarehouseMetadataDatabricksMetadata",
    "WarehouseMetadataClickHouseMetadata",
    "WarehouseMetadataMssqlMetadata",
]


class DatabaseSchema(BaseModel):
    """Schema info from ConnectionSchema."""

    id: str
    """Schema ID"""

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
    """Snowflake-specific warehouse metadata."""

    auth_method: Literal["username_password", "key_pair"]
    """Authentication method"""

    role: str
    """Snowflake role"""

    snowflake_account_id: str
    """Snowflake account identifier"""

    warehouse: str
    """Compute warehouse name"""

    warehouse_type: Literal["snowflake"]
    """Warehouse type discriminator"""


class WarehouseMetadataPostgresMetadata(BaseModel):
    """PostgreSQL-specific warehouse metadata."""

    host: str
    """Database host"""

    port: int
    """Database port"""

    warehouse_type: Literal["postgresql"]
    """Warehouse type discriminator"""


class WarehouseMetadataDatabricksMetadata(BaseModel):
    """Databricks-specific warehouse metadata."""

    http_path: str
    """SQL warehouse HTTP path"""

    server_hostname: str
    """Databricks server hostname"""

    warehouse_type: Literal["databricks"]
    """Warehouse type discriminator"""


class WarehouseMetadataClickHouseMetadata(BaseModel):
    """ClickHouse-specific warehouse metadata."""

    host: str
    """ClickHouse host"""

    port: int
    """ClickHouse port"""

    warehouse_type: Literal["clickhouse"]
    """Warehouse type discriminator"""


class WarehouseMetadataMssqlMetadata(BaseModel):
    """Microsoft SQL Server-specific warehouse metadata."""

    host: str
    """SQL Server host"""

    port: int
    """SQL Server port"""

    warehouse_type: Literal["mssql"]
    """Warehouse type discriminator"""


WarehouseMetadata: TypeAlias = Annotated[
    Union[
        WarehouseMetadataSnowflakeMetadata,
        WarehouseMetadataPostgresMetadata,
        WarehouseMetadataDatabricksMetadata,
        WarehouseMetadataClickHouseMetadata,
        WarehouseMetadataMssqlMetadata,
    ],
    PropertyInfo(discriminator="warehouse_type"),
]


class Connection(BaseModel):
    """Response model for a single connection.

    All data comes from the database (source of truth).
    JSON responses use 'id' field; YAML responses transform to 'kater_id' via MultiFormatRoute.
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

    database_timezone: Optional[str] = None
    """Default timezone for the connection"""

    description: Optional[str] = None
    """Connection description"""

    label: Optional[str] = None
    """Human-readable label"""

    query_timeout: Optional[int] = None
    """Query timeout in seconds"""

    query_timezone_conversion: Optional[str] = None
    """Timezone conversion mode (do_not_convert, convert_to_utc)"""

    sync_id: Optional[str] = None
    """Sync identifier for schema sync"""
