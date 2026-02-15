# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = ["CompilerExecuteResponse", "ColumnMap", "Metadata"]


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


class CompilerExecuteResponse(BaseModel):
    """Response model for query execution."""

    dialect: str
    """SQL dialect used"""

    success: bool
    """Whether execution succeeded"""

    cache_hit: Optional[bool] = None
    """Whether the result was served from cache"""

    column_map: Optional[List[ColumnMap]] = None
    """Maps UUID column aliases to human-readable names"""

    data: Optional[List[Dict[str, object]]] = None
    """Query result rows as list of column-value dicts"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Compilation errors (if any)"""

    execution_time_ms: Optional[float] = None
    """Total execution time in milliseconds"""

    metadata: Optional[Metadata] = None
    """Compilation metadata from the compiler."""

    row_count: Optional[int] = None
    """Number of rows returned"""

    sql: Optional[str] = None
    """Generated SQL statement"""
