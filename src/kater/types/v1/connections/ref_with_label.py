# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["RefWithLabel"]


class RefWithLabel(BaseModel):
    """A reference with optional label override"""

    ref: str
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str] = None
    """Optional label override for this reference"""
