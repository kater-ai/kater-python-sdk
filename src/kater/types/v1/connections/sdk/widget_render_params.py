# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = [
    "WidgetRenderParams",
    "Dashboard",
    "DashboardDashboardFilterState",
    "DashboardDashboardFilterStateValue",
    "DashboardDashboardFilterStateValueScalarFilterValue",
    "DashboardDashboardFilterStateValueMultiFilterValue",
    "DashboardDashboardFilterStateValueNumberRangeFilterValue",
    "DashboardDashboardFilterStateValueAbsoluteDateFilterValue",
    "DashboardDashboardFilterStateValueAbsoluteRangeFilterValue",
    "DashboardDashboardFilterStateValueRelativeRangeFilterValue",
    "DashboardDashboardFilterStateValueRelativeRangeFilterValueEnd",
    "DashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "DashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "DashboardDashboardFilterStateValueRelativeRangeFilterValueStart",
    "DashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "DashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "DashboardDashboardFilterStateValuePresetReferenceFilterValue",
    "DashboardDashboardFilterStateValueNullFilterValue",
    "FieldSelection",
    "FieldSelectionTimeframeOverride",
    "FilterState",
    "FilterStateValue",
    "FilterStateValueScalarFilterValue",
    "FilterStateValueMultiFilterValue",
    "FilterStateValueNumberRangeFilterValue",
    "FilterStateValueAbsoluteDateFilterValue",
    "FilterStateValueAbsoluteRangeFilterValue",
    "FilterStateValueRelativeRangeFilterValue",
    "FilterStateValueRelativeRangeFilterValueEnd",
    "FilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary",
    "FilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary",
    "FilterStateValueRelativeRangeFilterValueStart",
    "FilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary",
    "FilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary",
    "FilterStateValuePresetReferenceFilterValue",
    "FilterStateValueNullFilterValue",
    "Presentation",
    "ResultWindow",
    "Temporal",
    "Variable",
]


class WidgetRenderParams(TypedDict, total=False):
    connection_id: Required[str]

    dashboard: Required[Optional[Dashboard]]
    """Dashboard context block in `RenderedQueryRequestV1`."""

    field_selection: Required[FieldSelection]
    """Structured field selection: source field IDs plus optional grain overrides."""

    filter_state: Required[Iterable[FilterState]]

    pinned_variant: Required[Optional[str]]

    presentation: Required[Presentation]
    """Presentation config block in `RenderedQueryRequestV1`."""

    query_kater_id: Required[str]

    result_window: Required[ResultWindow]
    """
    Result window block in `RenderedQueryRequestV1` (consumers do not supply
    backend-computed `query_limit`, `max_row_limit`, `effective_limit`).
    """

    temporal: Required[Temporal]
    """Request clock block in `RenderedQueryRequestV1`.

    Either field may be `null` on the request; the backend resolves both before
    canonicalization (the canonical `temporal` block requires non-null `timezone`
    and `as_of`).
    """

    variables: Required[Iterable[Variable]]

    source: Optional[str]

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]


class DashboardDashboardFilterStateValueScalarFilterValue(TypedDict, total=False):
    value: Required[Union[str, float, bool]]
    """Single scalar runtime value"""

    mode: Literal["scalar"]


class DashboardDashboardFilterStateValueMultiFilterValue(TypedDict, total=False):
    values: Required[SequenceNotStr[Union[str, float, bool]]]
    """List of scalar runtime values"""

    mode: Literal["multi"]


class DashboardDashboardFilterStateValueNumberRangeFilterValue(TypedDict, total=False):
    end: Required[float]

    start: Required[float]

    mode: Literal["number_range"]


class DashboardDashboardFilterStateValueAbsoluteDateFilterValue(TypedDict, total=False):
    value: Required[str]
    """Absolute DATE or TIMESTAMP string"""

    mode: Literal["absolute_date"]


class DashboardDashboardFilterStateValueAbsoluteRangeFilterValue(TypedDict, total=False):
    end: Required[str]
    """Absolute DATE or TIMESTAMP string"""

    start: Required[str]
    """Absolute DATE or TIMESTAMP string"""

    mode: Literal["absolute_range"]


class DashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(TypedDict, total=False):
    amount: Required[int]

    direction: Required[Literal["ago", "ahead"]]

    unit: Required[Literal["day", "week", "month", "quarter", "year"]]


class DashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(TypedDict, total=False):
    anchor: Required[Literal["today", "now"]]


DashboardDashboardFilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    DashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    DashboardDashboardFilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class DashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(TypedDict, total=False):
    amount: Required[int]

    direction: Required[Literal["ago", "ahead"]]

    unit: Required[Literal["day", "week", "month", "quarter", "year"]]


class DashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(TypedDict, total=False):
    anchor: Required[Literal["today", "now"]]


DashboardDashboardFilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    DashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    DashboardDashboardFilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class DashboardDashboardFilterStateValueRelativeRangeFilterValue(TypedDict, total=False):
    end: Required[DashboardDashboardFilterStateValueRelativeRangeFilterValueEnd]

    start: Required[DashboardDashboardFilterStateValueRelativeRangeFilterValueStart]

    mode: Literal["relative_range"]


class DashboardDashboardFilterStateValuePresetReferenceFilterValue(TypedDict, total=False):
    preset: Required[str]
    """Stable preset key matching presets[].name"""

    mode: Literal["preset"]


class DashboardDashboardFilterStateValueNullFilterValue(TypedDict, total=False):
    mode: Literal["null"]


DashboardDashboardFilterStateValue: TypeAlias = Union[
    DashboardDashboardFilterStateValueScalarFilterValue,
    DashboardDashboardFilterStateValueMultiFilterValue,
    DashboardDashboardFilterStateValueNumberRangeFilterValue,
    DashboardDashboardFilterStateValueAbsoluteDateFilterValue,
    DashboardDashboardFilterStateValueAbsoluteRangeFilterValue,
    DashboardDashboardFilterStateValueRelativeRangeFilterValue,
    DashboardDashboardFilterStateValuePresetReferenceFilterValue,
    DashboardDashboardFilterStateValueNullFilterValue,
]


class DashboardDashboardFilterState(TypedDict, total=False):
    effective_kater_id: Required[str]
    """Stable effective runtime filter ID"""

    enabled: Optional[bool]
    """Requested enabled state override for this effective filter"""

    value: Optional[DashboardDashboardFilterStateValue]
    """Requested runtime value override for this effective filter"""


class Dashboard(TypedDict, total=False):
    """Dashboard context block in `RenderedQueryRequestV1`."""

    dashboard_filter_state: Required[Iterable[DashboardDashboardFilterState]]

    dashboard_kater_id: Required[Optional[str]]

    slot_name: Required[Optional[str]]

    widget_kater_id: Required[Optional[str]]


class FieldSelectionTimeframeOverride(TypedDict, total=False):
    """Runtime grain choice for a temporal source dimension."""

    active_timeframe: Required[str]

    source_kater_id: Required[str]


class FieldSelection(TypedDict, total=False):
    """Structured field selection: source field IDs plus optional grain overrides."""

    selected_field_ids: Required[SequenceNotStr[str]]

    timeframe_overrides: Iterable[FieldSelectionTimeframeOverride]


class FilterStateValueScalarFilterValue(TypedDict, total=False):
    value: Required[Union[str, float, bool]]
    """Single scalar runtime value"""

    mode: Literal["scalar"]


class FilterStateValueMultiFilterValue(TypedDict, total=False):
    values: Required[SequenceNotStr[Union[str, float, bool]]]
    """List of scalar runtime values"""

    mode: Literal["multi"]


class FilterStateValueNumberRangeFilterValue(TypedDict, total=False):
    end: Required[float]

    start: Required[float]

    mode: Literal["number_range"]


class FilterStateValueAbsoluteDateFilterValue(TypedDict, total=False):
    value: Required[str]
    """Absolute DATE or TIMESTAMP string"""

    mode: Literal["absolute_date"]


class FilterStateValueAbsoluteRangeFilterValue(TypedDict, total=False):
    end: Required[str]
    """Absolute DATE or TIMESTAMP string"""

    start: Required[str]
    """Absolute DATE or TIMESTAMP string"""

    mode: Literal["absolute_range"]


class FilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary(TypedDict, total=False):
    amount: Required[int]

    direction: Required[Literal["ago", "ahead"]]

    unit: Required[Literal["day", "week", "month", "quarter", "year"]]


class FilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary(TypedDict, total=False):
    anchor: Required[Literal["today", "now"]]


FilterStateValueRelativeRangeFilterValueEnd: TypeAlias = Union[
    FilterStateValueRelativeRangeFilterValueEndRelativeOffsetBoundary,
    FilterStateValueRelativeRangeFilterValueEndRelativeAnchorBoundary,
]


class FilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary(TypedDict, total=False):
    amount: Required[int]

    direction: Required[Literal["ago", "ahead"]]

    unit: Required[Literal["day", "week", "month", "quarter", "year"]]


class FilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary(TypedDict, total=False):
    anchor: Required[Literal["today", "now"]]


FilterStateValueRelativeRangeFilterValueStart: TypeAlias = Union[
    FilterStateValueRelativeRangeFilterValueStartRelativeOffsetBoundary,
    FilterStateValueRelativeRangeFilterValueStartRelativeAnchorBoundary,
]


class FilterStateValueRelativeRangeFilterValue(TypedDict, total=False):
    end: Required[FilterStateValueRelativeRangeFilterValueEnd]

    start: Required[FilterStateValueRelativeRangeFilterValueStart]

    mode: Literal["relative_range"]


class FilterStateValuePresetReferenceFilterValue(TypedDict, total=False):
    preset: Required[str]
    """Stable preset key matching presets[].name"""

    mode: Literal["preset"]


class FilterStateValueNullFilterValue(TypedDict, total=False):
    mode: Literal["null"]


FilterStateValue: TypeAlias = Union[
    FilterStateValueScalarFilterValue,
    FilterStateValueMultiFilterValue,
    FilterStateValueNumberRangeFilterValue,
    FilterStateValueAbsoluteDateFilterValue,
    FilterStateValueAbsoluteRangeFilterValue,
    FilterStateValueRelativeRangeFilterValue,
    FilterStateValuePresetReferenceFilterValue,
    FilterStateValueNullFilterValue,
]


class FilterState(TypedDict, total=False):
    effective_kater_id: Required[str]
    """Stable effective runtime filter ID"""

    enabled: Optional[bool]
    """Requested enabled state override for this effective filter"""

    value: Optional[FilterStateValue]
    """Requested runtime value override for this effective filter"""


class Presentation(TypedDict, total=False):
    """Presentation config block in `RenderedQueryRequestV1`."""

    chart: Dict[str, Union[str, int, float, bool, None, Iterable[object], Dict[str, object]]]

    display: Dict[str, Union[str, int, float, bool, None, Iterable[object], Dict[str, object]]]

    style: Dict[str, Union[str, int, float, bool, None, Iterable[object], Dict[str, object]]]


class ResultWindow(TypedDict, total=False):
    """
    Result window block in `RenderedQueryRequestV1` (consumers do not supply
    backend-computed `query_limit`, `max_row_limit`, `effective_limit`).
    """

    cursor: Required[Optional[str]]

    page_size: Required[Optional[int]]

    sort_by: Required[Optional[str]]

    sort_order: Required[Optional[Literal["asc", "desc"]]]


class Temporal(TypedDict, total=False):
    """Request clock block in `RenderedQueryRequestV1`.

    Either field may be `null`
    on the request; the backend resolves both before canonicalization (the
    canonical `temporal` block requires non-null `timezone` and `as_of`).
    """

    as_of: Required[Optional[str]]

    timezone: Required[Optional[str]]


class Variable(TypedDict, total=False):
    """Runtime variable value as supplied in a `RenderedQueryRequestV1`.

    `variable_kater_id` is preferred. Until every surface exposes it,
    `(query_kater_id, scope, name)` is the migration fallback identity.
    """

    name: Required[str]
    """Variable name within scope"""

    query_kater_id: Required[str]
    """Owning query UUID"""

    scope: Required[Literal["query", "global"]]

    value: Required[Union[str, float, bool, Iterable[object], Dict[str, object], None]]
    """Free-form JSON variable value"""

    variable_kater_id: Required[Optional[str]]
    """Stable variable UUID; fall back to (query_kater_id, scope, name) when null"""
