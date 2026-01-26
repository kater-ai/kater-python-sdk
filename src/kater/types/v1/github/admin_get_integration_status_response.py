# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AdminGetIntegrationStatusResponse"]


class AdminGetIntegrationStatusResponse(BaseModel):
    """Response for client GitHub integration status."""

    client_id: str

    connected: bool

    oauth_completed: bool

    connection_status: Optional[str] = None

    created_at: Optional[str] = None

    github_username: Optional[str] = None

    installation_id: Optional[int] = None

    last_sync_at: Optional[str] = None

    repository: Optional[str] = None

    repository_selection_pending: Optional[bool] = None

    scaffolding_branch: Optional[str] = None

    scaffolding_pr_url: Optional[str] = None

    scaffolding_status: Optional[str] = None

    updated_at: Optional[str] = None
