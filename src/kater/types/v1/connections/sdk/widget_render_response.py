# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel
from ...compiler_error_item import CompilerErrorItem

__all__ = [
    "WidgetRenderResponse",
    "AppliedFilterState",
    "AppliedFilterStateValue",
    "AppliedFilterStateValueScalarFilterValue",
    "AppliedFilterStateValueMultiFilterValue",
    "AppliedFilterStateValueNumberRangeFilterValue",
    "AppliedFilterStateValueAbsoluteDateFilterValue",
    "AppliedFilterStateValueAbsoluteRangeFilterValue",
    "AppliedFilterStateValueRelativeRangeFilterValue",
    "AppliedFilterStateValueRelativeRangeFilterValueEnd",
    "AppliedFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "AppliedFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "AppliedFilterStateValueRelativeRangeFilterValueStart",
    "AppliedFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "AppliedFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "AppliedFilterStateValuePresetReferenceFilterValue",
    "AppliedFilterStateValueNullFilterValue",
    "ColumnMap",
    "ColumnMapDataType",
    "ColumnMapDataTypeExtension",
    "ColumnMapModifier",
    "ColumnProfiles",
    "ConfigControls",
    "ConfigControlsChart",
    "ConfigControlsChartOption",
    "DefaultFilterState",
    "DefaultFilterStateValue",
    "DefaultFilterStateValueScalarFilterValue",
    "DefaultFilterStateValueMultiFilterValue",
    "DefaultFilterStateValueNumberRangeFilterValue",
    "DefaultFilterStateValueAbsoluteDateFilterValue",
    "DefaultFilterStateValueAbsoluteRangeFilterValue",
    "DefaultFilterStateValueRelativeRangeFilterValue",
    "DefaultFilterStateValueRelativeRangeFilterValueEnd",
    "DefaultFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "DefaultFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "DefaultFilterStateValueRelativeRangeFilterValueStart",
    "DefaultFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "DefaultFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "DefaultFilterStateValuePresetReferenceFilterValue",
    "DefaultFilterStateValueNullFilterValue",
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
    "RenderedQueryKey",
    "RenderedQueryKeyCanonical",
    "RenderedQueryKeyCanonicalCacheProjection",
    "RenderedQueryKeyCanonicalCacheProjectionAggregate",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateDimension",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateDimensionModifier",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateFilter",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateFilterFieldModifier",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateMeasure",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateVariable",
    "RenderedQueryKeyCanonicalCacheProjectionExact",
    "RenderedQueryKeyCanonicalCacheProjectionExactFilter",
    "RenderedQueryKeyCanonicalCacheProjectionExactFilterFieldModifier",
    "RenderedQueryKeyCanonicalCacheProjectionExactOutputColumn",
    "RenderedQueryKeyCanonicalCacheProjectionExactOutputColumnModifier",
    "RenderedQueryKeyCanonicalCacheProjectionExactResultWindow",
    "RenderedQueryKeyCanonicalCacheProjectionExactVariable",
    "RenderedQueryKeyCanonicalContract",
    "RenderedQueryKeyCanonicalDashboard",
    "RenderedQueryKeyCanonicalDashboardDashboardFilterState",
    "RenderedQueryKeyCanonicalFields",
    "RenderedQueryKeyCanonicalFieldsActiveField",
    "RenderedQueryKeyCanonicalFieldsActiveFieldModifier",
    "RenderedQueryKeyCanonicalFieldsOutputColumn",
    "RenderedQueryKeyCanonicalFieldsOutputColumnModifier",
    "RenderedQueryKeyCanonicalFieldsOutputColumnDataType",
    "RenderedQueryKeyCanonicalFieldsOutputColumnDataTypeExtension",
    "RenderedQueryKeyCanonicalFieldsSelectedField",
    "RenderedQueryKeyCanonicalFieldsSelectedFieldModifier",
    "RenderedQueryKeyCanonicalFilters",
    "RenderedQueryKeyCanonicalFiltersEffectiveFilter",
    "RenderedQueryKeyCanonicalFiltersEffectiveFilterFieldModifier",
    "RenderedQueryKeyCanonicalPresentation",
    "RenderedQueryKeyCanonicalQuery",
    "RenderedQueryKeyCanonicalResultWindow",
    "RenderedQueryKeyCanonicalSource",
    "RenderedQueryKeyCanonicalTemporal",
    "RenderedQueryKeyCanonicalTenant",
    "RenderedQueryKeyCanonicalVariable",
]


class AppliedFilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Scalar value compatible with Filter V2 runtime payloads"""

    mode: Optional[Literal["scalar"]] = None


class AppliedFilterStateValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class AppliedFilterStateValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class AppliedFilterStateValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class AppliedFilterStateValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class AppliedFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class AppliedFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


AppliedFilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    AppliedFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    AppliedFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class AppliedFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class AppliedFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


AppliedFilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    AppliedFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    AppliedFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class AppliedFilterStateValueRelativeRangeFilterValue(BaseModel):
    end: AppliedFilterStateValueRelativeRangeFilterValueEnd

    start: AppliedFilterStateValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class AppliedFilterStateValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class AppliedFilterStateValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


AppliedFilterStateValue: TypeAlias = Union[
    AppliedFilterStateValueScalarFilterValue,
    AppliedFilterStateValueMultiFilterValue,
    AppliedFilterStateValueNumberRangeFilterValue,
    AppliedFilterStateValueAbsoluteDateFilterValue,
    AppliedFilterStateValueAbsoluteRangeFilterValue,
    AppliedFilterStateValueRelativeRangeFilterValue,
    AppliedFilterStateValuePresetReferenceFilterValue,
    AppliedFilterStateValueNullFilterValue,
    None,
]


class AppliedFilterState(BaseModel):
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

    value: Optional[AppliedFilterStateValue] = None
    """Current typed runtime value"""


class ColumnMapDataTypeExtension(BaseModel):
    """Vendor-specific type extension"""

    engine: str
    """Database engine/dialect"""

    orig_type: str
    """Original type name in the source database"""

    options: Optional[Dict[str, object]] = None
    """Additional vendor-specific options"""

    raw_ddl: Optional[str] = None
    """Raw DDL for the type"""


class ColumnMapDataType(BaseModel):
    """Canonical data type metadata for this output column"""

    kind: Literal["Bool", "Text", "Number", "Datetime", "Complex", "Unknown"]
    """The canonical data type kind"""

    nullable: bool
    """Whether the field can be null"""

    extension: Optional[ColumnMapDataTypeExtension] = None
    """Vendor-specific type extension"""

    params: Optional[object] = None
    """Optional coarse metadata for the canonical type"""


class ColumnMapModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class ColumnMap(BaseModel):
    """Maps a UUID column alias to its human-readable name and type."""

    data_type: ColumnMapDataType
    """Canonical data type metadata for this output column"""

    field_type: str
    """Field type: dimension, measure, or calculation"""

    source_name: str
    """Source field name"""

    aggregation: Optional[str] = None
    """Aggregation type for measures: sum, count, min, max, avg, unknown.

    None for non-measures.
    """

    column_key: Optional[str] = None
    """SQL result alias for this concrete output column."""

    display_label: Optional[str] = None
    """Backend-provided display label"""

    modifiers: Optional[List[ColumnMapModifier]] = None
    """Normalized modifiers for this output occurrence.

    Raw timeframe is represented by an empty array.
    """

    source_kater_id: Optional[str] = None
    """Stable source field UUID for this output occurrence."""

    source_label: Optional[str] = None
    """Source field label"""


class ColumnProfiles(BaseModel):
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


class ConfigControlsChartOption(BaseModel):
    """Single select option for a backend-owned widget config control."""

    label: str
    """Human-readable display label"""

    value: str
    """Underlying config value"""


class ConfigControlsChart(BaseModel):
    """Backend-owned metadata for a widget config control."""

    options: Optional[List[ConfigControlsChartOption]] = None
    """Selectable options for the control when applicable"""


class ConfigControls(BaseModel):
    """Backend-owned widget config controls for the query builder panel."""

    chart: Optional[Dict[str, ConfigControlsChart]] = None
    """Chart config controls keyed by field name"""


class DefaultFilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Scalar value compatible with Filter V2 runtime payloads"""

    mode: Optional[Literal["scalar"]] = None


class DefaultFilterStateValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class DefaultFilterStateValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class DefaultFilterStateValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class DefaultFilterStateValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class DefaultFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class DefaultFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


DefaultFilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    DefaultFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    DefaultFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class DefaultFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class DefaultFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


DefaultFilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    DefaultFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    DefaultFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class DefaultFilterStateValueRelativeRangeFilterValue(BaseModel):
    end: DefaultFilterStateValueRelativeRangeFilterValueEnd

    start: DefaultFilterStateValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class DefaultFilterStateValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class DefaultFilterStateValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


DefaultFilterStateValue: TypeAlias = Union[
    DefaultFilterStateValueScalarFilterValue,
    DefaultFilterStateValueMultiFilterValue,
    DefaultFilterStateValueNumberRangeFilterValue,
    DefaultFilterStateValueAbsoluteDateFilterValue,
    DefaultFilterStateValueAbsoluteRangeFilterValue,
    DefaultFilterStateValueRelativeRangeFilterValue,
    DefaultFilterStateValuePresetReferenceFilterValue,
    DefaultFilterStateValueNullFilterValue,
    None,
]


class DefaultFilterState(BaseModel):
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

    value: Optional[DefaultFilterStateValue] = None
    """Current typed runtime value"""


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


class RenderedQueryKeyCanonicalCacheProjectionAggregateDimensionModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalCacheProjectionAggregateDimension(BaseModel):
    """Dimension entry inside the aggregate cache projection.

    `source_kater_id` plus normalized modifiers identify the projected source
    dimension in cache projections.
    """

    column_key: str

    modifiers: List[RenderedQueryKeyCanonicalCacheProjectionAggregateDimensionModifier]

    source_kater_id: str


class RenderedQueryKeyCanonicalCacheProjectionAggregateFilterFieldModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalCacheProjectionAggregateFilter(BaseModel):
    """Filter entry inside an exact or aggregate cache projection."""

    effective_kater_id: str

    enabled: bool

    expression: str

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

    field_modifiers: Optional[List[RenderedQueryKeyCanonicalCacheProjectionAggregateFilterFieldModifier]] = None

    field_source_kater_id: Optional[str] = None

    normalized_value: Optional[str] = None


class RenderedQueryKeyCanonicalCacheProjectionAggregateMeasure(BaseModel):
    """Measure entry inside the aggregate cache projection.

    `aggregation` is required (no None): an eligible aggregate cache always has
    a concrete aggregation function.
    """

    aggregation: Literal["sum", "count", "min", "max", "avg", "unknown"]

    column_key: str

    kater_id: str


class RenderedQueryKeyCanonicalCacheProjectionAggregateVariable(BaseModel):
    """Variable entry inside an exact or aggregate cache projection."""

    name: str

    normalized_value: str

    query_kater_id: str

    variable_kater_id: Optional[str] = None


class RenderedQueryKeyCanonicalCacheProjectionAggregate(BaseModel):
    """Projection used to derive `aggregate_cache_key_id`. Null when not eligible."""

    client_id: str

    connection_kater_id: str

    dimensions: List[RenderedQueryKeyCanonicalCacheProjectionAggregateDimension]

    filters: List[RenderedQueryKeyCanonicalCacheProjectionAggregateFilter]

    measures: List[RenderedQueryKeyCanonicalCacheProjectionAggregateMeasure]

    query_kater_id: str

    resolved_query_fingerprint: str

    source_fingerprint: str

    tenant_database: Optional[str] = None

    tenant_key: str

    variables: List[RenderedQueryKeyCanonicalCacheProjectionAggregateVariable]


class RenderedQueryKeyCanonicalCacheProjectionExactFilterFieldModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalCacheProjectionExactFilter(BaseModel):
    """Filter entry inside an exact or aggregate cache projection."""

    effective_kater_id: str

    enabled: bool

    expression: str

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

    field_modifiers: Optional[List[RenderedQueryKeyCanonicalCacheProjectionExactFilterFieldModifier]] = None

    field_source_kater_id: Optional[str] = None

    normalized_value: Optional[str] = None


class RenderedQueryKeyCanonicalCacheProjectionExactOutputColumnModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalCacheProjectionExactOutputColumn(BaseModel):
    """Column entry inside the exact cache projection."""

    column_key: str

    field_type: Literal["dimension", "measure", "calculation"]

    kater_id: str

    modifiers: List[RenderedQueryKeyCanonicalCacheProjectionExactOutputColumnModifier]

    source_kater_id: Optional[str] = None


class RenderedQueryKeyCanonicalCacheProjectionExactResultWindow(BaseModel):
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


class RenderedQueryKeyCanonicalCacheProjectionExactVariable(BaseModel):
    """Variable entry inside an exact or aggregate cache projection."""

    name: str

    normalized_value: str

    query_kater_id: str

    variable_kater_id: Optional[str] = None


class RenderedQueryKeyCanonicalCacheProjectionExact(BaseModel):
    """Projection used to derive `exact_cache_key_id`."""

    client_id: str

    connection_kater_id: str

    filters: List[RenderedQueryKeyCanonicalCacheProjectionExactFilter]

    output_columns: List[RenderedQueryKeyCanonicalCacheProjectionExactOutputColumn]

    query_kater_id: str

    resolved_query_fingerprint: str

    result_window: RenderedQueryKeyCanonicalCacheProjectionExactResultWindow
    """Result window subset inside the exact cache projection.

    Mirrors `RenderedQueryResultWindowV1` field-for-field today; kept distinct so
    cache-only changes do not perturb the canonical block hash, and so codegen emits
    a TypeScript type local to the cache projection per the PRD shape.
    """

    source_fingerprint: str

    tenant_database: Optional[str] = None

    tenant_key: str

    variables: List[RenderedQueryKeyCanonicalCacheProjectionExactVariable]


class RenderedQueryKeyCanonicalCacheProjection(BaseModel):
    """Cache projection sub-document of `canonical`.

    The projection itself contains
    no derived cache key IDs — those IDs are derived from it and live at the top level.
    """

    aggregate: Optional[RenderedQueryKeyCanonicalCacheProjectionAggregate] = None
    """Projection used to derive `aggregate_cache_key_id`. Null when not eligible."""

    exact: RenderedQueryKeyCanonicalCacheProjectionExact
    """Projection used to derive `exact_cache_key_id`."""

    version: Literal[1]


class RenderedQueryKeyCanonicalContract(BaseModel):
    """Identifies the canonicalization contract that produced this key.

    Changes to any of these values mean the meaning of the key has changed and
    consumers must treat it as a new key.
    """

    compiler_version: str

    filter_state_version: Literal[2]

    key_schema: Literal["RenderedQueryKeyV1"]

    key_version: Literal[1]

    widget_config_version: str


class RenderedQueryKeyCanonicalDashboardDashboardFilterState(BaseModel):
    """Shared dashboard filter state mapped to slot-specific effective filters."""

    applied_slot_effective_kater_ids: List[str]

    dashboard_effective_kater_id: str

    enabled: bool

    normalized_value: Optional[str] = None

    value: Union[str, float, bool, List[object], Dict[str, object], None] = None


class RenderedQueryKeyCanonicalDashboard(BaseModel):
    """Null-filled for standalone query execution; populated for dashboard widgets."""

    dashboard_filter_state: List[RenderedQueryKeyCanonicalDashboardDashboardFilterState]

    dashboard_kater_id: Optional[str] = None

    dashboard_name: Optional[str] = None

    slot_name: Optional[str] = None

    widget_kater_id: Optional[str] = None

    widget_name: Optional[str] = None


class RenderedQueryKeyCanonicalFieldsActiveFieldModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalFieldsActiveField(BaseModel):
    """A selected/active source field entry — strict subset of the field item."""

    field_type: Literal["dimension", "measure", "calculation"]

    modifiers: List[RenderedQueryKeyCanonicalFieldsActiveFieldModifier]

    source_kater_id: str


class RenderedQueryKeyCanonicalFieldsOutputColumnModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalFieldsOutputColumnDataTypeExtension(BaseModel):
    """Vendor-specific type extension"""

    engine: str
    """Database engine/dialect"""

    orig_type: str
    """Original type name in the source database"""

    options: Optional[Dict[str, object]] = None
    """Additional vendor-specific options"""

    raw_ddl: Optional[str] = None
    """Raw DDL for the type"""


class RenderedQueryKeyCanonicalFieldsOutputColumnDataType(BaseModel):
    """Data type specification"""

    kind: Literal["Bool", "Text", "Number", "Datetime", "Complex", "Unknown"]
    """The canonical data type kind"""

    nullable: bool
    """Whether the field can be null"""

    extension: Optional[RenderedQueryKeyCanonicalFieldsOutputColumnDataTypeExtension] = None
    """Vendor-specific type extension"""

    params: Optional[object] = None
    """Optional coarse metadata for the canonical type"""


class RenderedQueryKeyCanonicalFieldsOutputColumn(BaseModel):
    """An output column entry in `canonical.fields.output_columns`."""

    aggregation: Optional[Literal["sum", "count", "min", "max", "avg", "unknown"]] = None

    column_key: str
    """SQL result alias / row payload key"""

    display_label: Optional[str] = None

    field_type: Literal["dimension", "measure", "calculation"]

    modifiers: List[RenderedQueryKeyCanonicalFieldsOutputColumnModifier]
    """Normalized modifiers for this output occurrence"""

    output_index: int
    """Zero-based output column position"""

    role: Optional[str] = None

    slot: Literal["required", "optional"]

    source_kater_id: str
    """Stable source field UUID for this output occurrence"""

    source_label: Optional[str] = None

    source_name: str

    data_type: Optional[RenderedQueryKeyCanonicalFieldsOutputColumnDataType] = None
    """Data type specification"""


class RenderedQueryKeyCanonicalFieldsSelectedFieldModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalFieldsSelectedField(BaseModel):
    """A selected/active source field entry — strict subset of the field item."""

    field_type: Literal["dimension", "measure", "calculation"]

    modifiers: List[RenderedQueryKeyCanonicalFieldsSelectedFieldModifier]

    source_kater_id: str


class RenderedQueryKeyCanonicalFields(BaseModel):
    """
    Selected, active, and output field lists that participate in compile and
    widget roles. Ordering rules: selected/active are sorted by stable identity;
    output_columns preserves output order.
    """

    active_fields: List[RenderedQueryKeyCanonicalFieldsActiveField]

    output_columns: List[RenderedQueryKeyCanonicalFieldsOutputColumn]

    selected_fields: List[RenderedQueryKeyCanonicalFieldsSelectedField]


class RenderedQueryKeyCanonicalFiltersEffectiveFilterFieldModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class RenderedQueryKeyCanonicalFiltersEffectiveFilter(BaseModel):
    """An effective filter entry in `canonical.filters.effective_filters`."""

    data_type: str

    declaration_kater_ids: List[str]

    effective_kater_id: str

    enabled: bool

    expression: str

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

    field_modifiers: Optional[List[RenderedQueryKeyCanonicalFiltersEffectiveFilterFieldModifier]] = None

    field_source_kater_id: Optional[str] = None

    label: Optional[str] = None

    mode: Literal["static", "parameterized"]

    name: str

    normalized_value: Optional[str] = None

    owner_chain: List[str]

    required: bool

    scope: Literal["model", "topic", "dashboard", "query"]

    value: Union[str, float, bool, List[object], Dict[str, object], None] = None


class RenderedQueryKeyCanonicalFilters(BaseModel):
    """Effective filter state (model + topic + dashboard + query, after resolution)."""

    effective_filters: List[RenderedQueryKeyCanonicalFiltersEffectiveFilter]


class RenderedQueryKeyCanonicalPresentation(BaseModel):
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


class RenderedQueryKeyCanonicalQuery(BaseModel):
    """Anchors the rendered result to the query template and its selected field shape."""

    pinned_variant: Optional[str] = None

    query_kater_id: str

    resolved_query_fingerprint: str

    source_query_ref: str
    """Provenance only — consumers must not treat as identity"""


class RenderedQueryKeyCanonicalResultWindow(BaseModel):
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


class RenderedQueryKeyCanonicalSource(BaseModel):
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


class RenderedQueryKeyCanonicalTemporal(BaseModel):
    """Request clock context — makes date-relative filters deterministic.

    Selected date-grain identity lives in `fields.*.modifiers` and
    `fields.output_columns[].column_key`, not here.
    """

    as_of: str
    """ISO timestamp resolved once at the start of canonicalization"""

    timezone: str


class RenderedQueryKeyCanonicalTenant(BaseModel):
    """Hard tenant identity boundary."""

    client_id: str

    tenancy_mode: Literal["none", "row", "database"]

    tenant_attribute_fingerprint: Optional[str] = None

    tenant_database: Optional[str] = None

    tenant_key: str


class RenderedQueryKeyCanonicalVariable(BaseModel):
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


class RenderedQueryKeyCanonical(BaseModel):
    """The canonical sub-document. Hashing this produces `key_id`."""

    cache_projection: RenderedQueryKeyCanonicalCacheProjection
    """Cache projection sub-document of `canonical`.

    The projection itself contains no derived cache key IDs — those IDs are derived
    from it and live at the top level.
    """

    contract: RenderedQueryKeyCanonicalContract
    """Identifies the canonicalization contract that produced this key.

    Changes to any of these values mean the meaning of the key has changed and
    consumers must treat it as a new key.
    """

    dashboard: RenderedQueryKeyCanonicalDashboard
    """Null-filled for standalone query execution; populated for dashboard widgets."""

    fields: RenderedQueryKeyCanonicalFields
    """
    Selected, active, and output field lists that participate in compile and widget
    roles. Ordering rules: selected/active are sorted by stable identity;
    output_columns preserves output order.
    """

    filters: RenderedQueryKeyCanonicalFilters
    """Effective filter state (model + topic + dashboard + query, after resolution)."""

    presentation: RenderedQueryKeyCanonicalPresentation
    """
    Non-data inputs that affect widget config, narrative, chart rendering, and SDK
    rendering behavior. `display`, `chart`, and `style` are the only free-form JSON
    sections in the canonical key.
    """

    query: RenderedQueryKeyCanonicalQuery
    """Anchors the rendered result to the query template and its selected field shape."""

    result_window: RenderedQueryKeyCanonicalResultWindow
    """Identifies the returned window of rows.

    `sort_by`, when present, is a column_key.
    """

    source: RenderedQueryKeyCanonicalSource
    """Identifies the exact Kater source bundle used to resolve and compile."""

    temporal: RenderedQueryKeyCanonicalTemporal
    """Request clock context — makes date-relative filters deterministic.

    Selected date-grain identity lives in `fields.*.modifiers` and
    `fields.output_columns[].column_key`, not here.
    """

    tenant: RenderedQueryKeyCanonicalTenant
    """Hard tenant identity boundary."""

    variables: List[RenderedQueryKeyCanonicalVariable]


class RenderedQueryKey(BaseModel):
    """Top-level natural key returned by every runtime data and widget path.

    Format invariants (validation enforced by Story 1.2's hashing helpers):
    - `key_id`: `rqk_v2:<64 lowercase hex chars>`
    - `exact_cache_key_id`: `rqk_cache_exact_v2:<64 lowercase hex chars>`
    - `aggregate_cache_key_id`: `rqk_cache_agg_v2:<64 lowercase hex chars>` or null
    """

    aggregate_cache_key_id: Optional[str] = None
    """rqk_cache_agg_v2:<sha256-hex> or null when not eligible"""

    canonical: RenderedQueryKeyCanonical
    """The canonical sub-document. Hashing this produces `key_id`."""

    exact_cache_key_id: str
    """rqk_cache_exact_v2:<sha256-hex>"""

    key_id: str
    """rqk_v2:<sha256-hex>"""

    version: Literal[1]


class WidgetRenderResponse(BaseModel):
    """Response from the structured SDK widget render route.

    Returns a single widget's data + config for SDK consumers, plus a
    canonical `rendered_query_key` for stable cross-consumer identity.
    Shape matches CombinationPreviewResponse (minus internal metrics).
    """

    success: bool
    """Whether the preview succeeded"""

    applied_filter_state: Optional[List[AppliedFilterState]] = None
    """Applied runtime filter state for this widget preview"""

    auto_title: Optional[str] = None
    """Auto-generated title"""

    column_map: Optional[List[ColumnMap]] = None
    """Column metadata"""

    column_profiles: Optional[Dict[str, ColumnProfiles]] = None
    """Per-column statistical profiles keyed by kater_id (UUID column alias)."""

    config: Optional[Dict[str, object]] = None
    """Resolved WidgetConfig"""

    config_controls: Optional[ConfigControls] = None
    """Backend-owned widget config controls for the query builder panel."""

    data: Optional[List[Dict[str, object]]] = None
    """Query result rows"""

    default_filter_state: Optional[List[DefaultFilterState]] = None
    """Default runtime filter state for this widget preview"""

    dialect: Optional[str] = None
    """Warehouse dialect (e.g. snowflake, postgresql, databricks)"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Compilation errors"""

    filter_definitions: Optional[List[FilterDefinition]] = None
    """Resolved effective filter definitions for this widget preview"""

    has_more: Optional[bool] = None
    """Whether additional table rows can be fetched with next_cursor"""

    insight_runs: Optional[List[InsightRun]] = None
    """Structured runtime insight results for this widget preview."""

    is_row_limited: Optional[bool] = None
    """True when the app-wide row limit was applied and results were truncated"""

    next_cursor: Optional[str] = None
    """Opaque cursor for fetching the next table page"""

    page_size: Optional[int] = None
    """Number of rows requested per table page"""

    rendered_query_key: Optional[RenderedQueryKey] = None
    """Top-level natural key returned by every runtime data and widget path.

    Format invariants (validation enforced by Story 1.2's hashing helpers):

    - `key_id`: `rqk_v2:<64 lowercase hex chars>`
    - `exact_cache_key_id`: `rqk_cache_exact_v2:<64 lowercase hex chars>`
    - `aggregate_cache_key_id`: `rqk_cache_agg_v2:<64 lowercase hex chars>` or null
    """

    row_count: Optional[int] = None
    """Total rows represented by this widget result"""

    sql: Optional[str] = None
    """Compiled SQL query"""

    totals_row: Optional[Dict[str, object]] = None
    """Totals row over returned measure columns (UUID alias keys)"""

    widget_type: Optional[str] = None
    """Resolved widget type"""
