# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel
from ..compiler_error_item import CompilerErrorItem

__all__ = ["CombinationPreviewResponse", "ColumnMap"]


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


class CombinationPreviewResponse(BaseModel):
    """Response from combination preview with data + resolved config."""

    success: bool
    """Whether preview succeeded"""

    auto_title: Optional[str] = None
    """Auto-generated title"""

    cache_hit: Optional[bool] = None
    """Whether the result was served from cache"""

    column_map: Optional[List[ColumnMap]] = None
    """Enriched column metadata"""

    config: Optional[Dict[str, object]] = None
    """Resolved WidgetConfig (from config builder)"""

    data: Optional[List[Dict[str, object]]] = None
    """Query result rows"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Compilation errors (if any)"""

    execution_time_ms: Optional[float] = None
    """Total execution time in milliseconds"""

    widget_type: Optional[str] = None
    """Resolved widget type (e.g. 'axis_metric_by_dimensiondate')"""
