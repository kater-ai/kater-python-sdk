# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ScaffoldGetStatusResponse"]


class ScaffoldGetStatusResponse(BaseModel):
    """Response from scaffolding status check."""

    status: str

    branch: Optional[str] = None

    error: Optional[str] = None

    pr_number: Optional[int] = None

    pr_url: Optional[str] = None

    scaffolded_at: Optional[str] = None
