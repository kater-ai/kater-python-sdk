# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["CapabilityCreateParams"]


class CapabilityCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection UUID to enumerate capabilities against"""

    source: Optional[str]

    query_ids: Optional[SequenceNotStr[str]]
    """Optional list of query UUIDs to limit the response.

    When omitted (or null), the response includes capabilities for every query in
    the connection.
    """

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
