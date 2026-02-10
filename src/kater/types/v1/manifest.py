# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .manifest_entry import ManifestEntry

__all__ = ["Manifest"]


class Manifest(BaseModel):
    """Compilation manifest with all named objects."""

    generated_at: str

    objects: Dict[str, ManifestEntry]

    schema_version: Optional[str] = None
