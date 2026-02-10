# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "CompilerResolveResponse",
    "ResolvedQuery",
    "ResolvedQueryCalculation",
    "ResolvedQueryCalculationRefWithLabel",
    "ResolvedQueryCalculationInlineField",
    "ResolvedQueryChartHint",
    "ResolvedQueryChartHintChartHint1",
    "ResolvedQueryChartHintChartHint1Config",
    "ResolvedQueryChartHintChartHint2Output",
    "ResolvedQueryChartHintChartHint2OutputDefault",
    "ResolvedQueryChartHintChartHint2OutputDefaultConfig",
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
    "DependencyGraph",
    "DependencyGraphNodes",
    "Manifest",
    "ManifestObjects",
]


class ResolvedQueryCalculationRefWithLabel(BaseModel):
    """A reference with optional label override"""

    ref: str
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str] = None
    """Optional label override for this reference"""


class ResolvedQueryCalculationInlineField(BaseModel):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: str
    """Unique identifier for this inline field"""

    name: str
    """Name of the inline field"""

    sql: str
    """SQL expression for the field"""

    label: Optional[str] = None
    """Human-readable label"""


ResolvedQueryCalculation: TypeAlias = Union[
    ResolvedQueryCalculationRefWithLabel, ResolvedQueryCalculationInlineField, str
]


class ResolvedQueryChartHintChartHint1Config(BaseModel):
    """Chart configuration with variable references"""

    color_by: Optional[str] = None
    """Field or variable reference for color grouping"""

    size: Optional[str] = None
    """Field or variable reference for size"""

    stack_by: Optional[str] = None
    """Field or variable reference for stacking"""

    x_axis: Optional[str] = None
    """Field or variable reference for x-axis"""

    y_axis: Optional[str] = None
    """Field or variable reference for y-axis"""


class ResolvedQueryChartHintChartHint1(BaseModel):
    """A chart recommendation rule"""

    config: ResolvedQueryChartHintChartHint1Config
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


class ResolvedQueryChartHintChartHint2OutputDefaultConfig(BaseModel):
    """Chart configuration with variable references"""

    color_by: Optional[str] = None
    """Field or variable reference for color grouping"""

    size: Optional[str] = None
    """Field or variable reference for size"""

    stack_by: Optional[str] = None
    """Field or variable reference for stacking"""

    x_axis: Optional[str] = None
    """Field or variable reference for x-axis"""

    y_axis: Optional[str] = None
    """Field or variable reference for y-axis"""


class ResolvedQueryChartHintChartHint2OutputDefault(BaseModel):
    config: ResolvedQueryChartHintChartHint2OutputDefaultConfig
    """Chart configuration with variable references"""

    recommend: Literal[
        "line", "bar", "stacked_bar", "area", "pie", "donut", "scatter", "table", "heatmap", "single_value"
    ]
    """Type of chart visualization"""


class ResolvedQueryChartHintChartHint2Output(BaseModel):
    """A chart recommendation rule"""

    default: ResolvedQueryChartHintChartHint2OutputDefault


ResolvedQueryChartHint: TypeAlias = Union[ResolvedQueryChartHintChartHint1, ResolvedQueryChartHintChartHint2Output]


class ResolvedQueryDimensionRefWithLabel(BaseModel):
    """A reference with optional label override"""

    ref: str
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str] = None
    """Optional label override for this reference"""


class ResolvedQueryDimensionInlineField(BaseModel):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: str
    """Unique identifier for this inline field"""

    name: str
    """Name of the inline field"""

    sql: str
    """SQL expression for the field"""

    label: Optional[str] = None
    """Human-readable label"""


ResolvedQueryDimension: TypeAlias = Union[ResolvedQueryDimensionRefWithLabel, ResolvedQueryDimensionInlineField, str]


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


class ResolvedQueryFilterInlineExistsFilter1Exists(BaseModel):
    """EXISTS subquery condition"""

    from_: str = FieldInfo(alias="from")
    """Reference to the source view/table for the subquery"""

    where: List[str]
    """WHERE conditions for the subquery"""


class ResolvedQueryFilterInlineExistsFilter1NotExists(BaseModel):
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    from_: str = FieldInfo(alias="from")
    """Reference to the source view/table for the subquery"""

    where: List[str]
    """WHERE conditions for the subquery"""


class ResolvedQueryFilterInlineExistsFilter1(BaseModel):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    exists: ResolvedQueryFilterInlineExistsFilter1Exists
    """EXISTS subquery condition"""

    name: str
    """Name of the inline filter"""

    description: Optional[str] = None
    """Description of the filter"""

    label: Optional[str] = None
    """Human-readable label"""

    not_exists: Optional[ResolvedQueryFilterInlineExistsFilter1NotExists] = None
    """A subquery condition for EXISTS/NOT EXISTS filters"""


class ResolvedQueryFilterInlineExistsFilter2NotExists(BaseModel):
    """NOT EXISTS subquery condition"""

    from_: str = FieldInfo(alias="from")
    """Reference to the source view/table for the subquery"""

    where: List[str]
    """WHERE conditions for the subquery"""


class ResolvedQueryFilterInlineExistsFilter2Exists(BaseModel):
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    from_: str = FieldInfo(alias="from")
    """Reference to the source view/table for the subquery"""

    where: List[str]
    """WHERE conditions for the subquery"""


class ResolvedQueryFilterInlineExistsFilter2(BaseModel):
    """An inline filter using EXISTS or NOT EXISTS with a subquery"""

    name: str
    """Name of the inline filter"""

    not_exists: ResolvedQueryFilterInlineExistsFilter2NotExists
    """NOT EXISTS subquery condition"""

    description: Optional[str] = None
    """Description of the filter"""

    exists: Optional[ResolvedQueryFilterInlineExistsFilter2Exists] = None
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    label: Optional[str] = None
    """Human-readable label"""


ResolvedQueryFilter: TypeAlias = Union[
    ResolvedQueryFilterInlineFieldFilter,
    str,
    ResolvedQueryFilterInlineExistsFilter1,
    ResolvedQueryFilterInlineExistsFilter2,
]


class ResolvedQueryMeasureRefWithLabel(BaseModel):
    """A reference with optional label override"""

    ref: str
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str] = None
    """Optional label override for this reference"""


class ResolvedQueryMeasureInlineField(BaseModel):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: str
    """Unique identifier for this inline field"""

    name: str
    """Name of the inline field"""

    sql: str
    """SQL expression for the field"""

    label: Optional[str] = None
    """Human-readable label"""


ResolvedQueryMeasure: TypeAlias = Union[ResolvedQueryMeasureRefWithLabel, ResolvedQueryMeasureInlineField, str]


class ResolvedQueryOrderBy(BaseModel):
    """Sort order specification for query results.

    Use desc for descending (highest/newest first) and asc for ascending (lowest/oldest first).
    """

    asc: Optional[List[str]] = None
    """Fields to sort in ascending order (lowest/oldest first)"""

    desc: Optional[List[str]] = None
    """Fields to sort in descending order (highest/newest first)"""


class ResolvedQueryResolvedChartConfig(BaseModel):
    """Chart configuration"""

    color_by: Optional[str] = None
    """Field or variable reference for color grouping"""

    size: Optional[str] = None
    """Field or variable reference for size"""

    stack_by: Optional[str] = None
    """Field or variable reference for stacking"""

    x_axis: Optional[str] = None
    """Field or variable reference for x-axis"""

    y_axis: Optional[str] = None
    """Field or variable reference for y-axis"""


class ResolvedQueryResolvedChart(BaseModel):
    """The matched chart recommendation after evaluating chart hints"""

    config: ResolvedQueryResolvedChartConfig
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

    widget_category: Optional[Literal["axis", "pie", "single_value", "heatmap", "table", "static"]] = None
    """Category of widget that determines data shape constraints for queries"""


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


class DependencyGraph(BaseModel):
    """Dependency graph between schema objects."""

    edges: Dict[str, Dict[str, List[str]]]
    """Edge relationships with UUID string keys"""

    nodes: Dict[str, DependencyGraphNodes]
    """UUID string to node mapping"""


class ManifestObjects(BaseModel):
    """A single object entry in the manifest."""

    kater_id: str

    name: str

    type: str

    label: Optional[str] = None

    parent_id: Optional[str] = None

    source_file: Optional[str] = None


class Manifest(BaseModel):
    """Compilation manifest with all named objects."""

    generated_at: str

    objects: Dict[str, ManifestObjects]

    schema_version: Optional[str] = None


class CompilerResolveResponse(BaseModel):
    """Response model for a resolved query."""

    resolved_query: ResolvedQuery
    """The fully resolved query object"""

    dependency_graph: Optional[DependencyGraph] = None
    """Dependency graph between schema objects."""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""
