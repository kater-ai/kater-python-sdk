# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ConnectionRetrieveCredentialResponse",
    "PostgresCredentialResponse",
    "SnowflakeCredentialResponse",
    "SnowflakeCredentialResponseAuth",
    "SnowflakeCredentialResponseAuthSnowflakePasswordAuthResponse",
    "SnowflakeCredentialResponseAuthSnowflakePrivateKeyAuthResponse",
    "DatabricksCredentialResponse",
    "ClickHouseCredentialResponse",
    "MssqlCredentialResponse",
]


class PostgresCredentialResponse(BaseModel):
    """PostgreSQL credential response."""

    database: str
    """Database name"""

    host: str
    """Database host"""

    password: str
    """Decrypted password"""

    port: int
    """Database port"""

    username: str
    """Database username"""

    warehouse_type: Literal["postgresql"]
    """Warehouse type"""


class SnowflakeCredentialResponseAuthSnowflakePasswordAuthResponse(BaseModel):
    """Snowflake password authentication response."""

    auth_type: Literal["password"]
    """Authentication type"""

    password: str
    """Decrypted password"""


class SnowflakeCredentialResponseAuthSnowflakePrivateKeyAuthResponse(BaseModel):
    """Snowflake private key authentication response."""

    auth_type: Literal["private_key"]
    """Authentication type"""

    private_key: str
    """PEM-encoded private key"""

    private_key_passphrase: Optional[str] = None
    """Passphrase if key is encrypted"""


SnowflakeCredentialResponseAuth: TypeAlias = Annotated[
    Union[
        SnowflakeCredentialResponseAuthSnowflakePasswordAuthResponse,
        SnowflakeCredentialResponseAuthSnowflakePrivateKeyAuthResponse,
    ],
    PropertyInfo(discriminator="auth_type"),
]


class SnowflakeCredentialResponse(BaseModel):
    """Snowflake credential response."""

    account: str
    """Snowflake account identifier"""

    auth: SnowflakeCredentialResponseAuth
    """Authentication credentials"""

    role: str
    """Snowflake role"""

    username: str
    """Snowflake username"""

    warehouse: str
    """Compute warehouse name"""

    warehouse_type: Literal["snowflake"]
    """Warehouse type"""


class DatabricksCredentialResponse(BaseModel):
    """Databricks credential response."""

    access_token: str
    """Databricks personal access token"""

    http_path: str
    """SQL warehouse HTTP path"""

    server_hostname: str
    """Databricks server hostname"""

    warehouse_type: Literal["databricks"]
    """Warehouse type"""


class ClickHouseCredentialResponse(BaseModel):
    """ClickHouse credential response."""

    host: str
    """ClickHouse host"""

    password: str
    """Decrypted password"""

    port: int
    """ClickHouse port"""

    username: str
    """ClickHouse username"""

    warehouse_type: Literal["clickhouse"]
    """Warehouse type"""

    database: Optional[str] = None
    """Database name"""


class MssqlCredentialResponse(BaseModel):
    """Microsoft SQL Server credential response."""

    host: str
    """SQL Server host"""

    password: str
    """Decrypted password"""

    port: int
    """SQL Server port"""

    username: str
    """SQL Server username"""

    warehouse_type: Literal["mssql"]
    """Warehouse type"""

    database: Optional[str] = None
    """Database name"""


ConnectionRetrieveCredentialResponse: TypeAlias = Annotated[
    Union[
        PostgresCredentialResponse,
        SnowflakeCredentialResponse,
        DatabricksCredentialResponse,
        ClickHouseCredentialResponse,
        MssqlCredentialResponse,
    ],
    PropertyInfo(discriminator="warehouse_type"),
]
