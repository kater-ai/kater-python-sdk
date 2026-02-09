# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SyncEventResponse"]


class SyncEventResponse(BaseModel):
    """Response model for a single sync event."""

    id: str
    """Event ID"""

    created_at: datetime
    """Event timestamp"""

    event_type: str
    """Event type: step_started, step_completed, progress, warning, error"""

    message: str
    """Human-readable event message"""

    metadata: Optional[Dict[str, object]] = None
    """Additional event data"""

    step_name: Optional[str] = None
    """Step name if applicable"""
