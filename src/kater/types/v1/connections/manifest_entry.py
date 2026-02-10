# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ManifestEntry"]


class ManifestEntry(BaseModel):
    """A single object entry in the manifest."""

    kater_id: str

    name: str

    type: str

    label: Optional[str] = None

    parent_id: Optional[str] = None

    source_file: Optional[str] = None
