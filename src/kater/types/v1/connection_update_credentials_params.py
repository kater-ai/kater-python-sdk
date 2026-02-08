# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConnectionUpdateCredentialsParams",
    "PostgreSqlCredentialUpdate",
    "SnowflakeCredentialUpdate",
    "SnowflakeCredentialUpdateAuth",
    "SnowflakeCredentialUpdateAuthSnowflakePasswordCredentialAuth",
    "SnowflakeCredentialUpdateAuthSnowflakePrivateKeyCredentialAuth",
    "DatabricksCredentialUpdate",
    "ClickHouseCredentialUpdate",
    "MssqlCredentialUpdate",
]


class PostgreSqlCredentialUpdate(TypedDict, total=False):
    password: Required[str]
    """Database password"""

    username: Required[str]
    """Database username"""

    warehouse_type: Required[Literal["postgresql"]]
    """Warehouse type"""


class SnowflakeCredentialUpdate(TypedDict, total=False):
    auth: Required[SnowflakeCredentialUpdateAuth]
    """Authentication credentials"""

    username: Required[str]
    """Snowflake username"""

    warehouse_type: Required[Literal["snowflake"]]
    """Warehouse type"""


class SnowflakeCredentialUpdateAuthSnowflakePasswordCredentialAuth(TypedDict, total=False):
    """Snowflake password auth for credential update."""

    auth_type: Required[Literal["password"]]
    """Authentication type"""

    password: Required[str]
    """Snowflake password"""


class SnowflakeCredentialUpdateAuthSnowflakePrivateKeyCredentialAuth(TypedDict, total=False):
    """Snowflake private key auth for credential update."""

    auth_type: Required[Literal["private_key"]]
    """Authentication type"""

    private_key: Required[str]
    """PEM-encoded private key"""


SnowflakeCredentialUpdateAuth: TypeAlias = Union[
    SnowflakeCredentialUpdateAuthSnowflakePasswordCredentialAuth,
    SnowflakeCredentialUpdateAuthSnowflakePrivateKeyCredentialAuth,
]


class DatabricksCredentialUpdate(TypedDict, total=False):
    access_token: Required[str]
    """Databricks personal access token"""

    warehouse_type: Required[Literal["databricks"]]
    """Warehouse type"""


class ClickHouseCredentialUpdate(TypedDict, total=False):
    password: Required[str]
    """ClickHouse password"""

    username: Required[str]
    """ClickHouse username"""

    warehouse_type: Required[Literal["clickhouse"]]
    """Warehouse type"""


class MssqlCredentialUpdate(TypedDict, total=False):
    password: Required[str]
    """SQL Server password"""

    username: Required[str]
    """SQL Server username"""

    warehouse_type: Required[Literal["mssql"]]
    """Warehouse type"""


ConnectionUpdateCredentialsParams: TypeAlias = Union[
    PostgreSqlCredentialUpdate,
    SnowflakeCredentialUpdate,
    DatabricksCredentialUpdate,
    ClickHouseCredentialUpdate,
    MssqlCredentialUpdate,
]
