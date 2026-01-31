# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ConnectionRetrieveSchemaResponse",
    "WarehouseMetadata",
    "WarehouseMetadataSnowflakeMetadata",
    "WarehouseMetadataPostgresqlMetadata",
    "WarehouseMetadataDatabricksMetadata",
    "WarehouseMetadataClickhouseMetadata",
    "WarehouseMetadataMssqlMetadata",
    "Database",
    "DatabaseSchema",
]


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


class DatabaseSchema(BaseModel):
    database_object_name: str
    """The actual name of the schema object in the warehouse"""

    kater_id: str
    """Unique identifier for the schema"""

    name: str
    """Name of the schema"""

    ai_context: Optional[str] = None
    """Additional context for AI processing"""

    custom_properties: Optional[Dict[str, object]] = None
    """Custom properties"""

    description: Optional[str] = None
    """Description of the schema"""

    label: Optional[str] = None
    """Human-readable label for the schema"""


class Database(BaseModel):
    database_object_name: str
    """The actual name of the database object in the warehouse"""

    kater_id: str
    """Unique identifier for the database"""

    name: str
    """Name of the database"""

    ai_context: Optional[str] = None
    """Additional context for AI processing"""

    custom_properties: Optional[Dict[str, object]] = None
    """Custom properties"""

    description: Optional[str] = None
    """Description of the database"""

    label: Optional[str] = None
    """Human-readable label for the database"""

    schemas: Optional[List[DatabaseSchema]] = None
    """List of schemas in this database"""

    timezone: Optional[str] = None
    """Timezone for the database"""


class ConnectionRetrieveSchemaResponse(BaseModel):
    """Schema for Kater connection configuration files"""

    kater_id: str
    """Unique identifier for the connection"""

    name: str
    """Name of the connection"""

    warehouse_metadata: WarehouseMetadata
    """Warehouse-specific configuration (non-sensitive)"""

    ai_context: Optional[str] = None
    """Additional context for AI processing"""

    custom_properties: Optional[Dict[str, object]] = None
    """Custom properties"""

    databases: Optional[List[Database]] = None
    """List of databases in this connection"""

    description: Optional[str] = None
    """Description of the connection"""

    label: Optional[str] = None
    """Human-readable label for the connection"""

    query_timeout: Optional[int] = None
    """Query timeout in seconds"""

    query_timezone_conversion: Optional[Literal["do_not_convert", "convert_to_utc"]] = None
    """Timezone conversion mode for queries"""
