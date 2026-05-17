# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "CompilerRegenerateMetadataParams",
    "Persist",
    "PersistScope",
    "PostQueryState",
    "PostQueryStateFilter",
    "PostQueryStateFilterField",
    "PostQueryStateFilterFieldModifier",
    "PostQueryStateFilterDefaultValue",
    "PostQueryStateFilterDefaultValueDateRangeValue",
    "PostQueryStateFilterDefaultValueNumberRangeValue",
    "PostQueryStateFilterValues",
    "PostQueryStateSort",
    "PostQueryStateSortField",
    "PostQueryStateSortFieldModifier",
]


class CompilerRegenerateMetadataParams(TypedDict, total=False):
    persist: Required[Persist]
    """Persistence behavior configuration"""

    post_query_state: Required[PostQueryState]
    """Canonical post-query filters, sorts, and refinements"""

    query_kater_id: Required[str]
    """Query kater_id this state applies to"""

    rendered_query_key_id: Required[str]
    """Base rendered query key ID (without post-query state)"""

    source: Optional[str]

    post_query_state_id: Optional[str]
    """Existing post-query state ID for updates"""

    revision: Optional[int]
    """Expected revision for conflict detection"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]


class PersistScope(TypedDict, total=False):
    """Scope definition for post-query state persistence."""

    chat_thread_id: Optional[str]
    """Chat thread ID for chat_message_widget scope"""

    message_id: Optional[str]
    """Message ID for chat_message_widget scope"""

    session_id: Optional[str]
    """Session ID for query_builder_draft scope"""

    widget_instance_id: Optional[str]
    """Widget instance ID for chat_message_widget scope"""


class Persist(TypedDict, total=False):
    """Persistence behavior configuration"""

    mode: Required[str]
    """Persistence mode: 'none' or 'upsert'"""

    scope: Optional[PersistScope]
    """Scope definition for post-query state persistence."""

    scope_type: Optional[str]
    """Type of scope (e.g., 'chat_message_widget', 'query_builder_draft')"""


class PostQueryStateFilterFieldModifier(TypedDict, total=False):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Required[Literal["timeframe"]]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: Required[str]
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class PostQueryStateFilterField(TypedDict, total=False):
    """Field target using object form with ref and optional modifiers"""

    ref: Required[str]
    """Reference to the field"""

    modifiers: Optional[Iterable[PostQueryStateFilterFieldModifier]]
    """Optional modifiers for the field (e.g. timeframe)"""


class PostQueryStateFilterDefaultValueDateRangeValue(TypedDict, total=False):
    """Date range filter value"""

    mode: Required[Literal["absolute_range", "relative_range"]]


class PostQueryStateFilterDefaultValueNumberRangeValue(TypedDict, total=False):
    """Number range filter value"""

    max: Required[float]
    """Maximum value (inclusive)"""

    min: Required[float]
    """Minimum value (inclusive)"""


PostQueryStateFilterDefaultValue: TypeAlias = Union[
    str,
    float,
    bool,
    SequenceNotStr[Union[str, float, bool]],
    PostQueryStateFilterDefaultValueDateRangeValue,
    PostQueryStateFilterDefaultValueNumberRangeValue,
]


class PostQueryStateFilterValues(TypedDict, total=False):
    """Values source configuration for categorical filters"""

    source: Required[Literal["result_distinct"]]
    """Source of filter values"""

    limit: int
    """Maximum number of values to show"""

    searchable: bool
    """Whether the filter should be searchable"""

    sort: Literal["asc", "desc"]
    """Sort order for values"""


class PostQueryStateFilter(TypedDict, total=False):
    """A post-query filter definition for a specific field occurrence"""

    expression: Required[Literal["equals", "in", "between"]]
    """Filter expression operator"""

    field: Required[PostQueryStateFilterField]
    """Field target using object form with ref and optional modifiers"""

    kind: Required[Literal["date", "dropdown", "multiselect", "number_range"]]
    """Filter kind that determines UI control type"""

    default_enabled: Optional[bool]
    """Whether this filter should be enabled by default"""

    default_value: Optional[PostQueryStateFilterDefaultValue]
    """Default value for the filter when enabled"""

    values: Optional[PostQueryStateFilterValues]
    """Values source configuration for categorical filters"""


class PostQueryStateSortFieldModifier(TypedDict, total=False):
    """A normalized modifier applied to a source field occurrence.

    The first contract supports only timeframe modifiers.
    """

    kind: Required[Literal["timeframe"]]
    """Modifier kind. Unknown kinds are invalid until the shared contract is extended."""

    value: Required[str]
    """Concrete modifier value.

    Canonical contexts omit raw timeframe instead of storing value raw.
    """


class PostQueryStateSortField(TypedDict, total=False):
    """Field target using object form with ref and optional modifiers"""

    ref: Required[str]
    """Reference to the field"""

    modifiers: Optional[Iterable[PostQueryStateSortFieldModifier]]
    """Optional modifiers for the field (e.g. timeframe)"""


class PostQueryStateSort(TypedDict, total=False):
    """A post-query sort definition for a specific field occurrence"""

    field: Required[PostQueryStateSortField]
    """Field target using object form with ref and optional modifiers"""

    default_direction: Optional[Literal["asc", "desc"]]
    """Default sort direction when enabled"""

    default_enabled: Optional[bool]
    """Whether this sort should be enabled by default"""

    priority: Optional[int]
    """Sort priority for multi-field sorts (lower numbers sort first)"""


class PostQueryState(TypedDict, total=False):
    """Canonical post-query filters, sorts, and refinements"""

    filters: Optional[Iterable[PostQueryStateFilter]]
    """Post-query filter definitions that apply to returned result rows"""

    sorts: Optional[Iterable[PostQueryStateSort]]
    """Post-query sort definitions that apply to returned result rows"""
