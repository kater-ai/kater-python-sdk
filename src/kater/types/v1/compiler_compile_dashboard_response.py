# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = [
    "CompilerCompileDashboardResponse",
    "Context",
    "Dashboard",
    "Filter",
    "Widget",
    "WidgetColumnMapUnionMember0",
    "WidgetColumnMapUnionMember1",
    "WidgetGrid",
]


class Context(BaseModel):
    """Dashboard context for widgets"""

    filters: Optional[Dict[str, Dict[str, object]]] = None
    """Active filter values: {name: {value, label}}"""

    timeframe: Optional[Dict[str, str]] = None
    """Active timeframe: {label, start, end}"""

    topic: Optional[Dict[str, str]] = None
    """Dashboard topic: {label, time_dimension}"""


class Dashboard(BaseModel):
    """Dashboard metadata"""

    name: str
    """Dashboard name"""

    description: Optional[str] = None
    """Dashboard description"""

    kater_id: Optional[str] = None
    """Dashboard kater_id"""

    label: Optional[str] = None
    """Dashboard display label"""

    topic: Optional[str] = None
    """Dashboard topic reference"""


class Filter(BaseModel):
    """A resolved dashboard filter with current value and presets."""

    filter_type: str
    """Filter type: date_range, multi_select, select"""

    name: str
    """Filter name"""

    allow_null: Optional[bool] = None
    """Whether null (All) is allowed"""

    auto_apply: Optional[bool] = None
    """Whether filter auto-applies to queries"""

    current_value: Union[str, List[str], None] = None
    """Current filter value"""

    default: Optional[Dict[str, str]] = None
    """Default value specification"""

    field: Optional[str] = None
    """Field reference for data-driven filters"""

    null_label: Optional[str] = None
    """Label for null/All option"""

    presets: Optional[List[Dict[str, str]]] = None
    """Available presets"""


class WidgetColumnMapUnionMember0(BaseModel):
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


class WidgetColumnMapUnionMember1(BaseModel):
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


class WidgetGrid(BaseModel):
    """Grid position"""

    h: Optional[int] = None

    w: Optional[int] = None

    x: Optional[int] = None

    y: Optional[int] = None


class Widget(BaseModel):
    """A fully resolved widget ready for rendering."""

    column_map: Union[List[WidgetColumnMapUnionMember0], List[List[WidgetColumnMapUnionMember1]]]
    """Column metadata (single or multi-query)"""

    config: Dict[str, object]
    """Fully resolved WidgetConfig"""

    data: Union[List[Dict[str, object]], List[List[Dict[str, object]]]]
    """Query result data (single or multi-query)"""

    grid: WidgetGrid
    """Grid position"""

    kater_id: str
    """Widget unique identifier"""

    name: str
    """Widget name"""

    display_mode: Optional[str] = None
    """Display mode for multi-query: 'tabs' or 'grid'"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Per-widget compilation errors"""

    slot_configs: Optional[List[Dict[str, object]]] = None
    """Per-slot configs for multi-query containers"""

    widget_type: Optional[str] = None
    """Resolved widget type"""


class CompilerCompileDashboardResponse(BaseModel):
    """Response from dashboard compilation — fully resolved dashboard."""

    context: Context
    """Dashboard context for widgets"""

    dashboard: Dashboard
    """Dashboard metadata"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Dashboard-level compilation errors"""

    filters: Optional[List[Filter]] = None
    """Resolved filter definitions with current values"""

    widgets: Optional[List[Widget]] = None
    """Fully resolved widgets with data + config"""
