# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V1ListConnectionsParams"]


class V1ListConnectionsParams(TypedDict, total=False):
    status: Literal["approved", "pending", "all"]
