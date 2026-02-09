# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .sync_event_response import SyncEventResponse

__all__ = ["ConnectionRetrieveSyncStatusResponse"]


class ConnectionRetrieveSyncStatusResponse(BaseModel):
    """Response for sync status endpoint.

    Contains full sync state including progress and results.
    """

    connection_id: str
    """Connection ID"""

    created_at: datetime
    """Sync creation timestamp"""

    run_status: str
    """Workflow status: queued, running, succeeded, failed, canceled"""

    sync_id: str
    """Schema sync record ID"""

    completed_at: Optional[datetime] = None
    """Workflow completion timestamp"""

    current_step: Optional[str] = None
    """Current workflow step"""

    error_message: Optional[str] = None
    """Error message if failed"""

    events: Optional[List[SyncEventResponse]] = None
    """Sync event history"""

    hatchet_run_id: Optional[str] = None
    """Hatchet workflow run ID"""

    pr_number: Optional[int] = None
    """GitHub PR number"""

    pr_status: Optional[str] = None
    """PR status: open, merged, closed"""

    pr_url: Optional[str] = None
    """GitHub PR URL"""

    started_at: Optional[datetime] = None
    """Workflow start timestamp"""

    views_deleted: Optional[int] = None
    """Number of views deleted"""

    views_inserted: Optional[int] = None
    """Number of new views added"""

    views_renamed: Optional[int] = None
    """Number of views renamed (subset of updated)"""

    views_updated: Optional[int] = None
    """Number of views updated (dimension changes or renames)"""
