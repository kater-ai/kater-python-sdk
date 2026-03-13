# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["McpGetAuditHistoryResponse", "Item"]


class Item(BaseModel):
    """Response model for a single credential audit record."""

    id: str

    action: str

    actor_id: str

    created_at: datetime

    actor_ip: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None


class McpGetAuditHistoryResponse(BaseModel):
    """Paginated response for credential audit history."""

    items: List[Item]

    next_cursor: Optional[str] = None
