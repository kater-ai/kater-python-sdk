# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CompilerEnumerateParams"]


class CompilerEnumerateParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection to enumerate against"""

    source: Optional[str]

    query_refs: Optional[SequenceNotStr[str]]
    """Optional query refs to limit enumeration. If omitted, enumerates all queries."""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
