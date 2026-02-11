# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["ChartConfigParam"]


class ChartConfigParamTyped(TypedDict, total=False):
    """Chart configuration with variable references"""

    color_by: Optional[str]
    """Field or variable reference for color grouping"""

    size: Optional[str]
    """Field or variable reference for size"""

    stack_by: Optional[str]
    """Field or variable reference for stacking"""

    x_axis: Optional[str]
    """Field or variable reference for x-axis"""

    y_axis: Optional[str]
    """Field or variable reference for y-axis"""


ChartConfigParam: TypeAlias = Union[ChartConfigParamTyped, Dict[str, object]]
