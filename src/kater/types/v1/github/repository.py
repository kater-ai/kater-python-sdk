# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["Repository"]


class Repository(BaseModel):
    """Repository information response."""

    id: int

    default_branch: str

    full_name: str

    has_kater_structure: bool

    html_url: str

    is_empty: bool

    name: str

    owner: str

    private: bool
