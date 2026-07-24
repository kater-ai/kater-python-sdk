# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountGetStatusResponse"]


class AccountGetStatusResponse(BaseModel):
    """Current account access status for the authenticated org."""

    activation_status: Literal["trial_requested", "active"]
    """Kater activation state"""

    org_id: str
    """Authenticated PropelAuth organization ID"""

    message: Optional[str] = None
    """Activation guidance message, when gated"""
