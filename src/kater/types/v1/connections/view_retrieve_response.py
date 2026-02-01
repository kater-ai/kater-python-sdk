# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ViewRetrieveResponse"]


class ViewRetrieveResponse(BaseModel):
    """Response for a single view file's content."""

    branch: str
    """Branch the file was read from"""

    content: str
    """YAML file content"""

    name: str
    """File name (e.g., 'customers.yaml')"""

    path: str
    """Full path relative to connection folder"""
