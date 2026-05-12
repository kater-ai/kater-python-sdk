# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = [
    "CompilerExecuteResponse",
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


class ColumnMap(BaseModel):
    """Maps a UUID column alias to its human-readable name and type."""

    data_type: ColumnMapDataType
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

    field_type: Literal["dimension", "measure", "calculation"]

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

    field_type: Literal["dimension", "measure", "calculation"]

    kater_id: str


class RenderedQueryKeyCanonicalFieldsOutputColumn(BaseModel):
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


class RenderedQueryKeyCanonicalFieldsSelectedField(BaseModel):
    """A selected/active source field entry — strict subset of the field item."""

    active_timeframe: Optional[str] = None

    field_type: Literal["dimension", "measure", "calculation"]

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


class CompilerExecuteResponse(BaseModel):
    """Execute-stage projection from ``RenderResponse`` (Story 2.1 frozen dataclass).

    Has NO ``combination`` / ``combination_id`` field by contract. Carries
    every field the legacy ``ExecuteResponse`` exposes so consumer
    migrations swap legacy → structured with no response-handling changes.
    """

    success: bool
    """Whether execution succeeded"""

    applied_filter_state: Optional[List[AppliedFilterState]] = None
    """Applied runtime filter state used for execution."""

    auto_description: Optional[str] = None
    """Auto-generated description text."""

    auto_title: Optional[str] = None
    """Auto-generated title."""

    cache_hit: Optional[bool] = None
    """Whether the result was served from cache."""

    column_map: Optional[List[ColumnMap]] = None
    """Column metadata for the executed query's output."""

    data: Optional[List[Dict[str, object]]] = None
    """Query result rows."""

    dialect: Optional[str] = None
    """SQL dialect used."""

    errors: Optional[List[CompilerErrorItem]] = None
    """Compilation/execution errors (if any)."""

    execution_time_ms: Optional[float] = None
    """Total execution duration in milliseconds."""

    is_row_limited: Optional[bool] = None
    """True when the app-wide row limit was applied."""

    rendered_query_key: Optional[RenderedQueryKey] = None
    """Top-level natural key returned by every runtime data and widget path.

    Format invariants (validation enforced by Story 1.2's hashing helpers):

    - `key_id`: `rqk_v1:<64 lowercase hex chars>`
    - `exact_cache_key_id`: `rqk_cache_exact_v1:<64 lowercase hex chars>`
    - `aggregate_cache_key_id`: `rqk_cache_agg_v1:<64 lowercase hex chars>` or null
    """

    row_count: Optional[int] = None
    """Total rows returned by the executed query."""

    sql: Optional[str] = None
    """Generated SQL statement."""

    style_config: Optional[Dict[str, object]] = None
    """Resolved style config."""

    widget_config: Optional[Dict[str, object]] = None
    """Resolved widget config."""

    widget_type: Optional[str] = None
    """Resolved widget type."""
