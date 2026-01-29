# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatabaseUpdateSchemaParams"]


class DatabaseUpdateSchemaParams(TypedDict, total=False):
    connection_id: Required[str]

    database_id: Required[str]

    auto_merge: bool
    """If true and a name change requires a PR, auto-merge it"""

    description: Optional[str]
    """Schema description"""

    label: Optional[str]
    """Human-readable display label"""

    name: Optional[str]
    """Schema name"""
