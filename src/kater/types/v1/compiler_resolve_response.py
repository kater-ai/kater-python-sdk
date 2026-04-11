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

    request_id: Optional[str] = None
    """Write-back request ID.

    Non-null when ref-fix files were dispatched to CLI via WebSocket.
    """
