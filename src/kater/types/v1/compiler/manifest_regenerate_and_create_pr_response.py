# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ManifestRegenerateAndCreatePrResponse"]


class ManifestRegenerateAndCreatePrResponse(BaseModel):
    """Response model for manifest recovery PR creation."""

    branch_name: str
    """Remote branch name used for the PR"""

    pr_number: int
    """Created pull request number"""

    pr_url: str
    """Created pull request URL"""
