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

    combination_id: Optional[str] = None
    """Deterministic UUID v5 for this combination"""

    query_label: Optional[str] = None
    """Human-readable label for the query"""

    roles: Optional[Dict[str, str]] = None
    """Field-to-role mapping (e.g. {'due_month': 'x_axis'})"""

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

    widget_type: Optional[str] = None
    """Resolved widget type (e.g. 'axis_metric_by_dimensiondate')"""


class CompilerEnumerateResponse(BaseModel):
    """Response model for query combination enumeration."""

    combinations: List[Combination]
    """All valid query configurations"""

    total_count: int
    """Total number of combinations"""
