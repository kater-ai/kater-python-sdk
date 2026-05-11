# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "CapabilitySampleResponse",
    "Sample",
    "SampleDashboard",
    "SampleDashboardDashboardFilterState",
    "SampleDashboardDashboardFilterStateValue",
    "SampleDashboardDashboardFilterStateValueScalarFilterValue",
    "SampleDashboardDashboardFilterStateValueMultiFilterValue",
    "SampleDashboardDashboardFilterStateValueNumberRangeFilterValue",
    "SampleDashboardDashboardFilterStateValueAbsoluteDateFilterValue",
    "SampleDashboardDashboardFilterStateValueAbsoluteRangeFilterValue",
    "SampleDashboardDashboardFilterStateValueRelativeRangeFilterValue",
    "SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEnd",
    "SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStart",
    "SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "SampleDashboardDashboardFilterStateValuePresetReferenceFilterValue",
    "SampleDashboardDashboardFilterStateValueNullFilterValue",
    "SampleFieldSelection",
    "SampleFieldSelectionTimeframeOverride",
    "SampleFilterState",
    "SampleFilterStateValue",
    "SampleFilterStateValueScalarFilterValue",
    "SampleFilterStateValueMultiFilterValue",
    "SampleFilterStateValueNumberRangeFilterValue",
    "SampleFilterStateValueAbsoluteDateFilterValue",
    "SampleFilterStateValueAbsoluteRangeFilterValue",
    "SampleFilterStateValueRelativeRangeFilterValue",
    "SampleFilterStateValueRelativeRangeFilterValueEnd",
    "SampleFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "SampleFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "SampleFilterStateValueRelativeRangeFilterValueStart",
    "SampleFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "SampleFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "SampleFilterStateValuePresetReferenceFilterValue",
    "SampleFilterStateValueNullFilterValue",
    "SamplePresentation",
    "SampleResultWindow",
    "SampleTemporal",
    "SampleVariable",
]


class SampleDashboardDashboardFilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

    mode: Optional[Literal["scalar"]] = None


class SampleDashboardDashboardFilterStateValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class SampleDashboardDashboardFilterStateValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class SampleDashboardDashboardFilterStateValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class SampleDashboardDashboardFilterStateValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class SampleDashboardDashboardFilterStateValueRelativeRangeFilterValue(BaseModel):
    end: SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueEnd

    start: SampleDashboardDashboardFilterStateValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class SampleDashboardDashboardFilterStateValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class SampleDashboardDashboardFilterStateValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


SampleDashboardDashboardFilterStateValue: TypeAlias = Union[
    SampleDashboardDashboardFilterStateValueScalarFilterValue,
    SampleDashboardDashboardFilterStateValueMultiFilterValue,
    SampleDashboardDashboardFilterStateValueNumberRangeFilterValue,
    SampleDashboardDashboardFilterStateValueAbsoluteDateFilterValue,
    SampleDashboardDashboardFilterStateValueAbsoluteRangeFilterValue,
    SampleDashboardDashboardFilterStateValueRelativeRangeFilterValue,
    SampleDashboardDashboardFilterStateValuePresetReferenceFilterValue,
    SampleDashboardDashboardFilterStateValueNullFilterValue,
    None,
]


class SampleDashboardDashboardFilterState(BaseModel):
    effective_kater_id: str
    """Stable effective runtime filter ID"""

    enabled: Optional[bool] = None
    """Requested enabled state override for this effective filter"""

    value: Optional[SampleDashboardDashboardFilterStateValue] = None
    """Requested runtime value override for this effective filter"""


class SampleDashboard(BaseModel):
    """Dashboard context block in `RenderedQueryRequestV1`."""

    dashboard_filter_state: List[SampleDashboardDashboardFilterState]

    dashboard_kater_id: Optional[str] = None

    slot_name: Optional[str] = None

    widget_kater_id: Optional[str] = None


class SampleFieldSelectionTimeframeOverride(BaseModel):
    """Runtime grain choice for a temporal source dimension."""

    active_timeframe: str

    source_kater_id: str


class SampleFieldSelection(BaseModel):
    """Structured field selection: source field IDs plus optional grain overrides."""

    selected_field_ids: List[str]

    timeframe_overrides: Optional[List[SampleFieldSelectionTimeframeOverride]] = None


class SampleFilterStateValueScalarFilterValue(BaseModel):
    value: Union[str, float, bool]
    """Single scalar runtime value"""

    mode: Optional[Literal["scalar"]] = None


class SampleFilterStateValueMultiFilterValue(BaseModel):
    values: List[Union[str, float, bool]]
    """List of scalar runtime values"""

    mode: Optional[Literal["multi"]] = None


class SampleFilterStateValueNumberRangeFilterValue(BaseModel):
    end: float

    start: float

    mode: Optional[Literal["number_range"]] = None


class SampleFilterStateValueAbsoluteDateFilterValue(BaseModel):
    value: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_date"]] = None


class SampleFilterStateValueAbsoluteRangeFilterValue(BaseModel):
    end: str
    """Absolute DATE or TIMESTAMP string"""

    start: str
    """Absolute DATE or TIMESTAMP string"""

    mode: Optional[Literal["absolute_range"]] = None


class SampleFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class SampleFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


SampleFilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    SampleFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    SampleFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class SampleFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(BaseModel):
    amount: int

    direction: Literal["ago", "ahead"]

    unit: Literal["day", "week", "month", "quarter", "year"]


class SampleFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(BaseModel):
    anchor: Literal["today", "now"]


SampleFilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    SampleFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    SampleFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class SampleFilterStateValueRelativeRangeFilterValue(BaseModel):
    end: SampleFilterStateValueRelativeRangeFilterValueEnd

    start: SampleFilterStateValueRelativeRangeFilterValueStart

    mode: Optional[Literal["relative_range"]] = None


class SampleFilterStateValuePresetReferenceFilterValue(BaseModel):
    preset: str
    """Stable preset key matching presets[].name"""

    mode: Optional[Literal["preset"]] = None


class SampleFilterStateValueNullFilterValue(BaseModel):
    mode: Optional[Literal["null"]] = None


SampleFilterStateValue: TypeAlias = Union[
    SampleFilterStateValueScalarFilterValue,
    SampleFilterStateValueMultiFilterValue,
    SampleFilterStateValueNumberRangeFilterValue,
    SampleFilterStateValueAbsoluteDateFilterValue,
    SampleFilterStateValueAbsoluteRangeFilterValue,
    SampleFilterStateValueRelativeRangeFilterValue,
    SampleFilterStateValuePresetReferenceFilterValue,
    SampleFilterStateValueNullFilterValue,
    None,
]


class SampleFilterState(BaseModel):
    effective_kater_id: str
    """Stable effective runtime filter ID"""

    enabled: Optional[bool] = None
    """Requested enabled state override for this effective filter"""

    value: Optional[SampleFilterStateValue] = None
    """Requested runtime value override for this effective filter"""


class SamplePresentation(BaseModel):
    """Presentation config block in `RenderedQueryRequestV1`."""

    chart: Optional[Dict[str, Union[str, int, float, bool, None, List[object], Dict[str, object]]]] = None

    display: Optional[Dict[str, Union[str, int, float, bool, None, List[object], Dict[str, object]]]] = None

    style: Optional[Dict[str, Union[str, int, float, bool, None, List[object], Dict[str, object]]]] = None


class SampleResultWindow(BaseModel):
    """
    Result window block in `RenderedQueryRequestV1` (consumers do not supply
    backend-computed `query_limit`, `max_row_limit`, `effective_limit`).
    """

    cursor: Optional[str] = None

    page_size: Optional[int] = None

    sort_by: Optional[str] = None

    sort_order: Optional[Literal["asc", "desc"]] = None


class SampleTemporal(BaseModel):
    """Request clock block in `RenderedQueryRequestV1`.

    Either field may be `null`
    on the request; the backend resolves both before canonicalization (the
    canonical `temporal` block requires non-null `timezone` and `as_of`).
    """

    as_of: Optional[str] = None

    timezone: Optional[str] = None


class SampleVariable(BaseModel):
    """Runtime variable value as supplied in a `RenderedQueryRequestV1`.

    `variable_kater_id` is preferred. Until every surface exposes it,
    `(query_kater_id, scope, name)` is the migration fallback identity.
    """

    name: str
    """Variable name within scope"""

    query_kater_id: str
    """Owning query UUID"""

    scope: Literal["query", "global"]

    value: Union[str, float, bool, List[object], Dict[str, object], None] = None
    """Free-form JSON variable value"""

    variable_kater_id: Optional[str] = None
    """Stable variable UUID; fall back to (query_kater_id, scope, name) when null"""


class Sample(BaseModel):
    """Consumer-facing request shape.

    Excludes legacy `combination_id` / `combination`
    by contract: selected fields and variables are represented directly.
    """

    connection_id: str

    dashboard: Optional[SampleDashboard] = None
    """Dashboard context block in `RenderedQueryRequestV1`."""

    field_selection: SampleFieldSelection
    """Structured field selection: source field IDs plus optional grain overrides."""

    filter_state: List[SampleFilterState]

    pinned_variant: Optional[str] = None

    presentation: SamplePresentation
    """Presentation config block in `RenderedQueryRequestV1`."""

    query_kater_id: str

    result_window: SampleResultWindow
    """
    Result window block in `RenderedQueryRequestV1` (consumers do not supply
    backend-computed `query_limit`, `max_row_limit`, `effective_limit`).
    """

    temporal: SampleTemporal
    """Request clock block in `RenderedQueryRequestV1`.

    Either field may be `null` on the request; the backend resolves both before
    canonicalization (the canonical `temporal` block requires non-null `timezone`
    and `as_of`).
    """

    variables: List[SampleVariable]


class CapabilitySampleResponse(BaseModel):
    """Response shape for ``POST /api/v1/compiler/capabilities/sample``.

    Matches Story 6.2's CLI shim ``CapabilitySampleResponse`` verbatim:
    ``samples`` carries the deterministic ordered list of sampled selections,
    ``truncated`` is True when the request asked for more samples than exist,
    ``available`` documents the actual unique-selection count.

    ``extra="allow"`` ensures the deployed CLI shim deserializes future
    additions (e.g. a ``metadata`` block for telemetry) without redeploying.
    """

    available: Optional[int] = None

    samples: Optional[List[Sample]] = None

    truncated: Optional[bool] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
