# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["YamlCommitResponse"]


class YamlCommitResponse(BaseModel):
    """Response for YAML commit endpoint."""

    merged: bool
    """Whether the PR was auto-merged"""

    pr_number: int
    """GitHub PR number"""

    pr_url: str
    """GitHub PR URL"""
