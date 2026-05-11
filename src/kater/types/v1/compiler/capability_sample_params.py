# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CapabilitySampleParams"]


class CapabilitySampleParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection UUID to sample selections against"""

    n: Required[int]
    """Number of representative selections requested (must be >= 1)"""

    query_kater_id: Required[str]
    """Query UUID to sample selections for"""

    source: Optional[str]

    include_filter_variants: bool
    """When true, include tier-8 optional filter variants in the sample"""

    include_pinned_variants: bool
    """When true, include pinned-variant variants in the sample"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
