# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RefWithLabelParam"]


class RefWithLabelParam(TypedDict, total=False):
    """A reference with optional label override"""

    ref: Required[str]
    """Reference using ref(), var(), or expr() syntax"""

    label: Optional[str]
    """Optional label override for this reference"""
