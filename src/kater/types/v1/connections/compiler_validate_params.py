# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["CompilerValidateParams"]


class CompilerValidateParams(TypedDict, total=False):
    source: Optional[str]

    connection_ids: Optional[SequenceNotStr[str]]
    """Optional connection IDs to validate. If omitted, validates all connections."""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
