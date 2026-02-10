# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["SubqueryConditionParam"]

_SubqueryConditionParamReservedKeywords = TypedDict(
    "_SubqueryConditionParamReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SubqueryConditionParam(_SubqueryConditionParamReservedKeywords, total=False):
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    where: Required[SequenceNotStr[str]]
    """WHERE conditions for the subquery"""
