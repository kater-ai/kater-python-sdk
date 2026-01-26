# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIKeyCreateResponse"]


class APIKeyCreateResponse(BaseModel):
    """Response model for created API key (includes full key once)."""

    id: str
    """API key UUID"""

    created_at: datetime
    """Creation timestamp"""

    expires_at: Optional[datetime] = None
    """Expiration datetime"""

    key: str
    """Full API key (only shown once)"""

    name: str
    """API key name"""

    scopes: List[str]
    """Granted scopes"""
