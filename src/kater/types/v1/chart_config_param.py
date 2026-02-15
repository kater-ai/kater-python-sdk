# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ChartConfigParam"]


class ChartConfigParam(TypedDict, total=False):
    """Chart configuration with variable references"""

    color_by: Optional[str]
    """Field or variable reference for color grouping"""

    comparison: Optional[Literal["previous_period", "target"]]
    """Comparison mode for single_value widgets (e.g., previous_period, target)"""

    size: Optional[str]
    """Field or variable reference for size"""

    stack_by: Optional[str]
    """Field or variable reference for stacking"""

    target_value: Optional[str]
    """Target value for comparison: target mode"""

    x_axis: Optional[str]
    """Field or variable reference for x-axis"""

    y_axis: Optional[str]
    """Field or variable reference for y-axis"""
