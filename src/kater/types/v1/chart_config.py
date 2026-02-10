# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ChartConfig"]


class ChartConfig(BaseModel):
    """Chart configuration with variable references"""

    color_by: Optional[str] = None
    """Field or variable reference for color grouping"""

    size: Optional[str] = None
    """Field or variable reference for size"""

    stack_by: Optional[str] = None
    """Field or variable reference for stacking"""

    x_axis: Optional[str] = None
    """Field or variable reference for x-axis"""

    y_axis: Optional[str] = None
    """Field or variable reference for y-axis"""
