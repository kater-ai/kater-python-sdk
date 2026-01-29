# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["GitHubGetInstallationLinkResponse"]


class GitHubGetInstallationLinkResponse(BaseModel):
    """Response for installation link generation."""

    app_name: str

    installation_url: str
