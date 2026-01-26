# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Connection", "Database", "DatabaseSchema"]


class DatabaseSchema(BaseModel):
    """Schema info from ConnectionSchema."""

    id: str
    """Schema ID"""

    description: Optional[str] = None
    """Schema description"""

    label: Optional[str] = None
    """Human-readable label"""

    name: str
    """Schema name"""


class Database(BaseModel):
    """Database info from ConnectionSchema."""

    id: str
    """Database ID"""

    description: Optional[str] = None
    """Database description"""

    label: Optional[str] = None
    """Human-readable label"""

    name: str
    """Database name"""

    schemas: List[DatabaseSchema]
    """Schemas in this database"""

    timezone: Optional[str] = None
    """Timezone for the database"""


class Connection(BaseModel):
    """Response model for a single connection.

    All data comes from the database (source of truth).
    The id field serves as the kater_id.
    """

    id: str
    """Connection ID (also the kater_id)"""

    created_at: datetime
    """Creation timestamp"""

    credential_id: str
    """Credential ID"""

    databases: List[Database]
    """Databases in this connection"""

    description: Optional[str] = None
    """Connection description"""

    label: Optional[str] = None
    """Human-readable label"""

    name: str
    """Connection name"""

    updated_at: datetime
    """Last update timestamp"""

    account: Optional[str] = None
    """Snowflake account identifier"""

    host: Optional[str] = None
    """Database host (PostgreSQL, MSSQL, ClickHouse)"""

    http_path: Optional[str] = None
    """Databricks HTTP path"""

    port: Optional[int] = None
    """Database port (PostgreSQL, MSSQL, ClickHouse)"""

    role: Optional[str] = None
    """Snowflake role"""

    server_hostname: Optional[str] = None
    """Databricks server hostname"""

    warehouse: Optional[str] = None
    """Snowflake or Databricks warehouse name"""
