# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .chart_config_param import ChartConfigParam
from .inline_field_param import InlineFieldParam
from .ref_with_label_param import RefWithLabelParam
from .subquery_condition_param import SubqueryConditionParam

__all__ = [
    "CompilerExecuteParams",
    "ResolvedQuery",
    "ResolvedQueryCalculation",
    "ResolvedQueryChartHint",
    "ResolvedQueryChartHintChartHint1Input",
    "ResolvedQueryChartHintChartHint2Input",
    "ResolvedQueryChartHintChartHint2InputDefault",
    "ResolvedQueryDimension",
    "ResolvedQueryFilter",
    "ResolvedQueryFilterInlineFormulaFilter",
    "ResolvedQueryFilterInlineExistsFilter1",
    "ResolvedQueryFilterInlineExistsFilter2",
    "ResolvedQueryMeasure",
    "ResolvedQueryOrderBy",
    "ResolvedQueryResolvedChart",
    "ResolvedQueryResolvedVariable",
    "ResolvedQueryResolvedVariableBoundValue",
    "ResolvedQueryResolvedVariableBoundValueRelativeDateDefault",
    "ResolvedQueryResolvedVariableDefault",
    "ResolvedQueryResolvedVariableDefaultRelativeDateDefault",
    "ResolvedQueryResolvedVariableAllowedValues",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2",
    "ResolvedQueryResolvedVariableConstraints",
    "ResolvedQuerySelectFrom",
    "ResolvedQuerySelectFromOutputColumn",
]


class CompilerExecuteParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection to execute against"""

    resolved_query: Required[ResolvedQuery]
    """Previously resolved query object from /resolve"""

    source: Optional[str]

    tenant_key: Optional[str]
    """Tenant key for multi-tenant execution"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]


ResolvedQueryCalculation: TypeAlias = Union[RefWithLabelParam, InlineFieldParam, str]


class ResolvedQueryChartHintChartHint1Input(TypedDict, total=False):
    """A chart recommendation rule"""

    config: Required[ChartConfigParam]
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


class ResolvedQueryChartHintChartHint2InputDefault(TypedDict, total=False):
    config: Required[ChartConfigParam]
    """Chart configuration with variable references"""

    recommend: Required[
        Literal["line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"]
    ]
    """Type of chart visualization"""


class ResolvedQueryChartHintChartHint2Input(TypedDict, total=False):
    """A chart recommendation rule"""

    default: Required[ResolvedQueryChartHintChartHint2InputDefault]


ResolvedQueryChartHint: TypeAlias = Union[ResolvedQueryChartHintChartHint1Input, ResolvedQueryChartHintChartHint2Input]

ResolvedQueryDimension: TypeAlias = Union[RefWithLabelParam, InlineFieldParam, str]


class ResolvedQueryFilterInlineFormulaFilter(TypedDict, total=False):
    """An inline filter using a SQL/expression formula."""

    name: Required[str]
    """Name of the inline filter"""

    sql: Required[str]
    """SQL expression for the filter condition"""


class ResolvedQueryFilterInlineExistsFilter1(TypedDict, total=False):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    exists: Required[SubqueryConditionParam]
    """EXISTS subquery condition"""

    name: Required[str]
    """Name of the inline filter"""

    description: Optional[str]
    """Description of the filter"""

    label: Optional[str]
    """Human-readable label"""

    not_exists: Optional[SubqueryConditionParam]
    """A subquery condition for EXISTS/NOT EXISTS filters"""


class ResolvedQueryFilterInlineExistsFilter2(TypedDict, total=False):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    name: Required[str]
    """Name of the inline filter"""

    not_exists: Required[SubqueryConditionParam]
    """NOT EXISTS subquery condition"""

    description: Optional[str]
    """Description of the filter"""

    exists: Optional[SubqueryConditionParam]
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    label: Optional[str]
    """Human-readable label"""


ResolvedQueryFilter: TypeAlias = Union[
    ResolvedQueryFilterInlineFormulaFilter,
    str,
    ResolvedQueryFilterInlineExistsFilter1,
    ResolvedQueryFilterInlineExistsFilter2,
]

ResolvedQueryMeasure: TypeAlias = Union[RefWithLabelParam, InlineFieldParam, str]


class ResolvedQueryOrderBy(TypedDict, total=False):
    """Sort order specification for query results.

    Use desc for descending (highest/newest first) and asc for ascending (lowest/oldest first).
    """

    asc: Optional[SequenceNotStr[str]]
    """Fields to sort in ascending order (lowest/oldest first)"""

    desc: Optional[SequenceNotStr[str]]
    """Fields to sort in descending order (highest/newest first)"""


class ResolvedQueryResolvedChart(TypedDict, total=False):
    """The matched chart recommendation after evaluating chart hints"""

    config: Required[ChartConfigParam]
    """Chart configuration"""

    recommend: Required[
        Literal["line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"]
    ]
    """Recommended chart type"""


class ResolvedQueryResolvedVariableBoundValueRelativeDateDefault(TypedDict, total=False):
    """
    A relative date default for DATE/TIMESTAMP variables.
    Computes a concrete date relative to the current date at resolve time.
    """

    amount: Required[int]
    """Offset amount. Negative = past, positive = future (e.g., -30 = 30 days ago)"""

    unit: Required[str]
    """Time unit for the offset"""


ResolvedQueryResolvedVariableBoundValue: TypeAlias = Union[
    str,
    float,
    bool,
    SequenceNotStr[Union[str, float, bool]],
    ResolvedQueryResolvedVariableBoundValueRelativeDateDefault,
]


class ResolvedQueryResolvedVariableDefaultRelativeDateDefault(TypedDict, total=False):
    """
    A relative date default for DATE/TIMESTAMP variables.
    Computes a concrete date relative to the current date at resolve time.
    """

    amount: Required[int]
    """Offset amount. Negative = past, positive = future (e.g., -30 = 30 days ago)"""

    unit: Required[str]
    """Time unit for the offset"""


ResolvedQueryResolvedVariableDefault: TypeAlias = Union[
    str, float, bool, SequenceNotStr[Union[str, float, bool]], ResolvedQueryResolvedVariableDefaultRelativeDateDefault
]


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

    bound_value: Required[Optional[ResolvedQueryResolvedVariableBoundValue]]
    """The concrete value bound for this resolution"""

    default: Required[Optional[ResolvedQueryResolvedVariableDefault]]
    """Default value for this variable"""

    kater_id: Required[str]
    """Unique identifier for this variable"""

    name: Required[str]
    """Variable name identifier"""

    type: Required[
        Literal[
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

    is_runtime: Optional[bool]
    """True if this is a runtime variable (not resolved at compile time).

    Runtime variables have var() placeholders left in compiled SQL for literal
    substitution at execution time.
    """

    label: Optional[str]
    """Human-readable label for the variable"""


class ResolvedQuerySelectFromOutputColumn(TypedDict, total=False):
    """A column produced by a select_from CTE"""

    column_alias: Required[str]
    """The SQL column alias in the CTE output"""

    field_name: Required[str]
    """The field name used in q:query_name.field_name references"""

    source_type: Required[Literal["dimension", "dimension_date", "measure", "calculation"]]
    """Original type of the field in the source query"""


class ResolvedQuerySelectFrom(TypedDict, total=False):
    """A resolved select_from entry with CTE metadata"""

    cte_alias: Required[str]
    """CTE alias used in the WITH clause (e.g., **sf_compliance_rate**base)"""

    output_columns: Required[Iterable[ResolvedQuerySelectFromOutputColumn]]
    """Columns produced by the CTE, available as q:query_name.field_name in the parent"""

    ref: Required[str]
    """Reference to the source query"""

    variables: Optional[Dict[str, Union[str, float, bool]]]
    """Variable overrides passed to the referenced query"""


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

    widget_category: Required[Literal["axis", "funnel", "heatmap", "image", "kpi_card", "pie", "table", "text"]]
    """Widget category that determines data shape constraints"""

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

    disallowed_widget_types: Optional[
        List[
            Literal[
                "axis_metric_by_dimension",
                "axis_metric_by_dimensiondate",
                "axis_metric_by_dimensiondate_sliced_by_dimension",
                "axis_scatter_plot",
                "funnel_funnel_chart",
                "heatmap_heatmap",
                "image_image_grid",
                "image_single_image",
                "kpi_measure_with_dimension_expression",
                "kpi_measure_with_secondary_metric",
                "kpi_single_measure_compared_to_prev_period_sparkline",
                "kpi_single_value",
                "pie_pie_chart",
                "table_data_table",
                "table_fancy_subtotal_table",
                "table_key_value_list",
                "table_styled_table",
                "text_data_readout_with_sparkline",
                "text_narrative_text",
            ]
        ]
    ]
    """
    Widget types within the declared widget_category that must NOT render this query
    """

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

    select_from: Optional[Iterable[ResolvedQuerySelectFrom]]
    """Resolved select_from entries with CTE metadata"""
