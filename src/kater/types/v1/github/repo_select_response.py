# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .repository import Repository

__all__ = ["RepoSelectResponse"]


class RepoSelectResponse(BaseModel):
    """Repository selection response."""

    has_existing_structure: bool

    message: str

    needs_scaffolding: bool

    repository: Repository
    """Repository information response."""

    success: bool
