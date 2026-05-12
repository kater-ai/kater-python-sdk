# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "CapabilityCreateResponse",
    "Query",
    "QueryWidgetConstraints",
    "QueryWidgetConstraintsConstraints",
    "QueryWidgetConstraintsConstraintsDimensions",
    "QueryWidgetConstraintsConstraintsMetrics",
    "QueryDefaultFilterState",
    "QueryDefaultFilterStateValue",
    "QueryDefaultFilterStateValueScalarFilterValue",
    "QueryDefaultFilterStateValueMultiFilterValue",
    "QueryDefaultFilterStateValueNumberRangeFilterValue",
    "QueryDefaultFilterStateValueAbsoluteDateFilterValue",
    "QueryDefaultFilterStateValueAbsoluteRangeFilterValue",
    "QueryDefaultFilterStateValueRelativeRangeFilterValue",
    "QueryDefaultFilterStateValueRelativeRangeFilterValueEnd",
    "QueryDefaultFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "QueryDefaultFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "QueryDefaultFilterStateValueRelativeRangeFilterValueStart",
    "QueryDefaultFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "QueryDefaultFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "QueryDefaultFilterStateValuePresetReferenceFilterValue",
    "QueryDefaultFilterStateValueNullFilterValue",
    "QueryFilterDefinition",
    "QuerySelectableField",
    "QuerySelectableFieldDataType",
    "QuerySelectableFieldDataTypeExtension",
    "QueryVariableDefinition",
]


class QueryWidgetConstraintsConstraintsDimensions(BaseModel):
    """Dimension constraint with optional semantic flags."""

    max: Optional[int] = None

    min: int

    excludes_datetime_dimension: Optional[bool] = None

    max_cardinality: Optional[int] = None

    requires_categorical: Optional[bool] = None

    requires_datetime_dimension: Optional[bool] = None


class QueryWidgetConstraintsConstraintsMetrics(BaseModel):
    """Numeric min/max range constraint."""

    max: Optional[int] = None

    min: int


class QueryWidgetConstraintsConstraints(BaseModel):
    """Per-widget-type constraints sourced from the widget category mapping"""

    calculations_allowed: bool

    dimensions: QueryWidgetConstraintsConstraintsDimensions
    """Dimension constraint with optional semantic flags."""

    metrics: QueryWidgetConstraintsConstraintsMetrics
    """Numeric min/max range constraint."""

    requires_calculation: Optional[bool] = None


class QueryWidgetConstraints(BaseModel):
    """Widget category and per-widget-type constraints scoped to this query"""

    constraints: QueryWidgetConstraintsConstraints
    """Per-widget-type constraints sourced from the widget category mapping"""

    widget_category: str
    """Widget category name (matches WidgetCategoryMapping keys)"""


class QueryDefaultFilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

    mode: Optional[Literal["scalar"]] = None


class QueryDefaultFilterStateValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class QueryDefaultFilterStateValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class QueryDefaultFilterStateValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class QueryDefaultFilterStateValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class QueryDefaultFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class QueryDefaultFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


QueryDefaultFilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    QueryDefaultFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    QueryDefaultFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class QueryDefaultFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class QueryDefaultFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


QueryDefaultFilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    QueryDefaultFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    QueryDefaultFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class QueryDefaultFilterStateValueRelativeRangeFilterValue(BaseModel):
    end: QueryDefaultFilterStateValueRelativeRangeFilterValueEnd

    start: QueryDefaultFilterStateValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class QueryDefaultFilterStateValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class QueryDefaultFilterStateValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


QueryDefaultFilterStateValue: TypeAlias = Union[
    QueryDefaultFilterStateValueScalarFilterValue,
    QueryDefaultFilterStateValueMultiFilterValue,
    QueryDefaultFilterStateValueNumberRangeFilterValue,
    QueryDefaultFilterStateValueAbsoluteDateFilterValue,
    QueryDefaultFilterStateValueAbsoluteRangeFilterValue,
    QueryDefaultFilterStateValueRelativeRangeFilterValue,
    QueryDefaultFilterStateValuePresetReferenceFilterValue,
    QueryDefaultFilterStateValueNullFilterValue,
    None,
]


class QueryDefaultFilterState(BaseModel):
    effective_kater_id: str
    """Stable effective runtime filter ID"""

    enabled: Optional[bool] = None
    """Requested enabled state override for this effective filter"""

    value: Optional[QueryDefaultFilterStateValue] = None
    """Requested runtime value override for this effective filter"""


class QueryFilterDefinition(BaseModel):
    """Effective filter definition exposed via capabilities.

    This is a deliberate subset of the API-layer `FilterDefinitionResponse`
    shape, not a full mirror. The capabilities surface is intentionally
    decoupled so `packages/core` does not depend on `apps/api`, and so the
    JSON schema stays flat. Fields the capabilities surface omits include
    expressive value payloads (`static_value`, `default_value`, `values`,
    `presets`), AI-assistance metadata (`ai_context`), null-handling hints
    (`allow_null_value`, `null_label`), and UI placeholder/help strings;
    consumers that need those should fetch them from the API model. The
    fields included here are sufficient for capabilities-driven UI and
    request construction. Identity is `kater_id` (UUID); the legacy
    name-based `field` ref is replaced with `field_kater_id`.
    """

    data_type: str
    """Canonical data type"""

    effective_kater_id: str
    """Stable effective runtime filter ID (UUID)"""

    expression: str
    """Structured filter expression (operator literal)"""

    kater_id: str
    """Concrete declaration ID from the merged definition"""

    mode: Literal["static", "parameterized"]
    """Filter mode"""

    name: str
    """Logical filter name"""

    required: bool
    """Whether the filter is always active"""

    scope: Literal["model", "topic", "dashboard", "query"]
    """Filter scope"""

    declaration_kater_ids: Optional[List[str]] = None
    """Concrete declaration IDs (UUIDs) that contributed to this effective filter"""

    default_enabled: Optional[bool] = None
    """Default enabled state at runtime"""

    description: Optional[str] = None
    """Free-form filter description"""

    field_kater_id: Optional[str] = None
    """Field UUID this filter targets (when the filter binds to a field)"""

    kind: Optional[str] = None
    """Interactive filter kind (date, dropdown, etc.)"""

    label: Optional[str] = None
    """Display label"""

    owner_chain: Optional[List[str]] = None
    """Owner UUIDs from model/topic/dashboard/query precedence order"""


class QuerySelectableFieldDataTypeExtension(BaseModel):
    """Vendor-specific type extension"""

    engine: str
    """Database engine/dialect"""

    orig_type: str
    """Original type name in the source database"""

    options: Optional[Dict[str, object]] = None
    """Additional vendor-specific options"""

    raw_ddl: Optional[str] = None
    """Raw DDL for the type"""


class QuerySelectableFieldDataType(BaseModel):
    """Canonical data type for this field"""

    kind: Literal["Bool", "Text", "Number", "Datetime", "Complex", "Unknown"]
    """The canonical data type kind"""

    nullable: bool
    """Whether the field can be null"""

    extension: Optional[QuerySelectableFieldDataTypeExtension] = None
    """Vendor-specific type extension"""

    params: Optional[object] = None
    """Optional coarse metadata for the canonical type"""


class QuerySelectableField(BaseModel):
    """One selectable field exposed by a query, with temporal grain metadata.

    Identity is `kater_id` (UUID). `name` is a display-only label.

    Temporal invariants (enforced by `validate_temporal_consistency`):
    - Non-temporal fields must have `available_timeframes == []` and
      `default_active_timeframe is None`.
    - Temporal fields with non-null `default_active_timeframe` must list it
      in `available_timeframes`.
    - `default_active_timeframe` is `null` when no grain default is chosen.

    See PRD section `QueryCapabilitiesResponseV1` for the canonical rules.
    """

    data_type: QuerySelectableFieldDataType
    """Canonical data type for this field"""

    default_selected: bool
    """True when the field appears in the deterministic backend default selection"""

    description: Optional[str] = None
    """Long-form description for UI tooltips"""

    field_type: Literal["dimension", "measure", "calculation"]
    """Field kind: dimension, measure, or calculation"""

    kater_id: str
    """Authored field UUID (stable identity)"""

    label: Optional[str] = None
    """Display label (may be renamed)"""

    name: str
    """Field name within the query"""

    required: bool
    """True when the field is always part of the rendered output"""

    source: Literal["query", "parent", "pinned_variant"]
    """
    Origin of the field: directly authored by the query, inherited from the parent
    query, or pinned through a query variant.
    """

    available_timeframes: Optional[
        List[Literal["raw", "date", "day", "week", "month", "quarter", "year", "day_of_week", "hour"]]
    ] = None
    """Temporal grains the field can be projected to.

    Empty for non-temporal fields. For temporal fields, includes `raw` plus authored
    timeframes in deterministic display order.
    """

    default_active_timeframe: Optional[
        Literal["raw", "date", "day", "week", "month", "quarter", "year", "day_of_week", "hour"]
    ] = None
    """Time granularity for datetime dimensions"""


class QueryVariableDefinition(BaseModel):
    """A variable's schema exposed via capabilities.

    `variable_kater_id` is preferred. Until every authoring surface exposes
    a stable variable UUID, the migration fallback identity is
    `(query_kater_id, scope, name)`. Consumers SHOULD prefer
    `variable_kater_id` and fall back only when it is `null`.
    """

    is_runtime: bool
    """
    True = dynamic (entered at run time); False = static (authored default that
    never changes at runtime).
    """

    name: str
    """Variable name within scope"""

    query_kater_id: str
    """Owning query UUID"""

    scope: Literal["query", "global"]
    """Variable scope: query-local or global"""

    type: str
    """Variable data type, e.g. STRING, INT, DATE, BOOL, STRING[], TIMEFRAME"""

    variable_kater_id: Optional[str] = None
    """Stable variable UUID.

    Fall back to (query_kater_id, scope, name) when null (migration fallback only).
    """

    allowed_values_column_kater_id: Optional[str] = None
    """Dimension column UUID for from-column variables; null otherwise"""

    allowed_values_static: Optional[List[Union[str, float, bool]]] = None
    """
    Static enumeration of allowed values; null when the variable is unconstrained or
    column-derived
    """

    default: Union[str, float, bool, List[Union[str, float, bool]], None] = None
    """Authored default value"""

    description: Optional[str] = None
    """Free-form description"""

    label: Optional[str] = None
    """Display label"""


class Query(BaseModel):
    """Capabilities for a single query.

    Identical payload whether served over HTTP (one entry of
    `QueryCapabilitiesResponseV1.queries`) or written to disk (one value of
    `QueryCapabilitiesArtifact.queries`).

    Identity uses `kater_id` (UUID) throughout; `query_ref` is a provenance
    label for human inspection only.
    """

    query_kater_id: str
    """Owning query UUID (stable identity)"""

    query_label: Optional[str] = None
    """Display label for the query"""

    query_ref: str
    """Authored ref string (e.g. `q:compliance_rate`); provenance only, not identity"""

    widget_category: str
    """Widget category name"""

    widget_constraints: QueryWidgetConstraints
    """Widget category and per-widget-type constraints scoped to this query"""

    default_filter_state: Optional[List[QueryDefaultFilterState]] = None
    """Default runtime filter state to seed `RenderedQueryRequestV1.filter_state`"""

    default_selected_field_ids: Optional[List[str]] = None
    """
    Field UUIDs that the backend selects by default when a consumer omits
    `field_selection.selected_field_ids`. Typically empty (required fields cover the
    base render); non-empty when the team wants to highlight an optional dimension
    or measure.
    """

    filter_definitions: Optional[List[QueryFilterDefinition]] = None
    """Effective filter definitions in scope for this query"""

    required_field_ids: Optional[List[str]] = None
    """Field UUIDs that the backend always includes in the rendered output.

    Replaces the legacy enumerate `required_fields` name list.
    """

    selectable_fields: Optional[List[QuerySelectableField]] = None
    """All fields a consumer can select, including required ones.

    Ordering is deterministic: authoring order, then `kater_id` lex (matches NFR5).
    """

    variable_definitions: Optional[List[QueryVariableDefinition]] = None
    """Variable definitions for the query (flat list, not name-keyed dict)"""


class CapabilityCreateResponse(BaseModel):
    """Response shape for `POST /api/v1/compiler/capabilities`.

    Replaces `EnumerateResponse.combinations`; consumers build
    `RenderedQueryRequestV1.field_selection` from `selectable_fields` plus
    `default_selected_field_ids` instead of enumerating combinations.
    """

    connection_id: str
    """Connection identifier (UUID or canonical key)"""

    queries: Optional[List[Query]] = None
    """Capabilities for each query in the connection.

    Outer ordering is deterministic (by `query_kater_id` UUID lex order); the
    per-query payload is identical to the on-disk artifact.
    """
