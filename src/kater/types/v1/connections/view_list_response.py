# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["ViewListResponse", "File"]


class File(BaseModel):
    """A single view file in the sync."""

    name: str
    """File name (e.g., 'customers.yaml')"""

    path: str
    """Full path relative to connection folder"""


class ViewListResponse(BaseModel):
    """Response for listing view files in a sync."""

    branch: str
    """Branch the files were read from"""

    files: List[File]
    """List of view files"""

    is_pr_branch: bool
    """True if reading from PR branch, False if from main"""
