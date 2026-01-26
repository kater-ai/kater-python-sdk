# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ScaffoldTrigger"]


class ScaffoldTrigger(BaseModel):
    """Response from triggering scaffolding."""

    message: str

    status: str

    success: bool

    branch: Optional[str] = None

    error: Optional[str] = None

    pr_number: Optional[int] = None

    pr_url: Optional[str] = None
