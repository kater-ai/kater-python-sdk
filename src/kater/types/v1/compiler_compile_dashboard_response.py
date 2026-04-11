# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = [
    "CompilerCompileDashboardResponse",
    "Context",
    "Dashboard",
    "FilterApplicability",
    "FilterApplicabilitySlot",
    "FilterDefinition",
    "FilterDefinitionDefaultValue",
    "FilterDefinitionDefaultValueScalarFilterValue",
    "FilterDefinitionDefaultValueMultiFilterValue",
    "FilterDefinitionDefaultValueNumberRangeFilterValue",
    "FilterDefinitionDefaultValueAbsoluteDateFilterValue",
    "FilterDefinitionDefaultValueAbsoluteRangeFilterValue",
    "FilterDefinitionDefaultValueRelativeRangeFilterValue",
    "FilterDefinitionDefaultValueRelativeRangeFilterValueEnd",
    "FilterDefinitionDefaultValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "FilterDefinitionDefaultValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "FilterDefinitionDefaultValueRelativeRangeFilterValueStart",
    "FilterDefinitionDefaultValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "FilterDefinitionDefaultValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "FilterDefinitionDefaultValuePresetReferenceFilterValue",
    "FilterDefinitionDefaultValueNullFilterValue",
    "FilterDefinitionPreset",
    "FilterDefinitionPresetValue",
    "FilterDefinitionPresetValueScalarFilterValue",
    "FilterDefinitionPresetValueMultiFilterValue",
    "FilterDefinitionPresetValueNumberRangeFilterValue",
    "FilterDefinitionPresetValueAbsoluteDateFilterValue",
    "FilterDefinitionPresetValueAbsoluteRangeFilterValue",
    "FilterDefinitionPresetValueRelativeRangeFilterValue",
    "FilterDefinitionPresetValueRelativeRangeFilterValueEnd",
    "FilterDefinitionPresetValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "FilterDefinitionPresetValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "FilterDefinitionPresetValueRelativeRangeFilterValueStart",
    "FilterDefinitionPresetValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "FilterDefinitionPresetValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "FilterDefinitionPresetValuePresetReferenceFilterValue",
    "FilterDefinitionPresetValueNullFilterValue",
    "FilterDefinitionStaticValue",
    "FilterDefinitionStaticValueNumberRangeFilterValue",
    "FilterDefinitionStaticValueAbsoluteDateFilterValue",
    "FilterDefinitionStaticValueAbsoluteRangeFilterValue",
    "FilterDefinitionStaticValueRelativeRangeFilterValue",
    "FilterDefinitionStaticValueRelativeRangeFilterValueEnd",
    "FilterDefinitionStaticValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "FilterDefinitionStaticValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "FilterDefinitionStaticValueRelativeRangeFilterValueStart",
    "FilterDefinitionStaticValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "FilterDefinitionStaticValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "FilterDefinitionValues",
    "FilterDefinitionValuesStaticFilterValuesSource",
    "FilterDefinitionValuesStaticFilterValuesSourceItem",
    "FilterDefinitionValuesDynamicDistinctFilterValuesSource",
    "FilterState",
    "FilterStateValue",
    "FilterStateValueScalarFilterValue",
    "FilterStateValueMultiFilterValue",
    "FilterStateValueNumberRangeFilterValue",
    "FilterStateValueAbsoluteDateFilterValue",
    "FilterStateValueAbsoluteRangeFilterValue",
    "FilterStateValueRelativeRangeFilterValue",
    "FilterStateValueRelativeRangeFilterValueEnd",
    "FilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "FilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "FilterStateValueRelativeRangeFilterValueStart",
    "FilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "FilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "FilterStateValuePresetReferenceFilterValue",
    "FilterStateValueNullFilterValue",
    "Widget",
    "WidgetColumnMapUnionMember0",
    "WidgetColumnMapUnionMember1",
    "WidgetGrid",
    "WidgetColumnProfilesUnionMember0WidgetColumnProfilesUnionMember0Item",
    "WidgetColumnProfilesUnionMember1WidgetColumnProfilesUnionMember1Item",
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


class FilterApplicabilitySlot(BaseModel):
    """One dashboard slot that a shared filter applies to."""

    effective_kater_id: str
    """Slot-scoped effective runtime filter ID for this query context"""

    query_kater_id: str
    """UUID of the slot query"""

    query_name: str
    """Logical slot query name"""

    slot_name: str
    """Dashboard data-slot name"""


class FilterApplicability(BaseModel):
    """Per-filter mapping from dashboard-shared state to slot query contexts."""

    effective_kater_id: str
    """Dashboard-level effective runtime filter ID"""

    name: str
    """Logical shared filter name"""

    slots: Optional[List[FilterApplicabilitySlot]] = None
    """Slots and slot-scoped effective IDs that this shared filter applies to"""


class FilterDefinitionDefaultValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

    mode: Optional[Literal["scalar"]] = None


class FilterDefinitionDefaultValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class FilterDefinitionDefaultValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class FilterDefinitionDefaultValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class FilterDefinitionDefaultValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class FilterDefinitionDefaultValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterDefinitionDefaultValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterDefinitionDefaultValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    FilterDefinitionDefaultValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    FilterDefinitionDefaultValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class FilterDefinitionDefaultValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterDefinitionDefaultValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterDefinitionDefaultValueRelativeRangeFilterValueStart: TypeAlias = Union[
    FilterDefinitionDefaultValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    FilterDefinitionDefaultValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class FilterDefinitionDefaultValueRelativeRangeFilterValue(BaseModel):
    end: FilterDefinitionDefaultValueRelativeRangeFilterValueEnd

    start: FilterDefinitionDefaultValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class FilterDefinitionDefaultValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class FilterDefinitionDefaultValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


FilterDefinitionDefaultValue: TypeAlias = Union[
    FilterDefinitionDefaultValueScalarFilterValue,
    FilterDefinitionDefaultValueMultiFilterValue,
    FilterDefinitionDefaultValueNumberRangeFilterValue,
    FilterDefinitionDefaultValueAbsoluteDateFilterValue,
    FilterDefinitionDefaultValueAbsoluteRangeFilterValue,
    FilterDefinitionDefaultValueRelativeRangeFilterValue,
    FilterDefinitionDefaultValuePresetReferenceFilterValue,
    FilterDefinitionDefaultValueNullFilterValue,
    None,
]


class FilterDefinitionPresetValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

    mode: Optional[Literal["scalar"]] = None


class FilterDefinitionPresetValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class FilterDefinitionPresetValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class FilterDefinitionPresetValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class FilterDefinitionPresetValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class FilterDefinitionPresetValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterDefinitionPresetValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterDefinitionPresetValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    FilterDefinitionPresetValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    FilterDefinitionPresetValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class FilterDefinitionPresetValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterDefinitionPresetValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterDefinitionPresetValueRelativeRangeFilterValueStart: TypeAlias = Union[
    FilterDefinitionPresetValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    FilterDefinitionPresetValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class FilterDefinitionPresetValueRelativeRangeFilterValue(BaseModel):
    end: FilterDefinitionPresetValueRelativeRangeFilterValueEnd

    start: FilterDefinitionPresetValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class FilterDefinitionPresetValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class FilterDefinitionPresetValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


FilterDefinitionPresetValue: TypeAlias = Union[
    FilterDefinitionPresetValueScalarFilterValue,
    FilterDefinitionPresetValueMultiFilterValue,
    FilterDefinitionPresetValueNumberRangeFilterValue,
    FilterDefinitionPresetValueAbsoluteDateFilterValue,
    FilterDefinitionPresetValueAbsoluteRangeFilterValue,
    FilterDefinitionPresetValueRelativeRangeFilterValue,
    FilterDefinitionPresetValuePresetReferenceFilterValue,
    FilterDefinitionPresetValueNullFilterValue,
]


class FilterDefinitionPreset(BaseModel):
    label: str
    """Human-readable preset label"""

    name: str
    """Stable preset key"""

    value: FilterDefinitionPresetValue
    """Typed preset value payload"""


class FilterDefinitionStaticValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class FilterDefinitionStaticValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class FilterDefinitionStaticValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class FilterDefinitionStaticValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterDefinitionStaticValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterDefinitionStaticValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    FilterDefinitionStaticValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    FilterDefinitionStaticValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class FilterDefinitionStaticValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterDefinitionStaticValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterDefinitionStaticValueRelativeRangeFilterValueStart: TypeAlias = Union[
    FilterDefinitionStaticValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    FilterDefinitionStaticValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class FilterDefinitionStaticValueRelativeRangeFilterValue(BaseModel):
    end: FilterDefinitionStaticValueRelativeRangeFilterValueEnd

    start: FilterDefinitionStaticValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


FilterDefinitionStaticValue: TypeAlias = Union[
    str,
    float,
    bool,
    List[Union[str, float, bool]],
    FilterDefinitionStaticValueNumberRangeFilterValue,
    FilterDefinitionStaticValueAbsoluteDateFilterValue,
    FilterDefinitionStaticValueAbsoluteRangeFilterValue,
    FilterDefinitionStaticValueRelativeRangeFilterValue,
    None,
]


class FilterDefinitionValuesStaticFilterValuesSourceItem(BaseModel):
    value: Union[str, float, bool]
    """Selectable scalar value"""

    label: Optional[str] = None
    """Optional selectable value label"""


class FilterDefinitionValuesStaticFilterValuesSource(BaseModel):
    items: List[FilterDefinitionValuesStaticFilterValuesSourceItem]
    """Inline selectable items"""

    source: Optional[Literal["static"]] = None


class FilterDefinitionValuesDynamicDistinctFilterValuesSource(BaseModel):
    limit: Optional[int] = None
    """Maximum number of values to request"""

    sort: Optional[Literal["asc", "desc"]] = None
    """Supported sort order for dynamic distinct value loading"""

    source: Optional[Literal["dynamic_distinct"]] = None


FilterDefinitionValues: TypeAlias = Union[
    FilterDefinitionValuesStaticFilterValuesSource, FilterDefinitionValuesDynamicDistinctFilterValuesSource, None
]


class FilterDefinition(BaseModel):
    """Resolved effective filter definition exposed by the V2 API contract."""

    data_type: str
    """Canonical data type"""

    effective_kater_id: str
    """Stable effective runtime filter ID"""

    expression: str
    """Structured filter expression"""

    field: str
    """Target field ref"""

    kater_id: str
    """Concrete declaration ID from the merged definition"""

    mode: str
    """Filter mode: static or parameterized"""

    name: str
    """Logical filter name"""

    required: bool
    """Whether the filter is always active"""

    scope: str
    """Filter scope: model, topic, dashboard, or query"""

    ai_context: Optional[str] = None
    """AI-facing filter context"""

    allow_null_value: Optional[bool] = None
    """Whether null is allowed"""

    declaration_kater_ids: Optional[List[str]] = None
    """Concrete declaration IDs that contributed to this effective filter"""

    default_enabled: Optional[bool] = None
    """Default enabled state"""

    default_value: Optional[FilterDefinitionDefaultValue] = None
    """Default runtime value payload"""

    description: Optional[str] = None
    """Filter description"""

    help_text: Optional[str] = None
    """Optional UI help text"""

    kind: Optional[str] = None
    """Interactive filter kind"""

    label: Optional[str] = None
    """Human-readable filter label"""

    null_label: Optional[str] = None
    """Null option label"""

    owner_chain: Optional[List[str]] = None
    """Owner IDs from model/topic/dashboard/query precedence order"""

    placeholder: Optional[str] = None
    """Optional input placeholder"""

    presets: Optional[List[FilterDefinitionPreset]] = None
    """Filter preset definitions"""

    static_value: Optional[FilterDefinitionStaticValue] = None
    """Static filter value payload"""

    values: Optional[FilterDefinitionValues] = None
    """Selectable values metadata"""


class FilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

    mode: Optional[Literal["scalar"]] = None


class FilterStateValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class FilterStateValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class FilterStateValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class FilterStateValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class FilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    FilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    FilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class FilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class FilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


FilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    FilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    FilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class FilterStateValueRelativeRangeFilterValue(BaseModel):
    end: FilterStateValueRelativeRangeFilterValueEnd

    start: FilterStateValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class FilterStateValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class FilterStateValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


FilterStateValue: TypeAlias = Union[
    FilterStateValueScalarFilterValue,
    FilterStateValueMultiFilterValue,
    FilterStateValueNumberRangeFilterValue,
    FilterStateValueAbsoluteDateFilterValue,
    FilterStateValueAbsoluteRangeFilterValue,
    FilterStateValueRelativeRangeFilterValue,
    FilterStateValuePresetReferenceFilterValue,
    FilterStateValueNullFilterValue,
    None,
]


class FilterState(BaseModel):
    """Resolved runtime filter state exposed by the V2 API contract."""

    effective_kater_id: str
    """Stable effective runtime filter ID"""

    enabled: bool
    """Whether the filter is enabled at runtime"""

    name: str
    """Logical filter name"""

    required: bool
    """Whether the filter is required"""

    kind: Optional[str] = None
    """Interactive filter kind"""

    label: Optional[str] = None
    """Human-readable filter label"""

    value: Optional[FilterStateValue] = None
    """Current typed runtime value"""


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


class WidgetColumnProfilesUnionMember0WidgetColumnProfilesUnionMember0Item(BaseModel):
    """Statistical profile for a single result column."""

    cardinality: Optional[int] = None
    """Distinct non-null values for dimension columns.

    Null for measures and calculations.
    """

    cv: Optional[float] = None
    """Coefficient of variation (|stdev / mean|)."""

    has_outliers: Optional[bool] = None
    """True if any value lies outside [q1 - 1.5*IQR, q3 + 1.5*IQR]."""

    iqr: Optional[float] = None
    """Interquartile range (q3 - q1)."""

    max: Optional[float] = None
    """Maximum numeric value."""

    mean: Optional[float] = None
    """Arithmetic mean."""

    min: Optional[float] = None
    """Minimum numeric value. Null when the column has no numeric data."""

    null_count: Optional[int] = None
    """Number of null values in the column."""

    null_pct: Optional[float] = None
    """Fraction of null values (0.0-1.0)."""

    q1: Optional[float] = None
    """First quartile (25th percentile)."""

    q3: Optional[float] = None
    """Third quartile (75th percentile)."""

    stdev: Optional[float] = None
    """Population standard deviation."""


class WidgetColumnProfilesUnionMember1WidgetColumnProfilesUnionMember1Item(BaseModel):
    """Statistical profile for a single result column."""

    cardinality: Optional[int] = None
    """Distinct non-null values for dimension columns.

    Null for measures and calculations.
    """

    cv: Optional[float] = None
    """Coefficient of variation (|stdev / mean|)."""

    has_outliers: Optional[bool] = None
    """True if any value lies outside [q1 - 1.5*IQR, q3 + 1.5*IQR]."""

    iqr: Optional[float] = None
    """Interquartile range (q3 - q1)."""

    max: Optional[float] = None
    """Maximum numeric value."""

    mean: Optional[float] = None
    """Arithmetic mean."""

    min: Optional[float] = None
    """Minimum numeric value. Null when the column has no numeric data."""

    null_count: Optional[int] = None
    """Number of null values in the column."""

    null_pct: Optional[float] = None
    """Fraction of null values (0.0-1.0)."""

    q1: Optional[float] = None
    """First quartile (25th percentile)."""

    q3: Optional[float] = None
    """Third quartile (75th percentile)."""

    stdev: Optional[float] = None
    """Population standard deviation."""


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

    column_profiles: Union[
        Dict[str, WidgetColumnProfilesUnionMember0WidgetColumnProfilesUnionMember0Item],
        List[Dict[str, WidgetColumnProfilesUnionMember1WidgetColumnProfilesUnionMember1Item]],
        None,
    ] = None
    """Per-column profiles keyed by kater_id.

    dict for single-query widgets, list of dicts for multi-query widgets (aligned
    with column_map). Null when no slot was resolved.
    """

    display_mode: Optional[str] = None
    """Display mode for multi-query: 'tabs' or 'grid'"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Per-widget compilation errors"""

    row_count: Union[int, List[int], None] = None
    """Total rows represented by the widget result (single or multi-query)"""

    slot_configs: Optional[List[Dict[str, object]]] = None
    """Per-slot configs for multi-query containers"""

    totals_row: Union[Dict[str, object], List[Optional[Dict[str, object]]], None] = None
    """Totals row (single-query: dict | None; multi-query: list aligned with data)"""

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

    filter_applicability: Optional[List[FilterApplicability]] = None
    """Slot applicability metadata for each shared dashboard filter"""

    filter_definitions: Optional[List[FilterDefinition]] = None
    """Shared dashboard filter definitions"""

    filter_state: Optional[List[FilterState]] = None
    """Applied dashboard filter state after defaults and runtime overrides"""

    widgets: Optional[List[Widget]] = None
    """Fully resolved widgets with data + config"""
