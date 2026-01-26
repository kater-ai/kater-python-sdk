# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .repository import Repository

__all__ = ["RepoListResponse"]


class RepoListResponse(BaseModel):
    """List of repositories response."""

    repositories: List[Repository]

    total_count: int
