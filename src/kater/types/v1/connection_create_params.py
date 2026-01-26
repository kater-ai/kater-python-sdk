# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .database_config_param import DatabaseConfigParam

__all__ = [
    "ConnectionCreateParams",
    "PostgresConnectionConfig",
    "SnowflakeConnectionConfig",
    "SnowflakeConnectionConfigAuth",
    "SnowflakeConnectionConfigAuthSnowflakePasswordAuth",
    "SnowflakeConnectionConfigAuthSnowflakePrivateKeyAuth",
    "DatabricksConnectionConfig",
    "ClickHouseConnectionConfig",
    "MssqlConnectionConfig",
]


class PostgresConnectionConfig(TypedDict, total=False):
    databases: Required[Iterable[DatabaseConfigParam]]
    """Databases to include in the connection (at least one required)"""

    host: Required[str]
    """Database host"""

    name: Required[str]
    """Name of the connection"""

    password: Required[str]
    """Database password"""

    username: Required[str]
    """Database username"""

    warehouse_type: Required[Literal["postgresql"]]
    """Warehouse type"""

    description: Optional[str]
    """Description of the connection"""

    label: Optional[str]
    """Human-readable label for the connection (defaults to name if not set)"""

    port: int
    """Database port"""


class SnowflakeConnectionConfig(TypedDict, total=False):
    account: Required[str]
    """Snowflake account identifier (e.g., 'xy12345.us-east-1')"""

    auth: Required[SnowflakeConnectionConfigAuth]
    """Authentication configuration"""

    databases: Required[Iterable[DatabaseConfigParam]]
    """Databases to include in the connection (at least one required)"""

    name: Required[str]
    """Name of the connection"""

    role: Required[str]
    """Snowflake role"""

    username: Required[str]
    """Snowflake username"""

    warehouse: Required[str]
    """Compute warehouse name"""

    warehouse_type: Required[Literal["snowflake"]]
    """Warehouse type"""

    description: Optional[str]
    """Description of the connection"""

    label: Optional[str]
    """Human-readable label for the connection (defaults to name if not set)"""


class SnowflakeConnectionConfigAuthSnowflakePasswordAuth(TypedDict, total=False):
    """Snowflake password authentication."""

    auth_type: Required[Literal["password"]]
    """Authentication type"""

    password: Required[str]
    """Snowflake password"""


class SnowflakeConnectionConfigAuthSnowflakePrivateKeyAuth(TypedDict, total=False):
    """Snowflake private key authentication."""

    auth_type: Required[Literal["private_key"]]
    """Authentication type"""

    private_key: Required[str]
    """PEM-encoded private key"""

    private_key_passphrase: Optional[str]
    """Passphrase if key is encrypted"""


SnowflakeConnectionConfigAuth: TypeAlias = Union[
    SnowflakeConnectionConfigAuthSnowflakePasswordAuth, SnowflakeConnectionConfigAuthSnowflakePrivateKeyAuth
]


class DatabricksConnectionConfig(TypedDict, total=False):
    access_token: Required[str]
    """Databricks personal access token"""

    databases: Required[Iterable[DatabaseConfigParam]]
    """Databases to include in the connection (at least one required)"""

    http_path: Required[str]
    """SQL warehouse HTTP path (e.g., '/sql/1.0/warehouses/xxx')"""

    name: Required[str]
    """Name of the connection"""

    server_hostname: Required[str]
    """Databricks server hostname (e.g., 'dbc-xxx.cloud.databricks.com')"""

    warehouse_type: Required[Literal["databricks"]]
    """Warehouse type"""

    description: Optional[str]
    """Description of the connection"""

    label: Optional[str]
    """Human-readable label for the connection (defaults to name if not set)"""


class ClickHouseConnectionConfig(TypedDict, total=False):
    databases: Required[Iterable[DatabaseConfigParam]]
    """Databases to include in the connection (at least one required)"""

    host: Required[str]
    """ClickHouse host"""

    name: Required[str]
    """Name of the connection"""

    password: Required[str]
    """ClickHouse password"""

    username: Required[str]
    """ClickHouse username"""

    warehouse_type: Required[Literal["clickhouse"]]
    """Warehouse type"""

    description: Optional[str]
    """Description of the connection"""

    label: Optional[str]
    """Human-readable label for the connection (defaults to name if not set)"""

    port: int
    """ClickHouse port"""


class MssqlConnectionConfig(TypedDict, total=False):
    databases: Required[Iterable[DatabaseConfigParam]]
    """Databases to include in the connection (at least one required)"""

    host: Required[str]
    """SQL Server host"""

    name: Required[str]
    """Name of the connection"""

    password: Required[str]
    """SQL Server password"""

    username: Required[str]
    """SQL Server username"""

    warehouse_type: Required[Literal["mssql"]]
    """Warehouse type"""

    description: Optional[str]
    """Description of the connection"""

    label: Optional[str]
    """Human-readable label for the connection (defaults to name if not set)"""

    port: int
    """SQL Server port"""


ConnectionCreateParams: TypeAlias = Union[
    PostgresConnectionConfig,
    SnowflakeConnectionConfig,
    DatabricksConnectionConfig,
    ClickHouseConnectionConfig,
    MssqlConnectionConfig,
]
