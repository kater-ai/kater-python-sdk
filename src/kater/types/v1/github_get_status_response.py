# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GitHubGetStatusResponse"]


class GitHubGetStatusResponse(BaseModel):
    """Response for connection status."""

    connected: bool

    default_branch: Optional[str] = None

    last_sync_at: Optional[str] = None

    last_used_at: Optional[str] = None

    owner: Optional[str] = None

    repository: Optional[str] = None

    scaffolding_pr_author: Optional[str] = None

    scaffolding_pr_created_at: Optional[str] = None

    scaffolding_pr_state: Optional[str] = None

    scaffolding_pr_title: Optional[str] = None

    scaffolding_pr_url: Optional[str] = None

    scaffolding_status: Optional[str] = None

    status: Optional[str] = None
