# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = ["McpListResponse", "McpListResponseItem"]


class McpListResponseItem(BaseModel):
    """Response model for a tenant-visible MCP server with connection status."""

    auth_type: Literal["api_key", "oauth2", "none"]
    """Authentication type for MCP server connections."""

    connection_status: str

    mcp_id: str

    name: str

    slug: str

    description: Optional[str] = None


McpListResponse: TypeAlias = List[McpListResponseItem]
