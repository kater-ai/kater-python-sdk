# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .manifest import Manifest
from ..._models import BaseModel
from .chart_config import ChartConfig
from .inline_field import InlineField
from .ref_with_label import RefWithLabel
from .subquery_condition import SubqueryCondition

__all__ = [
    "CompilerResolveResponse",
    "ResolvedQuery",
    "ResolvedQueryCalculation",
    "ResolvedQueryChartHint",
    "ResolvedQueryChartHintChartHint1Output",
    "ResolvedQueryChartHintChartHint2Output",
    "ResolvedQueryChartHintChartHint2OutputDefault",
    "ResolvedQueryDimension",
    "ResolvedQueryFilter",
    "ResolvedQueryFilterInlineFormulaFilter",
    "ResolvedQueryFilterInlineExistsFilter1",
    "ResolvedQueryFilterInlineExistsFilter2",
    "ResolvedQueryMeasure",
    "ResolvedQueryOrderBy",
    "ResolvedQueryOrderByOrderByItem",
    "ResolvedQueryResolvedChart",
    "ResolvedQueryResolvedVariable",
    "ResolvedQueryResolvedVariableAllowedValues",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2",
    "ResolvedQueryResolvedVariableConstraints",
    "ResolvedQuerySelectFrom",
    "ResolvedQuerySelectFromOutputColumn",
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
    "DependencyGraph",
    "DependencyGraphNodes",
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
    "RefFix",
    "RefFixReplacement",
    "RenderedQueryKey",
    "RenderedQueryKeyCanonical",
    "RenderedQueryKeyCanonicalCacheProjection",
    "RenderedQueryKeyCanonicalCacheProjectionAggregate",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateDimension",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateFilter",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateMeasure",
    "RenderedQueryKeyCanonicalCacheProjectionAggregateVariable",
    "RenderedQueryKeyCanonicalCacheProjectionExact",
    "RenderedQueryKeyCanonicalCacheProjectionExactFilter",
    "RenderedQueryKeyCanonicalCacheProjectionExactOutputColumn",
    "RenderedQueryKeyCanonicalCacheProjectionExactResultWindow",
    "RenderedQueryKeyCanonicalCacheProjectionExactVariable",
    "RenderedQueryKeyCanonicalContract",
    "RenderedQueryKeyCanonicalDashboard",
    "RenderedQueryKeyCanonicalDashboardDashboardFilterState",
    "RenderedQueryKeyCanonicalFields",
    "RenderedQueryKeyCanonicalFieldsActiveField",
    "RenderedQueryKeyCanonicalFieldsOutputColumn",
    "RenderedQueryKeyCanonicalFieldsSelectedField",
    "RenderedQueryKeyCanonicalFilters",
    "RenderedQueryKeyCanonicalFiltersEffectiveFilter",
    "RenderedQueryKeyCanonicalPresentation",
    "RenderedQueryKeyCanonicalQuery",
    "RenderedQueryKeyCanonicalResultWindow",
    "RenderedQueryKeyCanonicalSource",
    "RenderedQueryKeyCanonicalTemporal",
    "RenderedQueryKeyCanonicalTenant",
    "RenderedQueryKeyCanonicalVariable",
]

ResolvedQueryCalculation: TypeAlias = Union[RefWithLabel, InlineField, str]


class ResolvedQueryChartHintChartHint1Output(BaseModel):
    """A chart recommendation rule"""

    config: ChartConfig
    """Chart configuration with variable references"""

    recommend: Literal[
        "line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"
    ]
    """Type of chart visualization"""

    when: Dict[str, Union[str, List[str]]]
    """
    Conditions based on variable values - can be single value (string) or multiple
    values (array)
    """


class ResolvedQueryChartHintChartHint2OutputDefault(BaseModel):
    config: ChartConfig
    """Chart configuration with variable references"""

    recommend: Literal[
        "line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"
    ]
    """Type of chart visualization"""


class ResolvedQueryChartHintChartHint2Output(BaseModel):
    """A chart recommendation rule"""

    default: ResolvedQueryChartHintChartHint2OutputDefault


ResolvedQueryChartHint: TypeAlias = Union[
    ResolvedQueryChartHintChartHint1Output, ResolvedQueryChartHintChartHint2Output
]

ResolvedQueryDimension: TypeAlias = Union[RefWithLabel, InlineField, str]


class ResolvedQueryFilterInlineFormulaFilter(BaseModel):
    """An inline filter using a SQL/expression formula"""

    name: str
    """Name of the inline filter"""

    sql: str
    """SQL expression for the filter condition"""


class ResolvedQueryFilterInlineExistsFilter1(BaseModel):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    exists: SubqueryCondition
    """EXISTS subquery condition"""

    name: str
    """Name of the inline filter"""

    description: Optional[str] = None
    """Description of the filter"""

    label: Optional[str] = None
    """Human-readable label"""

    not_exists: Optional[SubqueryCondition] = None
    """A subquery condition for EXISTS/NOT EXISTS filters"""


class ResolvedQueryFilterInlineExistsFilter2(BaseModel):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    name: str
    """Name of the inline filter"""

    not_exists: SubqueryCondition
    """NOT EXISTS subquery condition"""

    description: Optional[str] = None
    """Description of the filter"""

    exists: Optional[SubqueryCondition] = None
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    label: Optional[str] = None
    """Human-readable label"""


ResolvedQueryFilter: TypeAlias = Union[
    ResolvedQueryFilterInlineFormulaFilter,
    str,
    ResolvedQueryFilterInlineExistsFilter1,
    ResolvedQueryFilterInlineExistsFilter2,
]

ResolvedQueryMeasure: TypeAlias = Union[RefWithLabel, InlineField, str]


class ResolvedQueryOrderByOrderByItem(BaseModel):
    """Explicit sort direction for a field."""

    direction: Literal["asc", "desc"]
    """
    Sort direction: asc (ascending, A-Z / oldest first) or desc (descending, Z-A /
    newest first).
    """

    field: str
    """A string that may be a ref(), var(), or expr() reference"""


ResolvedQueryOrderBy: TypeAlias = Union[ResolvedQueryOrderByOrderByItem, str]


class ResolvedQueryResolvedChart(BaseModel):
    """The matched chart recommendation after evaluating chart hints"""

    config: ChartConfig
    """Chart configuration"""

    recommend: Literal[
        "line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"
    ]
    """Recommended chart type"""


class ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static(BaseModel):
    """A value with optional display label"""

    value: Union[str, float, bool]
    """The actual value"""

    label: Optional[str] = None
    """Human-readable label for the value"""


class ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1(BaseModel):
    """Allowed values for a variable - either static list or from column"""

    static: List[ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static]
    """Static list of allowed values with optional labels"""


class ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2(BaseModel):
    """Allowed values for a variable - either static list or from column"""

    from_column: str
    """Reference to column for dynamic values"""

    cache_ttl: Optional[int] = None
    """Cache time-to-live in seconds"""

    limit: Optional[int] = None
    """Maximum number of values to retrieve"""

    order_by: Optional[Literal["asc", "desc"]] = None
    """Sort order for values"""


ResolvedQueryResolvedVariableAllowedValues: TypeAlias = Union[
    ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1,
    ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2,
    None,
]


class ResolvedQueryResolvedVariableConstraints(BaseModel):
    """Constraints for variable types"""

    max: Optional[float] = None
    """Maximum allowed value"""

    max_length: Optional[int] = None
    """Maximum length for STRING variables"""

    min: Optional[float] = None
    """Minimum allowed value"""

    step: Optional[float] = None
    """Step increment for numeric input"""


class ResolvedQueryResolvedVariable(BaseModel):
    """A variable definition with its bound value"""

    bound_value: Union[str, float, bool, List[Union[str, float, bool]]]
    """The concrete value bound for this resolution"""

    default: Union[str, float, bool, List[Union[str, float, bool]]]
    """Default value for this variable"""

    kater_id: str
    """Unique identifier for this variable"""

    name: str
    """Variable name identifier"""

    type: Literal[
        "STRING",
        "INT",
        "FLOAT",
        "DATE",
        "TIMESTAMP",
        "BOOL",
        "STRING[]",
        "INT[]",
        "FLOAT[]",
        "DATE[]",
        "DIMENSION",
        "MEASURE",
        "CALCULATION",
        "FILTER",
        "TIMEFRAME",
    ]
    """Data type of the variable"""

    allowed_values: Optional[ResolvedQueryResolvedVariableAllowedValues] = None
    """Allowed values configuration"""

    constraints: Optional[ResolvedQueryResolvedVariableConstraints] = None
    """Constraints for variable types"""

    description: Optional[str] = None
    """Description of the variable's purpose"""

    is_default: Optional[bool] = None
    """True if bound_value equals the default value"""

    is_runtime: Optional[bool] = None
    """True if this is a runtime variable (not resolved at compile time).

    Runtime variables have var() placeholders left in compiled SQL for literal
    substitution at execution time.
    """

    label: Optional[str] = None
    """Human-readable label for the variable"""


class ResolvedQuerySelectFromOutputColumn(BaseModel):
    """A column produced by a select_from CTE"""

    column_alias: str
    """The SQL column alias in the CTE output"""

    field_name: str
    """The field name used in q:query_name.field_name references"""

    source_type: Literal["dimension", "dimension_date", "measure", "calculation"]
    """Original type of the field in the source query"""


class ResolvedQuerySelectFrom(BaseModel):
    """A resolved select_from entry with CTE metadata"""

    cte_alias: str
    """CTE alias used in the WITH clause (e.g., **sf_compliance_rate**base)"""

    output_columns: List[ResolvedQuerySelectFromOutputColumn]
    """Columns produced by the CTE, available as q:query_name.field_name in the parent"""

    ref: str
    """Reference to the source query"""

    variables: Optional[Dict[str, Union[str, float, bool]]] = None
    """Variable overrides passed to the referenced query"""


class ResolvedQuery(BaseModel):
    """The fully resolved query object"""

    kater_id: str
    """Unique identifier for this resolved query instance"""

    name: str
    """Name from the leaf query in the inheritance chain"""

    source_query: str
    """Reference to the original query template this was resolved from"""

    topic: str
    """
    Reference to the topic this query uses (always known after inheritance
    resolution)
    """

    widget_category: Literal["axis", "funnel", "heatmap", "image", "kpi_card", "pie", "radial", "table", "text"]
    """Widget category that determines data shape constraints"""

    ai_context: Optional[str] = None
    """Usage guidance for AI processing"""

    calculations: Optional[List[ResolvedQueryCalculation]] = None
    """Merged required + selected optional calculations"""

    chart_hints: Optional[List[ResolvedQueryChartHint]] = None
    """Chart recommendations preserved for evaluation"""

    custom_properties: Optional[Dict[str, object]] = None
    """Custom properties"""

    description: Optional[str] = None
    """Description of the query"""

    dimensions: Optional[List[ResolvedQueryDimension]] = None
    """Merged required + selected optional dimensions"""

    disallowed_widget_types: Optional[
        List[
            Literal[
                "axis_metric_by_dimension",
                "axis_metric_by_dimensiondate",
                "axis_metric_by_dimensiondate_sliced_by_dimension",
                "axis_metric_by_metric",
                "funnel_funnel_chart",
                "heatmap_heatmap",
                "image_image_grid",
                "image_single_image",
                "kpi_measure_with_dimension_expression",
                "kpi_measure_with_secondary_metric",
                "kpi_measure_with_target_progress",
                "kpi_single_measure_compared_to_prev_period_sparkline",
                "kpi_single_value",
                "pie_donut_chart",
                "pie_donut_with_measure",
                "pie_pie_chart",
                "radial_chart",
                "radial_with_single_value",
                "radial_with_single_value_stacked",
                "table_data_table",
                "table_fancy_subtotal_table",
                "table_key_value_list",
                "table_styled_table",
                "text_data_readout_with_sparkline",
                "text_narrative_text",
            ]
        ]
    ] = None
    """
    Widget types within the declared widget_category that must NOT render this query
    """

    filters: Optional[List[ResolvedQueryFilter]] = None
    """Merged required + selected optional filters"""

    inheritance_chain: Optional[List[str]] = None
    """Ordered list of query refs that were merged during inheritance resolution"""

    label: Optional[str] = None
    """Human-readable label with var() values substituted"""

    limit: Optional[int] = None
    """Maximum number of rows to return"""

    measures: Optional[List[ResolvedQueryMeasure]] = None
    """Merged required + selected optional measures"""

    order_by: Optional[List[ResolvedQueryOrderBy]] = None
    """Sort order for query results"""

    resolved_chart: Optional[ResolvedQueryResolvedChart] = None
    """The matched chart recommendation after evaluating chart hints"""

    resolved_variables: Optional[List[ResolvedQueryResolvedVariable]] = None
    """Full variable definitions with bound values"""

    select_from: Optional[List[ResolvedQuerySelectFrom]] = None
    """Resolved select_from entries with CTE metadata"""

    totals: Optional[bool] = None
    """
    When true, compute a totals_row over returned measure columns and expose it
    alongside data.
    """


class AppliedFilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

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

    kind: Optional[str] = None
    """Interactive filter kind"""

    label: Optional[str] = None
    """Human-readable filter label"""

    value: Optional[AppliedFilterStateValue] = None
    """Current typed runtime value"""


class DefaultFilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

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

    kind: Optional[str] = None
    """Interactive filter kind"""

    label: Optional[str] = None
    """Human-readable filter label"""

    value: Optional[DefaultFilterStateValue] = None
    """Current typed runtime value"""


class DependencyGraphNodes(BaseModel):
    """A node in the dependency graph."""

    file: str
    """Source file path"""

    fqn: str
    """Fully qualified name (e.g. 'dim_customer.region')"""

    kater_id: str
    """UUID of the schema object"""

    line: int
    """Line number in source file"""

    node_type: str
    """Node type: QUERY, VIEW, DIMENSION, MEASURE, FILTER, EXPRESSION"""

    column: Optional[int] = None
    """Column number in source file"""


class DependencyGraph(BaseModel):
    """Dependency graph between schema objects."""

    edges: Dict[str, Dict[str, List[str]]]
    """Edge relationships with UUID string keys"""

    nodes: Dict[str, DependencyGraphNodes]
    """UUID string to node mapping"""


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


class RefFixReplacement(BaseModel):
    """A single ref replacement within a file."""

    file_path: str
    """Path to the file containing the replaced ref"""

    line_number: int
    """Line number where the replacement occurred"""

    new_ref: str
    """Updated reference string"""

    old_ref: str
    """Original reference string"""


class RefFix(BaseModel):
    """A file that was modified by auto-fix with its replacements."""

    file_path: str
    """Path to the modified file"""

    new_content: str
    """Full updated file content after fixes"""

    replacements: List[RefFixReplacement]
    """Individual ref replacements made in this file"""


class RenderedQueryKeyCanonicalCacheProjectionAggregateDimension(BaseModel):
    """Dimension entry inside the aggregate cache projection.

    `source_kater_id` is required (not nullable) here so two timeframe variants
    of the same temporal source dimension produce different cache projections.
    """

    active_timeframe: Optional[str] = None

    column_key: str

    source_kater_id: str


class RenderedQueryKeyCanonicalCacheProjectionAggregateFilter(BaseModel):
    """Filter entry inside an exact or aggregate cache projection."""

    effective_kater_id: str

    enabled: bool

    expression: str

    field_active_timeframe: Optional[str] = None

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

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


class RenderedQueryKeyCanonicalCacheProjectionExactFilter(BaseModel):
    """Filter entry inside an exact or aggregate cache projection."""

    effective_kater_id: str

    enabled: bool

    expression: str

    field_active_timeframe: Optional[str] = None

    field_column_key: Optional[str] = None

    field_kater_id: Optional[str] = None

    field_source_kater_id: Optional[str] = None

    normalized_value: Optional[str] = None


class RenderedQueryKeyCanonicalCacheProjectionExactOutputColumn(BaseModel):
    """Column entry inside the exact cache projection."""

    active_timeframe: Optional[str] = None

    column_key: str

    field_type: Literal["dimension", "dimension_date", "measure", "calculation"]

    kater_id: str

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


class RenderedQueryKeyCanonicalFieldsActiveField(BaseModel):
    """A selected/active source field entry — strict subset of the field item."""

    active_timeframe: Optional[str] = None

    field_type: Literal["dimension", "dimension_date", "measure", "calculation"]

    kater_id: str


class RenderedQueryKeyCanonicalFieldsOutputColumn(BaseModel):
    """An output column entry in `canonical.fields.output_columns`."""

    active_timeframe: Optional[str] = None
    """Concrete temporal grain (e.g. 'raw', 'month'); null for non-temporal"""

    aggregation: Optional[Literal["sum", "count", "min", "max", "avg", "unknown"]] = None

    column_key: str
    """SQL result alias / row payload key"""

    field_type: Literal["dimension", "dimension_date", "measure", "calculation"]

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


class RenderedQueryKeyCanonicalFieldsSelectedField(BaseModel):
    """A selected/active source field entry — strict subset of the field item."""

    active_timeframe: Optional[str] = None

    field_type: Literal["dimension", "dimension_date", "measure", "calculation"]

    kater_id: str


class RenderedQueryKeyCanonicalFields(BaseModel):
    """
    Selected, active, and output field lists that participate in compile and
    widget roles. Ordering rules: selected/active are sorted by stable identity;
    output_columns preserves output order.
    """

    active_fields: List[RenderedQueryKeyCanonicalFieldsActiveField]

    output_columns: List[RenderedQueryKeyCanonicalFieldsOutputColumn]

    selected_fields: List[RenderedQueryKeyCanonicalFieldsSelectedField]


class RenderedQueryKeyCanonicalFiltersEffectiveFilter(BaseModel):
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

    Selected date-grain identity lives in `fields.*.active_timeframe` and
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

    Selected date-grain identity lives in `fields.*.active_timeframe` and
    `fields.output_columns[].column_key`, not here.
    """

    tenant: RenderedQueryKeyCanonicalTenant
    """Hard tenant identity boundary."""

    variables: List[RenderedQueryKeyCanonicalVariable]


class RenderedQueryKey(BaseModel):
    """Top-level natural key returned by every runtime data and widget path.

    Format invariants (validation enforced by Story 1.2's hashing helpers):
    - `key_id`: `rqk_v1:<64 lowercase hex chars>`
    - `exact_cache_key_id`: `rqk_cache_exact_v1:<64 lowercase hex chars>`
    - `aggregate_cache_key_id`: `rqk_cache_agg_v1:<64 lowercase hex chars>` or null
    """

    aggregate_cache_key_id: Optional[str] = None
    """rqk_cache_agg_v1:<sha256-hex> or null when not eligible"""

    canonical: RenderedQueryKeyCanonical
    """The canonical sub-document. Hashing this produces `key_id`."""

    exact_cache_key_id: str
    """rqk_cache_exact_v1:<sha256-hex>"""

    key_id: str
    """rqk_v1:<sha256-hex>"""

    version: Literal[1]


class CompilerResolveResponse(BaseModel):
    """Response model for a resolved query."""

    resolved_query: ResolvedQuery
    """The fully resolved query object"""

    applied_filter_state: Optional[List[AppliedFilterState]] = None
    """Applied runtime filter state after request overrides"""

    default_filter_state: Optional[List[DefaultFilterState]] = None
    """Default runtime filter state derived from filter definitions"""

    dependency_graph: Optional[DependencyGraph] = None
    """Dependency graph between schema objects."""

    filter_definitions: Optional[List[FilterDefinition]] = None
    """Resolved effective filter definitions for this query context"""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""

    ref_fixes: Optional[List[RefFix]] = None
    """Files auto-fixed due to renamed refs. None when no renames detected."""

    rendered_query_key: Optional[RenderedQueryKey] = None
    """Top-level natural key returned by every runtime data and widget path.

    Format invariants (validation enforced by Story 1.2's hashing helpers):

    - `key_id`: `rqk_v1:<64 lowercase hex chars>`
    - `exact_cache_key_id`: `rqk_cache_exact_v1:<64 lowercase hex chars>`
    - `aggregate_cache_key_id`: `rqk_cache_agg_v1:<64 lowercase hex chars>` or null
    """

    request_id: Optional[str] = None
    """Write-back request ID.

    Non-null when ref-fix files were dispatched to CLI via WebSocket.
    """
