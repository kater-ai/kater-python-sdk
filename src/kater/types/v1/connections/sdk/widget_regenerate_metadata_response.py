# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = [
    "WidgetRegenerateMetadataResponse",
    "CanonicalPostQueryState",
    "CanonicalPostQueryStateFilter",
    "CanonicalPostQueryStateFilterField",
    "CanonicalPostQueryStateFilterFieldModifier",
    "CanonicalPostQueryStateFilterDefaultValue",
    "CanonicalPostQueryStateFilterDefaultValueDateRangeValue",
    "CanonicalPostQueryStateFilterDefaultValueNumberRangeValue",
    "CanonicalPostQueryStateFilterValues",
    "CanonicalPostQueryStateSort",
    "CanonicalPostQueryStateSortField",
    "CanonicalPostQueryStateSortFieldModifier",
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
    "ResultScope",
]


class CanonicalPostQueryStateFilterFieldModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class CanonicalPostQueryStateFilterField(BaseModel):
    """Field target using object form with ref and optional modifiers"""

    ref: str
    """Reference to the field"""

    modifiers: Optional[List[CanonicalPostQueryStateFilterFieldModifier]] = None
    """Optional modifiers for the field (e.g. timeframe)"""


class CanonicalPostQueryStateFilterDefaultValueDateRangeValue(BaseModel):
    """Date range filter value"""

    mode: Literal["absolute_range", "relative_range"]


class CanonicalPostQueryStateFilterDefaultValueNumberRangeValue(BaseModel):
    """Number range filter value"""

    max: float
    """Maximum value (inclusive)"""

    min: float
    """Minimum value (inclusive)"""


CanonicalPostQueryStateFilterDefaultValue: TypeAlias = Union[
    str,
    float,
    bool,
    List[Union[str, float, bool]],
    CanonicalPostQueryStateFilterDefaultValueDateRangeValue,
    CanonicalPostQueryStateFilterDefaultValueNumberRangeValue,
    None,
]


class CanonicalPostQueryStateFilterValues(BaseModel):
    """Values source configuration for categorical filters"""

    source: Literal["result_distinct"]
    """Source of filter values"""

    limit: Optional[int] = None
    """Maximum number of values to show"""

    searchable: Optional[bool] = None
    """Whether the filter should be searchable"""

    sort: Optional[Literal["asc", "desc"]] = None
    """Sort order for values"""


class CanonicalPostQueryStateFilter(BaseModel):
    """A post-query filter definition for a specific field occurrence"""

    expression: Literal["equals", "in", "between"]
    """Filter expression operator"""

    field: CanonicalPostQueryStateFilterField
    """Field target using object form with ref and optional modifiers"""

    kind: Literal["date", "dropdown", "multiselect", "number_range"]
    """Filter kind that determines UI control type"""

    default_enabled: Optional[bool] = None
    """Whether this filter should be enabled by default"""

    default_value: Optional[CanonicalPostQueryStateFilterDefaultValue] = None
    """Default value for the filter when enabled"""

    values: Optional[CanonicalPostQueryStateFilterValues] = None
    """Values source configuration for categorical filters"""


class CanonicalPostQueryStateSortFieldModifier(BaseModel):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Literal["timeframe"]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: str
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class CanonicalPostQueryStateSortField(BaseModel):
    """Field target using object form with ref and optional modifiers"""

    ref: str
    """Reference to the field"""

    modifiers: Optional[List[CanonicalPostQueryStateSortFieldModifier]] = None
    """Optional modifiers for the field (e.g. timeframe)"""


class CanonicalPostQueryStateSort(BaseModel):
    """A post-query sort definition for a specific field occurrence"""

    field: CanonicalPostQueryStateSortField
    """Field target using object form with ref and optional modifiers"""

    default_direction: Optional[Literal["asc", "desc"]] = None
    """Default sort direction when enabled"""

    default_enabled: Optional[bool] = None
    """Whether this sort should be enabled by default"""

    priority: Optional[int] = None
    """Sort priority for multi-field sorts (lower numbers sort first)"""


class CanonicalPostQueryState(BaseModel):
    """
    Schema for post-query refinements that run after SQL execution on returned result rows
    """

    filters: Optional[List[CanonicalPostQueryStateFilter]] = None
    """Post-query filter definitions that apply to returned result rows"""

    sorts: Optional[List[CanonicalPostQueryStateSort]] = None
    """Post-query sort definitions that apply to returned result rows"""


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


class ResultScope(BaseModel):
    """Scope metadata for post-query transformation results."""

    base_row_count: int
    """Number of base rows before post-query transformation"""

    has_more: bool
    """Whether more rows are available beyond the current set"""

    is_row_limited: bool
    """Whether the result is limited by row count restrictions"""

    scope: str
    """Scope of transformation: 'available_rows', etc."""

    transformed_row_count: int
    """Number of rows after post-query transformation"""


class WidgetRegenerateMetadataResponse(BaseModel):
    """Response from post-query mutation endpoints."""

    auto_description: Optional[str] = None
    """Auto-generated description text"""

    auto_description_structured: Optional[Dict[str, object]] = None
    """Auto-generated structured description"""

    auto_title: Optional[str] = None
    """Auto-generated title"""

    canonical_post_query_state: Optional[CanonicalPostQueryState] = None
    """
    Schema for post-query refinements that run after SQL execution on returned
    result rows
    """

    footnote: Optional[str] = None
    """Auto-generated footnote text"""

    footnote_structured: Optional[Dict[str, object]] = None
    """Auto-generated structured footnote"""

    insight_runs: Optional[List[InsightRun]] = None
    """Regenerated insight runs for transformed data"""

    post_query_key_id: Optional[str] = None
    """Deterministic hash for narrative caching (null for unavailable)"""

    post_query_state_id: Optional[str] = None
    """Saved post-query state ID (null for unavailable responses)"""

    reason: Optional[str] = None
    """Reason for unavailable status"""

    result_scope: Optional[ResultScope] = None
    """Scope metadata for post-query transformation results."""

    revision: Optional[int] = None
    """Current revision number (null for unavailable responses)"""

    status: Optional[str] = None
    """Status for error cases ('unavailable', null for success)"""
