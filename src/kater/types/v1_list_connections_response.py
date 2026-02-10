# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "V1ListConnectionsResponse",
    "V1ListConnectionsResponseItem",
    "V1ListConnectionsResponseItemDatabase",
    "V1ListConnectionsResponseItemDatabaseSchema",
    "V1ListConnectionsResponseItemWarehouseMetadata",
    "V1ListConnectionsResponseItemWarehouseMetadataSnowflakeMetadata",
    "V1ListConnectionsResponseItemWarehouseMetadataPostgresqlMetadata",
    "V1ListConnectionsResponseItemWarehouseMetadataDatabricksMetadata",
    "V1ListConnectionsResponseItemWarehouseMetadataClickhouseMetadata",
    "V1ListConnectionsResponseItemWarehouseMetadataMssqlMetadata",
]


class V1ListConnectionsResponseItemDatabaseSchema(BaseModel):
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


class V1ListConnectionsResponseItemDatabase(BaseModel):
    """Database info from ConnectionSchema."""

    id: str
    """Database ID"""

    database_object_name: str
    """Actual name of the database in the warehouse"""

    name: str
    """Database name"""

    schemas: List[V1ListConnectionsResponseItemDatabaseSchema]
    """Schemas in this database"""

    description: Optional[str] = None
    """Database description"""

    label: Optional[str] = None
    """Human-readable label"""

    timezone: Optional[str] = None
    """Timezone for the database"""


class V1ListConnectionsResponseItemWarehouseMetadataSnowflakeMetadata(BaseModel):
    auth_method: Literal["username_password", "key_pair"]
    """Authentication method"""

    role: str
    """Snowflake role"""

    snowflake_account_id: str
    """Snowflake account identifier"""

    warehouse: str
    """Snowflake compute warehouse name"""

    warehouse_type: Literal["snowflake"]


class V1ListConnectionsResponseItemWarehouseMetadataPostgresqlMetadata(BaseModel):
    host: str
    """Database host address"""

    port: int
    """Database port (default: 5432)"""

    warehouse_type: Literal["postgresql"]


class V1ListConnectionsResponseItemWarehouseMetadataDatabricksMetadata(BaseModel):
    http_path: str
    """Databricks SQL warehouse HTTP path"""

    server_hostname: str
    """Databricks server hostname"""

    warehouse_type: Literal["databricks"]


class V1ListConnectionsResponseItemWarehouseMetadataClickhouseMetadata(BaseModel):
    host: str
    """ClickHouse host address"""

    port: int
    """ClickHouse port (default: 8443)"""

    warehouse_type: Literal["clickhouse"]


class V1ListConnectionsResponseItemWarehouseMetadataMssqlMetadata(BaseModel):
    host: str
    """SQL Server host address"""

    port: int
    """SQL Server port (default: 1433)"""

    warehouse_type: Literal["mssql"]


V1ListConnectionsResponseItemWarehouseMetadata: TypeAlias = Annotated[
    Union[
        V1ListConnectionsResponseItemWarehouseMetadataSnowflakeMetadata,
        V1ListConnectionsResponseItemWarehouseMetadataPostgresqlMetadata,
        V1ListConnectionsResponseItemWarehouseMetadataDatabricksMetadata,
        V1ListConnectionsResponseItemWarehouseMetadataClickhouseMetadata,
        V1ListConnectionsResponseItemWarehouseMetadataMssqlMetadata,
    ],
    PropertyInfo(discriminator="warehouse_type"),
]


class V1ListConnectionsResponseItem(BaseModel):
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

    databases: List[V1ListConnectionsResponseItemDatabase]
    """Databases in this connection"""

    name: str
    """Connection name"""

    updated_at: datetime
    """Last update timestamp"""

    warehouse_metadata: V1ListConnectionsResponseItemWarehouseMetadata
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


V1ListConnectionsResponse: TypeAlias = List[V1ListConnectionsResponseItem]
