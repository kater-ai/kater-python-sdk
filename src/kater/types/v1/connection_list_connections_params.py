# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConnectionListConnectionsParams"]


class ConnectionListConnectionsParams(TypedDict, total=False):
    status: Literal["approved", "pending", "all"]
