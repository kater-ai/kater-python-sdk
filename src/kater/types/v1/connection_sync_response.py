# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConnectionSyncResponse"]


class ConnectionSyncResponse(BaseModel):
    """Response for starting a schema sync.

    Returned with 202 Accepted when sync workflow is successfully queued.
    """

    sync_id: str
    """Schema sync record ID"""

    hatchet_run_id: Optional[str] = None
    """Hatchet workflow run ID"""

    status: Optional[str] = None
    """Current sync status"""
