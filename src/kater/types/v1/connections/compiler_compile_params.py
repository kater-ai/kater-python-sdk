# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "CompilerCompileParams",
    "ResolvedQuery",
    "ResolvedQueryCalculation",
    "ResolvedQueryCalculationRefWithLabel",
    "ResolvedQueryCalculationInlineField",
    "ResolvedQueryChartHint",
    "ResolvedQueryChartHintChartHint1",
    "ResolvedQueryChartHintChartHint1Config",
    "ResolvedQueryChartHintChartHint2Input",
    "ResolvedQueryChartHintChartHint2InputDefault",
    "ResolvedQueryChartHintChartHint2InputDefaultConfig",
    "ResolvedQueryDimension",
    "ResolvedQueryDimensionRefWithLabel",
    "ResolvedQueryDimensionInlineField",
    "ResolvedQueryFilter",
    "ResolvedQueryFilterInlineFieldFilter",
    "ResolvedQueryFilterInlineExistsFilter1",
    "ResolvedQueryFilterInlineExistsFilter1Exists",
    "ResolvedQueryFilterInlineExistsFilter1NotExists",
    "ResolvedQueryFilterInlineExistsFilter2",
    "ResolvedQueryFilterInlineExistsFilter2NotExists",
    "ResolvedQueryFilterInlineExistsFilter2Exists",
    "ResolvedQueryMeasure",
    "ResolvedQueryMeasureRefWithLabel",
    "ResolvedQueryMeasureInlineField",
    "ResolvedQueryOrderBy",
    "ResolvedQueryResolvedChart",
    "ResolvedQueryResolvedChartConfig",
    "ResolvedQueryResolvedVariable",
    "ResolvedQueryResolvedVariableAllowedValues",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2",
    "ResolvedQueryResolvedVariableConstraints",
]


class CompilerCompileParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection to compile against"""

    resolved_query: Required[ResolvedQuery]
    """Previously resolved query object from /resolve"""

    source: Optional[str]

    tenant_database: Optional[str]
    """Optional tenant database override"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]


class ResolvedQueryCalculationRefWithLabel(TypedDict, total=False):
    """A reference with optional label override"""

    ref: Required[str]
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str]
    """Optional label override for this reference"""


class ResolvedQueryCalculationInlineField(TypedDict, total=False):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: Required[str]
    """Unique identifier for this inline field"""

    name: Required[str]
    """Name of the inline field"""

    sql: Required[str]
    """SQL expression for the field"""

    label: Optional[str]
    """Human-readable label"""


ResolvedQueryCalculation: TypeAlias = Union[
    ResolvedQueryCalculationRefWithLabel, ResolvedQueryCalculationInlineField, str
]


class ResolvedQueryChartHintChartHint1Config(TypedDict, total=False):
    """Chart configuration with variable references"""

    color_by: Optional[str]
    """Field or variable reference for color grouping"""

    size: Optional[str]
    """Field or variable reference for size"""

    stack_by: Optional[str]
    """Field or variable reference for stacking"""

    x_axis: Optional[str]
    """Field or variable reference for x-axis"""

    y_axis: Optional[str]
    """Field or variable reference for y-axis"""


class ResolvedQueryChartHintChartHint1(TypedDict, total=False):
    """A chart recommendation rule"""

    config: Required[ResolvedQueryChartHintChartHint1Config]
    """Chart configuration with variable references"""

    recommend: Required[
        Literal["line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"]
    ]
    """Type of chart visualization"""

    when: Required[Dict[str, Union[str, SequenceNotStr[str]]]]
    """
    Conditions based on variable values - can be single value (string) or multiple
    values (array)
    """


class ResolvedQueryChartHintChartHint2InputDefaultConfig(TypedDict, total=False):
    """Chart configuration with variable references"""

    color_by: Optional[str]
    """Field or variable reference for color grouping"""

    size: Optional[str]
    """Field or variable reference for size"""

    stack_by: Optional[str]
    """Field or variable reference for stacking"""

    x_axis: Optional[str]
    """Field or variable reference for x-axis"""

    y_axis: Optional[str]
    """Field or variable reference for y-axis"""


class ResolvedQueryChartHintChartHint2InputDefault(TypedDict, total=False):
    config: Required[ResolvedQueryChartHintChartHint2InputDefaultConfig]
    """Chart configuration with variable references"""

    recommend: Required[
        Literal["line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"]
    ]
    """Type of chart visualization"""


class ResolvedQueryChartHintChartHint2Input(TypedDict, total=False):
    """A chart recommendation rule"""

    default: Required[ResolvedQueryChartHintChartHint2InputDefault]


ResolvedQueryChartHint: TypeAlias = Union[ResolvedQueryChartHintChartHint1, ResolvedQueryChartHintChartHint2Input]


class ResolvedQueryDimensionRefWithLabel(TypedDict, total=False):
    """A reference with optional label override"""

    ref: Required[str]
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str]
    """Optional label override for this reference"""


class ResolvedQueryDimensionInlineField(TypedDict, total=False):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: Required[str]
    """Unique identifier for this inline field"""

    name: Required[str]
    """Name of the inline field"""

    sql: Required[str]
    """SQL expression for the field"""

    label: Optional[str]
    """Human-readable label"""


ResolvedQueryDimension: TypeAlias = Union[ResolvedQueryDimensionRefWithLabel, ResolvedQueryDimensionInlineField, str]


class ResolvedQueryFilterInlineFieldFilter(TypedDict, total=False):
    """An inline filter using field + operator + values"""

    field: Required[str]
    """Reference to the field to filter on"""

    name: Required[str]
    """Name of the inline filter"""

    operator: Required[
        Literal[
            "equals",
            "not_equals",
            "in",
            "not_in",
            "greater_than",
            "less_than",
            "greater_than_or_equals",
            "less_than_or_equals",
            "between",
            "in_the_last",
            "in_the_next",
            "contains",
            "not_contains",
            "starts_with",
            "ends_with",
            "is_null",
            "is_not_null",
        ]
    ]
    """Filter operator to apply"""

    sql_value: Optional[str]
    """SQL expression for the filter value"""

    static_values: Optional[SequenceNotStr[Union[str, float, bool]]]
    """Fixed values for the filter"""


_ResolvedQueryFilterInlineExistsFilter1ExistsReservedKeywords = TypedDict(
    "_ResolvedQueryFilterInlineExistsFilter1ExistsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResolvedQueryFilterInlineExistsFilter1Exists(
    _ResolvedQueryFilterInlineExistsFilter1ExistsReservedKeywords, total=False
):
    """EXISTS subquery condition"""

    where: Required[SequenceNotStr[str]]
    """WHERE conditions for the subquery"""


_ResolvedQueryFilterInlineExistsFilter1NotExistsReservedKeywords = TypedDict(
    "_ResolvedQueryFilterInlineExistsFilter1NotExistsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResolvedQueryFilterInlineExistsFilter1NotExists(
    _ResolvedQueryFilterInlineExistsFilter1NotExistsReservedKeywords, total=False
):
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    where: Required[SequenceNotStr[str]]
    """WHERE conditions for the subquery"""


class ResolvedQueryFilterInlineExistsFilter1(TypedDict, total=False):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    exists: Required[ResolvedQueryFilterInlineExistsFilter1Exists]
    """EXISTS subquery condition"""

    name: Required[str]
    """Name of the inline filter"""

    description: Optional[str]
    """Description of the filter"""

    label: Optional[str]
    """Human-readable label"""

    not_exists: Optional[ResolvedQueryFilterInlineExistsFilter1NotExists]
    """A subquery condition for EXISTS/NOT EXISTS filters"""


_ResolvedQueryFilterInlineExistsFilter2NotExistsReservedKeywords = TypedDict(
    "_ResolvedQueryFilterInlineExistsFilter2NotExistsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResolvedQueryFilterInlineExistsFilter2NotExists(
    _ResolvedQueryFilterInlineExistsFilter2NotExistsReservedKeywords, total=False
):
    """NOT EXISTS subquery condition"""

    where: Required[SequenceNotStr[str]]
    """WHERE conditions for the subquery"""


_ResolvedQueryFilterInlineExistsFilter2ExistsReservedKeywords = TypedDict(
    "_ResolvedQueryFilterInlineExistsFilter2ExistsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResolvedQueryFilterInlineExistsFilter2Exists(
    _ResolvedQueryFilterInlineExistsFilter2ExistsReservedKeywords, total=False
):
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    where: Required[SequenceNotStr[str]]
    """WHERE conditions for the subquery"""


class ResolvedQueryFilterInlineExistsFilter2(TypedDict, total=False):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    name: Required[str]
    """Name of the inline filter"""

    not_exists: Required[ResolvedQueryFilterInlineExistsFilter2NotExists]
    """NOT EXISTS subquery condition"""

    description: Optional[str]
    """Description of the filter"""

    exists: Optional[ResolvedQueryFilterInlineExistsFilter2Exists]
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    label: Optional[str]
    """Human-readable label"""


ResolvedQueryFilter: TypeAlias = Union[
    ResolvedQueryFilterInlineFieldFilter,
    str,
    ResolvedQueryFilterInlineExistsFilter1,
    ResolvedQueryFilterInlineExistsFilter2,
]


class ResolvedQueryMeasureRefWithLabel(TypedDict, total=False):
    """A reference with optional label override"""

    ref: Required[str]
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str]
    """Optional label override for this reference"""


class ResolvedQueryMeasureInlineField(TypedDict, total=False):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: Required[str]
    """Unique identifier for this inline field"""

    name: Required[str]
    """Name of the inline field"""

    sql: Required[str]
    """SQL expression for the field"""

    label: Optional[str]
    """Human-readable label"""


ResolvedQueryMeasure: TypeAlias = Union[ResolvedQueryMeasureRefWithLabel, ResolvedQueryMeasureInlineField, str]


class ResolvedQueryOrderBy(TypedDict, total=False):
    """Sort order specification for query results.

    Use desc for descending (highest/newest first) and asc for ascending (lowest/oldest first).
    """

    asc: Optional[SequenceNotStr[str]]
    """Fields to sort in ascending order (lowest/oldest first)"""

    desc: Optional[SequenceNotStr[str]]
    """Fields to sort in descending order (highest/newest first)"""


class ResolvedQueryResolvedChartConfig(TypedDict, total=False):
    """Chart configuration"""

    color_by: Optional[str]
    """Field or variable reference for color grouping"""

    size: Optional[str]
    """Field or variable reference for size"""

    stack_by: Optional[str]
    """Field or variable reference for stacking"""

    x_axis: Optional[str]
    """Field or variable reference for x-axis"""

    y_axis: Optional[str]
    """Field or variable reference for y-axis"""


class ResolvedQueryResolvedChart(TypedDict, total=False):
    """The matched chart recommendation after evaluating chart hints"""

    config: Required[ResolvedQueryResolvedChartConfig]
    """Chart configuration"""

    recommend: Required[
        Literal["line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"]
    ]
    """Recommended chart type"""


class ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static(TypedDict, total=False):
    """A value with optional display label"""

    value: Required[Union[str, float, bool]]
    """The actual value"""

    label: Optional[str]
    """Human-readable label for the value"""


class ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1(TypedDict, total=False):
    """Allowed values for a variable - either static list or from column"""

    static: Required[Iterable[ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static]]
    """Static list of allowed values with optional labels"""


class ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2(TypedDict, total=False):
    """Allowed values for a variable - either static list or from column"""

    from_column: Required[str]
    """Reference to column for dynamic values"""

    cache_ttl: int
    """Cache time-to-live in seconds"""

    limit: int
    """Maximum number of values to retrieve"""

    order_by: Literal["asc", "desc"]
    """Sort order for values"""


ResolvedQueryResolvedVariableAllowedValues: TypeAlias = Union[
    ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1,
    ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2,
]


class ResolvedQueryResolvedVariableConstraints(TypedDict, total=False):
    """Constraints for variable types"""

    max: Optional[float]
    """Maximum allowed value"""

    max_length: Optional[int]
    """Maximum length for STRING variables"""

    min: Optional[float]
    """Minimum allowed value"""

    step: Optional[float]
    """Step increment for numeric input"""


class ResolvedQueryResolvedVariable(TypedDict, total=False):
    """A variable definition with its bound value"""

    bound_value: Required[Union[str, float, bool]]
    """The concrete value bound for this resolution"""

    default: Required[Union[str, float, bool]]
    """Default value for this variable"""

    name: Required[str]
    """Variable name identifier"""

    type: Required[
        Literal["STRING", "INT", "FLOAT", "DATE", "TIMESTAMP", "BOOL", "DIMENSION", "MEASURE", "CALCULATION", "FILTER"]
    ]
    """Data type of the variable"""

    allowed_values: Optional[ResolvedQueryResolvedVariableAllowedValues]
    """Allowed values configuration"""

    constraints: Optional[ResolvedQueryResolvedVariableConstraints]
    """Constraints for variable types"""

    description: Optional[str]
    """Description of the variable's purpose"""

    is_default: Optional[bool]
    """True if bound_value equals the default value"""

    label: Optional[str]
    """Human-readable label for the variable"""


class ResolvedQuery(TypedDict, total=False):
    """Previously resolved query object from /resolve"""

    kater_id: Required[str]
    """Unique identifier for this resolved query instance"""

    name: Required[str]
    """Name from the leaf query in the inheritance chain"""

    source_query: Required[str]
    """Reference to the original query template this was resolved from"""

    topic: Required[str]
    """
    Reference to the topic this query uses (always known after inheritance
    resolution)
    """

    ai_context: Optional[str]
    """Usage guidance for AI processing"""

    calculations: Optional[SequenceNotStr[ResolvedQueryCalculation]]
    """Merged required + selected optional calculations"""

    chart_hints: Optional[Iterable[ResolvedQueryChartHint]]
    """Chart recommendations preserved for evaluation"""

    custom_properties: Optional[Dict[str, object]]
    """Custom properties"""

    description: Optional[str]
    """Description of the query"""

    dimensions: Optional[SequenceNotStr[ResolvedQueryDimension]]
    """Merged required + selected optional dimensions"""

    filters: Optional[SequenceNotStr[ResolvedQueryFilter]]
    """Merged required + selected optional filters"""

    inheritance_chain: Optional[SequenceNotStr[str]]
    """Ordered list of query refs that were merged during inheritance resolution"""

    label: Optional[str]
    """Human-readable label with var() values substituted"""

    limit: Optional[int]
    """Maximum number of rows to return"""

    measures: Optional[SequenceNotStr[ResolvedQueryMeasure]]
    """Merged required + selected optional measures"""

    order_by: Optional[ResolvedQueryOrderBy]
    """Sort order specification for query results.

    Use desc for descending (highest/newest first) and asc for ascending
    (lowest/oldest first).
    """

    required_access_grants: Optional[SequenceNotStr[str]]
    """Access grants required to use this query"""

    resolved_chart: Optional[ResolvedQueryResolvedChart]
    """The matched chart recommendation after evaluating chart hints"""

    resolved_variables: Optional[Iterable[ResolvedQueryResolvedVariable]]
    """Full variable definitions with bound values"""

    widget_category: Optional[Literal["axis", "pie", "single_value", "heatmap", "table", "static"]]
    """Category of widget that determines data shape constraints for queries"""
