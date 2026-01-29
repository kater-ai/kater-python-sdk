# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ConnectionUpdateParams"]


class ConnectionUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Connection description"""

    label: Optional[str]
    """Human-readable display label"""

    name: Optional[str]
    """Connection name (snake_case identifier)"""
