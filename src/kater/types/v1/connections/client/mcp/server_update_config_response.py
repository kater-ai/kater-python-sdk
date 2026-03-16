# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["ServerUpdateConfigResponse"]


class ServerUpdateConfigResponse(BaseModel):
    """Response model for a registered MCP server."""

    id: str

    allowed_capabilities: List[object]

    auth_type: Literal["api_key", "oauth2", "none"]
    """Authentication type for MCP server connections."""

    capabilities: List[object]

    created_at: datetime

    enabled: bool

    name: str

    server_url: str

    slug: str

    status: Literal["pending_setup", "active"]
    """Lifecycle status of an MCP server registration."""

    transport: Literal["auto", "streamable_http", "sse"]
    """Transport protocol for MCP server communication."""
