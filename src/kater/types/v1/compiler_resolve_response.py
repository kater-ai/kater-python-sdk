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
    "ResolvedQueryFilterInlineFieldFilter",
    "ResolvedQueryFilterInlineExistsFilter1",
    "ResolvedQueryFilterInlineExistsFilter2",
    "ResolvedQueryMeasure",
    "ResolvedQueryOrderBy",
    "ResolvedQueryResolvedChart",
    "ResolvedQueryResolvedVariable",
    "ResolvedQueryResolvedVariableAllowedValues",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues1Static",
    "ResolvedQueryResolvedVariableAllowedValuesVariableAllowedValues2",
    "ResolvedQueryResolvedVariableConstraints",
    "ResolvedQuerySelectFrom",
    "ResolvedQuerySelectFromOutputColumn",
    "DependencyGraph",
    "DependencyGraphNodes",
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


class ResolvedQueryFilterInlineFieldFilter(BaseModel):
    """An inline filter using field + operator + values"""

    field: str
    """Reference to the field to filter on"""

    name: str
    """Name of the inline filter"""

    operator: Literal[
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
    """Filter operator to apply"""

    sql_value: Optional[str] = None
    """SQL expression for the filter value"""

    static_values: Optional[List[Union[str, float, bool]]] = None
    """Fixed values for the filter"""


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
    ResolvedQueryFilterInlineFieldFilter,
    str,
    ResolvedQueryFilterInlineExistsFilter1,
    ResolvedQueryFilterInlineExistsFilter2,
]

ResolvedQueryMeasure: TypeAlias = Union[RefWithLabel, InlineField, str]


class ResolvedQueryOrderBy(BaseModel):
    """Sort order specification for query results.

    Use desc for descending (highest/newest first) and asc for ascending (lowest/oldest first).
    """

    asc: Optional[List[str]] = None
    """Fields to sort in ascending order (lowest/oldest first)"""

    desc: Optional[List[str]] = None
    """Fields to sort in descending order (highest/newest first)"""


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

    bound_value: Union[str, float, bool]
    """The concrete value bound for this resolution"""

    default: Union[str, float, bool]
    """Default value for this variable"""

    name: str
    """Variable name identifier"""

    type: Literal[
        "STRING", "INT", "FLOAT", "DATE", "TIMESTAMP", "BOOL", "DIMENSION", "MEASURE", "CALCULATION", "FILTER"
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

    label: Optional[str] = None
    """Human-readable label for the variable"""


class ResolvedQuerySelectFromOutputColumn(BaseModel):
    """A column produced by a select_from CTE"""

    column_alias: str
    """The SQL column alias in the CTE output"""

    field_name: str
    """The field name used in q:query_name.field_name references"""

    source_type: Literal["dimension", "measure", "calculation"]
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

    widget_category: Literal["axis", "pie", "single_value", "heatmap", "table", "static"]
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
                "kpi_card",
                "line_chart",
                "bar_chart",
                "pie_chart",
                "donut_chart",
                "area_chart",
                "scatter_chart",
                "data_table",
                "card_grid",
                "heatmap",
                "gauge",
                "text",
                "image",
                "styled_table",
                "stat_cards",
                "key_value_list",
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

    order_by: Optional[ResolvedQueryOrderBy] = None
    """Sort order specification for query results.

    Use desc for descending (highest/newest first) and asc for ascending
    (lowest/oldest first).
    """

    required_access_grants: Optional[List[str]] = None
    """Access grants required to use this query"""

    resolved_chart: Optional[ResolvedQueryResolvedChart] = None
    """The matched chart recommendation after evaluating chart hints"""

    resolved_variables: Optional[List[ResolvedQueryResolvedVariable]] = None
    """Full variable definitions with bound values"""

    select_from: Optional[List[ResolvedQuerySelectFrom]] = None
    """Resolved select_from entries with CTE metadata"""


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


class CompilerResolveResponse(BaseModel):
    """Response model for a resolved query."""

    resolved_query: ResolvedQuery
    """The fully resolved query object"""

    dependency_graph: Optional[DependencyGraph] = None
    """Dependency graph between schema objects."""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""
