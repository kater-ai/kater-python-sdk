# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    """Response model for API key (masked)."""

    id: str
    """API key UUID"""

    created_at: datetime
    """Creation timestamp"""

    description: Optional[str] = None
    """Optional description"""

    expires_at: Optional[datetime] = None
    """Expiration datetime"""

    key_prefix: str
    """Key prefix for display (e.g., kat_live_7kD9...)"""

    last_used_at: Optional[datetime] = None
    """Last usage timestamp"""

    name: str
    """API key name"""

    scopes: List[str]
    """Granted scopes"""

    status: Literal["active", "revoked", "expired"]
    """Key status (active/revoked/expired)"""
