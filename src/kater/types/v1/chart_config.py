# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

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

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
