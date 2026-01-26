# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["GitHubCheckInstallationsResponse", "Installation"]


class Installation(BaseModel):
    """Information about an existing GitHub App installation."""

    account_login: str

    account_type: str

    installation_id: int


class GitHubCheckInstallationsResponse(BaseModel):
    """Response for checking existing installations."""

    has_existing_installation: bool

    installations: Optional[List[Installation]] = None
