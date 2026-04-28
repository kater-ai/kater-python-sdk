# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "CompilerResolveParams",
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
]


class CompilerResolveParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection to resolve against"""

    query_id: Required[str]
    """UUID of the query template"""

    source: Optional[str]

    auto_fix: bool
    """Automatically fix broken refs caused by renames. Defaults to True."""

    combination: str
    """Comma-separated slot selections and variable assignments.

    Reserved keys: measure, dimension, calculation. All other keys are variable
    assignments. Example: 'measure=Compliance
    Rate,dimension=Department,breakdown=region'
    """

    filter_state: Optional[Iterable[FilterState]]
    """Optional V2 runtime filter-state payload keyed by effective filter ID."""

    pinned_variant: Optional[str]
    """Optional pinned variant name (e.g.

    '\\__base'). Selects a specific pinned configuration.
    """

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]


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
