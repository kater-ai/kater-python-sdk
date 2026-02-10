# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["InlineField"]


class InlineField(BaseModel):
    """An inline field definition for dimensions/measures/calculations"""

    kater_id: str
    """Unique identifier for this inline field"""

    name: str
    """Name of the inline field"""

    sql: str
    """SQL expression for the field"""

    label: Optional[str] = None
    """Human-readable label"""
