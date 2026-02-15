# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChartConfig"]


class ChartConfig(BaseModel):
    """Chart configuration with variable references"""

    color_by: Optional[str] = None
    """Field or variable reference for color grouping"""

    comparison: Optional[Literal["previous_period", "target"]] = None
    """Comparison mode for single_value widgets (e.g., previous_period, target)"""

    size: Optional[str] = None
    """Field or variable reference for size"""

    stack_by: Optional[str] = None
    """Field or variable reference for stacking"""

    target_value: Optional[str] = None
    """Target value for comparison: target mode"""

    x_axis: Optional[str] = None
    """Field or variable reference for x-axis"""

    y_axis: Optional[str] = None
    """Field or variable reference for y-axis"""
