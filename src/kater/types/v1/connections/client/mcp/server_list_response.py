# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ......_models import BaseModel

__all__ = ["ServerListResponse", "ServerListResponseItem"]


class ServerListResponseItem(BaseModel):
    """Response model for a single server in the list."""

    id: str

    allowed_capabilities_count: int

    auth_type: Literal["api_key", "oauth2", "none"]
    """Authentication type for MCP server connections."""

    capabilities_count: int

    created_at: datetime

    enabled: bool

    name: str

    server_url: str

    slug: str

    status: Literal["pending_setup", "active"]
    """Lifecycle status of an MCP server registration."""

    transport: Literal["auto", "streamable_http", "sse"]
    """Transport protocol for MCP server communication."""


ServerListResponse: TypeAlias = List[ServerListResponseItem]
