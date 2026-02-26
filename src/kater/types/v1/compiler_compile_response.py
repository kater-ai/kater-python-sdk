# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .manifest import Manifest
from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = ["CompilerCompileResponse", "ColumnMap", "Metadata"]


class ColumnMap(BaseModel):
    """Maps a UUID column alias to its human-readable name and type."""

    field_type: str
    """Field type: dimension, measure, or calculation"""

    kater_id: str
    """UUID string used as SQL column alias"""

    name: str
    """Human-readable column name"""

    aggregation: Optional[str] = None
    """Aggregation type for measures: sum, count, min, max, avg, unknown.

    None for non-measures.
    """

    label: Optional[str] = None
    """Display label"""


class Metadata(BaseModel):
    """Compilation metadata from the compiler."""

    dialect: str
    """SQL dialect used (e.g. 'snowflake')"""

    query_ref: str
    """Reference to the compiled query"""

    dimensions_used: Optional[List[str]] = None
    """Dimension names used in compilation"""

    filters_used: Optional[List[str]] = None
    """Filter names used in compilation"""

    measures_used: Optional[List[str]] = None
    """Measure names used in compilation"""

    views_used: Optional[List[str]] = None
    """View names used in compilation"""


class CompilerCompileResponse(BaseModel):
    """Response model for SQL compilation."""

    dialect: str
    """SQL dialect used (e.g. 'snowflake')"""

    success: bool
    """Whether compilation succeeded"""

    column_map: Optional[List[ColumnMap]] = None
    """Maps UUID column aliases to human-readable names and types"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Compilation errors"""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""

    metadata: Optional[Metadata] = None
    """Compilation metadata from the compiler."""

    request_id: Optional[str] = None
    """Write-back request ID.

    Non-null when files were dispatched to CLI via WebSocket.
    """

    sql: Optional[str] = None
    """Generated SQL statement"""
