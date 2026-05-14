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
    "InsightRun",
    "InsightRunContext",
    "InsightRunContextExecution",
    "InsightRunContextInsight",
    "InsightRunContextHost",
    "InsightRunContextInput",
    "InsightRunContextInputQuery",
    "InsightRunFinding",
    "InsightRunFindingEvidence",
    "InsightRunFindingFollowUp",
    "InsightRunSummary",
    "Widget",
    "WidgetColumnMapUnionMember0",
    "WidgetColumnMapUnionMember0DataType",
    "WidgetColumnMapUnionMember0DataTypeExtension",
    "WidgetColumnMapUnionMember1",
    "WidgetColumnMapUnionMember1DataType",
    "WidgetColumnMapUnionMember1DataTypeExtension",
    "WidgetGrid",
    "WidgetColumnProfilesUnionMember0WidgetColumnProfilesUnionMember0Item",
    "WidgetColumnProfilesUnionMember1WidgetColumnProfilesUnionMember1Item",
    "WidgetDependencies",
    "WidgetDependenciesSlot",
    "WidgetDependenciesSlotTimeframeOverride",
    "WidgetDependenciesSlotVariableValue",
    "WidgetRenderedQueryKey",
    "WidgetRenderedQueryKeyCanonical",
    "WidgetRenderedQueryKeyCanonicalCacheProjection",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionAggregate",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateDimension",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateFilter",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateMeasure",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateVariable",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionExact",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionExactFilter",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionExactOutputColumn",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionExactResultWindow",
    "WidgetRenderedQueryKeyCanonicalCacheProjectionExactVariable",
    "WidgetRenderedQueryKeyCanonicalContract",
    "WidgetRenderedQueryKeyCanonicalDashboard",
    "WidgetRenderedQueryKeyCanonicalDashboardDashboardFilterState",
    "WidgetRenderedQueryKeyCanonicalFields",
    "WidgetRenderedQueryKeyCanonicalFieldsActiveField",
    "WidgetRenderedQueryKeyCanonicalFieldsOutputColumn",
    "WidgetRenderedQueryKeyCanonicalFieldsSelectedField",
    "WidgetRenderedQueryKeyCanonicalFilters",
    "WidgetRenderedQueryKeyCanonicalFiltersEffectiveFilter",
    "WidgetRenderedQueryKeyCanonicalPresentation",
    "WidgetRenderedQueryKeyCanonicalQuery",
    "WidgetRenderedQueryKeyCanonicalResultWindow",
    "WidgetRenderedQueryKeyCanonicalSource",
    "WidgetRenderedQueryKeyCanonicalTemporal",
    "WidgetRenderedQueryKeyCanonicalTenant",
    "WidgetRenderedQueryKeyCanonicalVariable",
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
    """Scalar value compatible with Filter V2 runtime payloads"""

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
    """Scalar value compatible with Filter V2 runtime payloads"""

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
    """Scalar value compatible with Filter V2 runtime payloads"""

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

    filter_type: Optional[str] = None
    """Interactive filter control type"""

    help_text: Optional[str] = None
    """Optional UI help text"""

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
    """Scalar value compatible with Filter V2 runtime payloads"""

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

    filter_type: Optional[str] = None
    """Interactive filter control type"""

    label: Optional[str] = None
    """Human-readable filter label"""

    value: Optional[FilterStateValue] = None
    """Current typed runtime value"""


class InsightRunContextExecution(BaseModel):
    """Execution metadata captured for a completed insight run."""

    kater_id: str

    surface: Literal["dashboard", "preview", "chat"]

    params: Optional[Dict[str, object]] = None


class InsightRunContextInsight(BaseModel):
    """Insight definition metadata attached to a run result."""

    entrypoint: str

    kater_id: str

    name: str

    description: Optional[str] = None


class InsightRunContextHost(BaseModel):
    """Host surface metadata for the container that triggered the run."""

    dashboard_kater_id: Optional[str] = None

    dashboard_name: Optional[str] = None

    query_kater_id: Optional[str] = None

    query_name: Optional[str] = None

    widget_kater_id: Optional[str] = None


class InsightRunContextInputQuery(BaseModel):
    """Query metadata describing the source of an insight input."""

    description: Optional[str] = None

    kater_id: Optional[str] = None

    name: Optional[str] = None

    rendered_query_key: Optional[str] = None


class InsightRunContextInput(BaseModel):
    """Normalized input metadata attached to an insight run."""

    dataset_name: str

    input_name: str

    row_count: int

    bindings: Optional[Dict[str, str]] = None

    query: Optional[InsightRunContextInputQuery] = None
    """Query metadata describing the source of an insight input."""


class InsightRunContext(BaseModel):
    """Typed execution context attached to an insight run result."""

    execution: InsightRunContextExecution
    """Execution metadata captured for a completed insight run."""

    insight: InsightRunContextInsight
    """Insight definition metadata attached to a run result."""

    host: Optional[InsightRunContextHost] = None
    """Host surface metadata for the container that triggered the run."""

    inputs: Optional[List[InsightRunContextInput]] = None


class InsightRunFindingEvidence(BaseModel):
    """Structured evidence attached to a finding."""

    label: str

    value: Union[str, float, bool]

    description: Optional[str] = None


class InsightRunFindingFollowUp(BaseModel):
    """Structured action hint emitted by an insight finding."""

    id: str

    instructions: str

    label: str

    payload: Optional[Dict[str, object]] = None


class InsightRunFinding(BaseModel):
    """Single analytical finding emitted by an insight run."""

    kind: str

    summary: str

    confidence: Optional[float] = None

    details: Optional[List[str]] = None

    evidence: Optional[List[InsightRunFindingEvidence]] = None

    follow_ups: Optional[List[InsightRunFindingFollowUp]] = None

    metadata: Optional[Dict[str, object]] = None

    severity: Optional[Literal["info", "positive", "warning", "critical"]] = None


class InsightRunSummary(BaseModel):
    """Top-level summary for an insight run."""

    text: str

    confidence: Optional[float] = None

    severity: Optional[Literal["info", "positive", "warning", "critical"]] = None


class InsightRun(BaseModel):
    """Validated structured output for a completed insight run."""

    context: Optional[InsightRunContext] = None
    """Typed execution context attached to an insight run result."""

    findings: Optional[List[InsightRunFinding]] = None

    metadata: Optional[Dict[str, object]] = None

    summary: Optional[InsightRunSummary] = None
    """Top-level summary for an insight run."""


class WidgetColumnMapUnionMember0DataTypeExtension(BaseModel):
    """Vendor-specific type extension"""

    engine: str
    """Database engine/dialect"""

    orig_type: str
    """Original type name in the source database"""

    options: Optional[Dict[str, object]] = None
    """Additional vendor-specific options"""

    raw_ddl: Optional[str] = None
    """Raw DDL for the type"""


class WidgetColumnMapUnionMember0DataType(BaseModel):
    """Canonical data type metadata for this output column"""

    kind: Literal["Bool", "Text", "Number", "Datetime", "Complex", "Unknown"]
    """The canonical data type kind"""

    nullable: bool
    """Whether the field can be null"""

    extension: Optional[WidgetColumnMapUnionMember0DataTypeExtension] = None
    """Vendor-specific type extension"""

    params: Optional[object] = None
    """Optional coarse metadata for the canonical type"""


class WidgetColumnMapUnionMember0(BaseModel):
    """Maps a UUID column alias to its human-readable name and type."""

    data_type: WidgetColumnMapUnionMember0DataType
    """Canonical data type metadata for this output column"""

    field_type: str
    """Field type: dimension, measure, or calculation"""

    kater_id: str
    """Authored source field UUID"""

    name: str
    """Human-readable column name"""

    active_timeframe: Optional[str] = None
    """Concrete active timeframe for temporal dimensions, e.g. raw, month, quarter."""

    aggregation: Optional[str] = None
    """Aggregation type for measures: sum, count, min, max, avg, unknown.

    None for non-measures.
    """

    column_key: Optional[str] = None
    """SQL result alias for this concrete output column."""

    label: Optional[str] = None
    """Display label"""

    source_kater_id: Optional[str] = None
    """Authored source field UUID for derived timeframe columns."""


class WidgetColumnMapUnionMember1DataTypeExtension(BaseModel):
    """Vendor-specific type extension"""

    engine: str
    """Database engine/dialect"""

    orig_type: str
    """Original type name in the source database"""

    options: Optional[Dict[str, object]] = None
    """Additional vendor-specific options"""

    raw_ddl: Optional[str] = None
    """Raw DDL for the type"""


class WidgetColumnMapUnionMember1DataType(BaseModel):
    """Canonical data type metadata for this output column"""

    kind: Literal["Bool", "Text", "Number", "Datetime", "Complex", "Unknown"]
    """The canonical data type kind"""

    nullable: bool
    """Whether the field can be null"""

    extension: Optional[WidgetColumnMapUnionMember1DataTypeExtension] = None
    """Vendor-specific type extension"""

    params: Optional[object] = None
    """Optional coarse metadata for the canonical type"""


class WidgetColumnMapUnionMember1(BaseModel):
    """Maps a UUID column alias to its human-readable name and type."""

    data_type: WidgetColumnMapUnionMember1DataType
    """Canonical data type metadata for this output column"""

    field_type: str
    """Field type: dimension, measure, or calculation"""

    kater_id: str
    """Authored source field UUID"""

    name: str
    """Human-readable column name"""

    active_timeframe: Optional[str] = None
    """Concrete active timeframe for temporal dimensions, e.g. raw, month, quarter."""

    aggregation: Optional[str] = None
    """Aggregation type for measures: sum, count, min, max, avg, unknown.

    None for non-measures.
    """

    column_key: Optional[str] = None
    """SQL result alias for this concrete output column."""

    label: Optional[str] = None
    """Display label"""

    source_kater_id: Optional[str] = None
    """Authored source field UUID for derived timeframe columns."""


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


class WidgetDependenciesSlotTimeframeOverride(BaseModel):
    """Runtime grain choice for a temporal source dimension."""

    active_timeframe: str

    source_kater_id: str


class WidgetDependenciesSlotVariableValue(BaseModel):
    """Runtime variable value as supplied in a `RenderedQueryRequestV1`.

    `variable_kater_id` is preferred. Until every surface exposes it,
    `(query_kater_id, scope, name)` is the migration fallback identity.
    """

    name: str
    """Variable name within scope"""

    query_kater_id: str
    """Owning query UUID"""

    scope: Literal["query", "global"]

    value: Union[str, float, bool, List[object], Dict[str, object], None] = None
    """Free-form JSON variable value"""

    variable_kater_id: Optional[str] = None
    """Stable variable UUID; fall back to (query_kater_id, scope, name) when null"""


class WidgetDependenciesSlot(BaseModel):
    """A dashboard data slot that a widget depends on."""

    query_kater_id: str
    """Query kater_id backing the slot"""

    query_name: str
    """Query name backing the slot"""

    selected_field_ids: List[str]
    """UUIDs of selected fields for this dependency slot"""

    slot_name: str
    """Dashboard slot name"""

    timeframe_overrides: List[WidgetDependenciesSlotTimeframeOverride]
    """Temporal grain overrides for selected fields"""

    variable_values: List[WidgetDependenciesSlotVariableValue]
    """Runtime variable values applied to the slot"""

    combination: Optional[str] = None
    """Legacy combination string (derived, deprecated)"""

    pinned_variant: Optional[str] = None
    """Pinned query variant used for the slot, if any"""


class WidgetDependencies(BaseModel):
    """Dependency metadata describing which dashboard slots feed this widget"""

    slots: Optional[List[WidgetDependenciesSlot]] = None
    """Dashboard data slots that feed this widget"""


class WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateDimension(BaseModel):
    """Dimension entry inside the aggregate cache projection.

    `source_kater_id` is required (not nullable) here so two timeframe variants
    of the same temporal source dimension produce different cache projections.
    """

    active_timeframe: Optional[str] = None

    column_key: str

    source_kater_id: str


class WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateFilter(BaseModel):
    """Filter entry inside an exact or aggregate cache projection."""

    effective_kater_id: str

    enabled: bool

    expression: str

    field_active_timeframe: Optional[str] = None

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

    field_source_kater_id: Optional[str] = None

    normalized_value: Optional[str] = None


class WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateMeasure(BaseModel):
    """Measure entry inside the aggregate cache projection.

    `aggregation` is required (no None): an eligible aggregate cache always has
    a concrete aggregation function.
    """

    aggregation: Literal["sum", "count", "min", "max", "avg", "unknown"]

    column_key: str

    kater_id: str


class WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateVariable(BaseModel):
    """Variable entry inside an exact or aggregate cache projection."""

    name: str

    normalized_value: str

    query_kater_id: str

    variable_kater_id: Optional[str] = None


class WidgetRenderedQueryKeyCanonicalCacheProjectionAggregate(BaseModel):
    """Projection used to derive `aggregate_cache_key_id`. Null when not eligible."""

    client_id: str

    connection_kater_id: str

    dimensions: List[WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateDimension]

    filters: List[WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateFilter]

    measures: List[WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateMeasure]

    query_kater_id: str

    resolved_query_fingerprint: str

    source_fingerprint: str

    tenant_database: Optional[str] = None

    tenant_key: str

    variables: List[WidgetRenderedQueryKeyCanonicalCacheProjectionAggregateVariable]


class WidgetRenderedQueryKeyCanonicalCacheProjectionExactFilter(BaseModel):
    """Filter entry inside an exact or aggregate cache projection."""

    effective_kater_id: str

    enabled: bool

    expression: str

    field_active_timeframe: Optional[str] = None

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

    field_source_kater_id: Optional[str] = None

    normalized_value: Optional[str] = None


class WidgetRenderedQueryKeyCanonicalCacheProjectionExactOutputColumn(BaseModel):
    """Column entry inside the exact cache projection."""

    active_timeframe: Optional[str] = None

    column_key: str

    field_type: Literal["dimension", "measure", "calculation"]

    kater_id: str

    source_kater_id: Optional[str] = None


class WidgetRenderedQueryKeyCanonicalCacheProjectionExactResultWindow(BaseModel):
    """Result window subset inside the exact cache projection.

    Mirrors `RenderedQueryResultWindowV1` field-for-field today; kept distinct so
    cache-only changes do not perturb the canonical block hash, and so codegen
    emits a TypeScript type local to the cache projection per the PRD shape.
    """

    cursor: Optional[str] = None

    effective_limit: Optional[int] = None

    max_row_limit: Optional[int] = None

    page_size: Optional[int] = None

    query_limit: Optional[int] = None

    sort_by: Optional[str] = None

    sort_order: Optional[Literal["asc", "desc"]] = None


class WidgetRenderedQueryKeyCanonicalCacheProjectionExactVariable(BaseModel):
    """Variable entry inside an exact or aggregate cache projection."""

    name: str

    normalized_value: str

    query_kater_id: str

    variable_kater_id: Optional[str] = None


class WidgetRenderedQueryKeyCanonicalCacheProjectionExact(BaseModel):
    """Projection used to derive `exact_cache_key_id`."""

    client_id: str

    connection_kater_id: str

    filters: List[WidgetRenderedQueryKeyCanonicalCacheProjectionExactFilter]

    output_columns: List[WidgetRenderedQueryKeyCanonicalCacheProjectionExactOutputColumn]

    query_kater_id: str

    resolved_query_fingerprint: str

    result_window: WidgetRenderedQueryKeyCanonicalCacheProjectionExactResultWindow
    """Result window subset inside the exact cache projection.

    Mirrors `RenderedQueryResultWindowV1` field-for-field today; kept distinct so
    cache-only changes do not perturb the canonical block hash, and so codegen emits
    a TypeScript type local to the cache projection per the PRD shape.
    """

    source_fingerprint: str

    tenant_database: Optional[str] = None

    tenant_key: str

    variables: List[WidgetRenderedQueryKeyCanonicalCacheProjectionExactVariable]


class WidgetRenderedQueryKeyCanonicalCacheProjection(BaseModel):
    """Cache projection sub-document of `canonical`.

    The projection itself contains
    no derived cache key IDs — those IDs are derived from it and live at the top level.
    """

    aggregate: Optional[WidgetRenderedQueryKeyCanonicalCacheProjectionAggregate] = None
    """Projection used to derive `aggregate_cache_key_id`. Null when not eligible."""

    exact: WidgetRenderedQueryKeyCanonicalCacheProjectionExact
    """Projection used to derive `exact_cache_key_id`."""

    version: Literal[1]


class WidgetRenderedQueryKeyCanonicalContract(BaseModel):
    """Identifies the canonicalization contract that produced this key.

    Changes to any of these values mean the meaning of the key has changed and
    consumers must treat it as a new key.
    """

    compiler_version: str

    filter_state_version: Literal[2]

    key_schema: Literal["RenderedQueryKeyV1"]

    key_version: Literal[1]

    widget_config_version: str


class WidgetRenderedQueryKeyCanonicalDashboardDashboardFilterState(BaseModel):
    """Shared dashboard filter state mapped to slot-specific effective filters."""

    applied_slot_effective_kater_ids: List[str]

    dashboard_effective_kater_id: str

    enabled: bool

    normalized_value: Optional[str] = None

    value: Union[str, float, bool, List[object], Dict[str, object], None] = None


class WidgetRenderedQueryKeyCanonicalDashboard(BaseModel):
    """Null-filled for standalone query execution; populated for dashboard widgets."""

    dashboard_filter_state: List[WidgetRenderedQueryKeyCanonicalDashboardDashboardFilterState]

    dashboard_kater_id: Optional[str] = None

    dashboard_name: Optional[str] = None

    slot_name: Optional[str] = None

    widget_kater_id: Optional[str] = None

    widget_name: Optional[str] = None


class WidgetRenderedQueryKeyCanonicalFieldsActiveField(BaseModel):
    """A selected/active source field entry — strict subset of the field item."""

    active_timeframe: Optional[str] = None

    field_type: Literal["dimension", "measure", "calculation"]

    kater_id: str


class WidgetRenderedQueryKeyCanonicalFieldsOutputColumn(BaseModel):
    """An output column entry in `canonical.fields.output_columns`."""

    active_timeframe: Optional[str] = None
    """Concrete temporal grain (e.g. 'raw', 'month'); null for non-temporal"""

    aggregation: Optional[Literal["sum", "count", "min", "max", "avg", "unknown"]] = None

    column_key: str
    """SQL result alias / row payload key"""

    field_type: Literal["dimension", "measure", "calculation"]

    kater_id: str
    """Authored source field UUID"""

    label: Optional[str] = None

    name: str

    output_index: int
    """Zero-based output column position"""

    role: Optional[str] = None

    slot: Literal["required", "optional"]

    source_kater_id: Optional[str] = None
    """Source field UUID when derived from an authored field"""


class WidgetRenderedQueryKeyCanonicalFieldsSelectedField(BaseModel):
    """A selected/active source field entry — strict subset of the field item."""

    active_timeframe: Optional[str] = None

    field_type: Literal["dimension", "measure", "calculation"]

    kater_id: str


class WidgetRenderedQueryKeyCanonicalFields(BaseModel):
    """
    Selected, active, and output field lists that participate in compile and
    widget roles. Ordering rules: selected/active are sorted by stable identity;
    output_columns preserves output order.
    """

    active_fields: List[WidgetRenderedQueryKeyCanonicalFieldsActiveField]

    output_columns: List[WidgetRenderedQueryKeyCanonicalFieldsOutputColumn]

    selected_fields: List[WidgetRenderedQueryKeyCanonicalFieldsSelectedField]


class WidgetRenderedQueryKeyCanonicalFiltersEffectiveFilter(BaseModel):
    """An effective filter entry in `canonical.filters.effective_filters`."""

    data_type: str

    declaration_kater_ids: List[str]

    effective_kater_id: str

    enabled: bool

    expression: str

    field_active_timeframe: Optional[str] = None

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

    field_source_kater_id: Optional[str] = None

    label: Optional[str] = None

    mode: Literal["static", "parameterized"]

    name: str

    normalized_value: Optional[str] = None

    owner_chain: List[str]

    required: bool

    scope: Literal["model", "topic", "dashboard", "query"]

    value: Union[str, float, bool, List[object], Dict[str, object], None] = None


class WidgetRenderedQueryKeyCanonicalFilters(BaseModel):
    """Effective filter state (model + topic + dashboard + query, after resolution)."""

    effective_filters: List[WidgetRenderedQueryKeyCanonicalFiltersEffectiveFilter]


class WidgetRenderedQueryKeyCanonicalPresentation(BaseModel):
    """
    Non-data inputs that affect widget config, narrative, chart rendering, and SDK
    rendering behavior. `display`, `chart`, and `style` are the only free-form JSON
    sections in the canonical key.
    """

    chart: Dict[str, Union[str, int, float, bool, None, List[object], Dict[str, object]]]

    config_fingerprint: str

    display: Dict[str, Union[str, int, float, bool, None, List[object], Dict[str, object]]]

    roles: Dict[str, str]
    """Widget role -> column_key (not human-readable field name)"""

    style: Dict[str, Union[str, int, float, bool, None, List[object], Dict[str, object]]]

    widget_category: str

    widget_type: Optional[str] = None


class WidgetRenderedQueryKeyCanonicalQuery(BaseModel):
    """Anchors the rendered result to the query template and its selected field shape."""

    pinned_variant: Optional[str] = None

    query_kater_id: str

    resolved_query_fingerprint: str

    source_query_ref: str
    """Provenance only — consumers must not treat as identity"""


class WidgetRenderedQueryKeyCanonicalResultWindow(BaseModel):
    """Identifies the returned window of rows.

    `sort_by`, when present, is a column_key.
    """

    cursor: Optional[str] = None

    effective_limit: Optional[int] = None

    max_row_limit: Optional[int] = None

    page_size: Optional[int] = None

    query_limit: Optional[int] = None

    sort_by: Optional[str] = None

    sort_order: Optional[Literal["asc", "desc"]] = None


class WidgetRenderedQueryKeyCanonicalSource(BaseModel):
    """Identifies the exact Kater source bundle used to resolve and compile."""

    connection_config_fingerprint: str

    connection_kater_id: str

    dependency_graph_fingerprint: Optional[str] = None

    manifest_fingerprint: Optional[str] = None

    source_fingerprint: str

    source_kind: Literal["saved_repo", "branch", "dev_session"]

    source_ref: Optional[str] = None

    theme_fingerprint: Optional[str] = None

    widget_registry_fingerprint: str


class WidgetRenderedQueryKeyCanonicalTemporal(BaseModel):
    """Request clock context — makes date-relative filters deterministic.

    Selected date-grain identity lives in `fields.*.active_timeframe` and
    `fields.output_columns[].column_key`, not here.
    """

    as_of: str
    """ISO timestamp resolved once at the start of canonicalization"""

    timezone: str


class WidgetRenderedQueryKeyCanonicalTenant(BaseModel):
    """Hard tenant identity boundary."""

    client_id: str

    tenancy_mode: Literal["none", "row", "database"]

    tenant_attribute_fingerprint: Optional[str] = None

    tenant_database: Optional[str] = None

    tenant_key: str


class WidgetRenderedQueryKeyCanonicalVariable(BaseModel):
    """A variable applied to compile or post-assembly runtime substitution."""

    is_runtime: bool

    name: str

    normalized_value: str
    """Deterministic string used for hashing and cache projection"""

    query_kater_id: str

    scope: Literal["query", "global"]

    source: Literal["default", "request", "pinned_variant", "dashboard"]

    value: Union[str, float, bool, List[object], Dict[str, object], None] = None
    """Display/debug value (free-form JSON)"""

    variable_kater_id: Optional[str] = None


class WidgetRenderedQueryKeyCanonical(BaseModel):
    """The canonical sub-document. Hashing this produces `key_id`."""

    cache_projection: WidgetRenderedQueryKeyCanonicalCacheProjection
    """Cache projection sub-document of `canonical`.

    The projection itself contains no derived cache key IDs — those IDs are derived
    from it and live at the top level.
    """

    contract: WidgetRenderedQueryKeyCanonicalContract
    """Identifies the canonicalization contract that produced this key.

    Changes to any of these values mean the meaning of the key has changed and
    consumers must treat it as a new key.
    """

    dashboard: WidgetRenderedQueryKeyCanonicalDashboard
    """Null-filled for standalone query execution; populated for dashboard widgets."""

    fields: WidgetRenderedQueryKeyCanonicalFields
    """
    Selected, active, and output field lists that participate in compile and widget
    roles. Ordering rules: selected/active are sorted by stable identity;
    output_columns preserves output order.
    """

    filters: WidgetRenderedQueryKeyCanonicalFilters
    """Effective filter state (model + topic + dashboard + query, after resolution)."""

    presentation: WidgetRenderedQueryKeyCanonicalPresentation
    """
    Non-data inputs that affect widget config, narrative, chart rendering, and SDK
    rendering behavior. `display`, `chart`, and `style` are the only free-form JSON
    sections in the canonical key.
    """

    query: WidgetRenderedQueryKeyCanonicalQuery
    """Anchors the rendered result to the query template and its selected field shape."""

    result_window: WidgetRenderedQueryKeyCanonicalResultWindow
    """Identifies the returned window of rows.

    `sort_by`, when present, is a column_key.
    """

    source: WidgetRenderedQueryKeyCanonicalSource
    """Identifies the exact Kater source bundle used to resolve and compile."""

    temporal: WidgetRenderedQueryKeyCanonicalTemporal
    """Request clock context — makes date-relative filters deterministic.

    Selected date-grain identity lives in `fields.*.active_timeframe` and
    `fields.output_columns[].column_key`, not here.
    """

    tenant: WidgetRenderedQueryKeyCanonicalTenant
    """Hard tenant identity boundary."""

    variables: List[WidgetRenderedQueryKeyCanonicalVariable]


class WidgetRenderedQueryKey(BaseModel):
    """Top-level natural key returned by every runtime data and widget path.

    Format invariants (validation enforced by Story 1.2's hashing helpers):
    - `key_id`: `rqk_v1:<64 lowercase hex chars>`
    - `exact_cache_key_id`: `rqk_cache_exact_v1:<64 lowercase hex chars>`
    - `aggregate_cache_key_id`: `rqk_cache_agg_v1:<64 lowercase hex chars>` or null
    """

    aggregate_cache_key_id: Optional[str] = None
    """rqk_cache_agg_v1:<sha256-hex> or null when not eligible"""

    canonical: WidgetRenderedQueryKeyCanonical
    """The canonical sub-document. Hashing this produces `key_id`."""

    exact_cache_key_id: str
    """rqk_cache_exact_v1:<sha256-hex>"""

    key_id: str
    """rqk_v1:<sha256-hex>"""

    version: Literal[1]


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

    dependencies: Optional[WidgetDependencies] = None
    """Dependency metadata describing which dashboard slots feed this widget"""

    display_mode: Optional[str] = None
    """Display mode for multi-query: 'tabs' or 'grid'"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Per-widget compilation errors"""

    rendered_query_key: Optional[WidgetRenderedQueryKey] = None
    """Top-level natural key returned by every runtime data and widget path.

    Format invariants (validation enforced by Story 1.2's hashing helpers):

    - `key_id`: `rqk_v1:<64 lowercase hex chars>`
    - `exact_cache_key_id`: `rqk_cache_exact_v1:<64 lowercase hex chars>`
    - `aggregate_cache_key_id`: `rqk_cache_agg_v1:<64 lowercase hex chars>` or null
    """

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

    insight_runs: Optional[List[InsightRun]] = None
    """Structured dashboard-root insight execution results"""

    widgets: Optional[List[Widget]] = None
    """Fully resolved widgets with data + config"""
