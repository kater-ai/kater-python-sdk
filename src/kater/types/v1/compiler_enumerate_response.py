# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["CompilerEnumerateResponse", "Combination"]


class Combination(BaseModel):
    """A single valid query configuration."""

    query_ref: str
    """Query template reference (e.g. 'q:COMPLIANCE_OVERVIEW')"""

    widget_category: str
    """Widget category (e.g. 'axis', 'table')"""

    query_label: Optional[str] = None
    """Human-readable label for the query"""

    selected_calculations: Optional[List[str]] = None
    """Selected optional calculation names"""

    selected_dimensions: Optional[List[str]] = None
    """Selected optional dimension names"""

    selected_filters: Optional[List[str]] = None
    """Selected optional filter names"""

    selected_measures: Optional[List[str]] = None
    """Selected optional measure names"""

    variable_assignments: Optional[Dict[str, object]] = None
    """Variable name to value assignments"""


class CompilerEnumerateResponse(BaseModel):
    """Response model for query combination enumeration."""

    combinations: List[Combination]
    """All valid query configurations"""

    total_count: int
    """Total number of combinations"""
