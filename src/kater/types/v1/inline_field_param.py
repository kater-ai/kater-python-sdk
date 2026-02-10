# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["InlineFieldParam"]


class InlineFieldParam(TypedDict, total=False):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: Required[str]
    """Unique identifier for this inline field"""

    name: Required[str]
    """Name of the inline field"""

    sql: Required[str]
    """SQL expression for the field"""

    label: Optional[str]
    """Human-readable label"""
