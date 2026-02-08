# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["YamlRetrieveResponse"]


class YamlRetrieveResponse(BaseModel):
    """Response for reading connection.yaml from repo."""

    folder_name: str
    """Folder name in the repo (e.g. 'prod_db_connection')"""

    yaml_content: str
    """Raw YAML content of connection.yaml"""
