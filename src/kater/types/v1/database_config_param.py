# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatabaseConfigParam", "Schema"]


class Schema(TypedDict, total=False):
    """Schema configuration for connection creation request."""

    name: Required[str]
    """Schema name (also used as the warehouse object name)"""

    description: Optional[str]
    """Description of the schema"""

    label: Optional[str]
    """Human-readable label for the schema (defaults to name if not set)"""


class DatabaseConfigParam(TypedDict, total=False):
    """Database configuration for connection creation request."""

    name: Required[str]
    """Database name (also used as the warehouse object name)"""

    description: Optional[str]
    """Description of the database"""

    label: Optional[str]
    """Human-readable label for the database (defaults to name if not set)"""

    schemas: Iterable[Schema]
    """Schema configurations to include (empty = discover all schemas)"""

    timezone: Optional[str]
    """Timezone for the database (e.g., 'UTC', 'America/New_York')"""
