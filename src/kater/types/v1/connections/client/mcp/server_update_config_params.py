# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ServerUpdateConfigParams"]


class ServerUpdateConfigParams(TypedDict, total=False):
    auth_type: Optional[Literal["api_key", "oauth2", "none"]]
    """Authentication type for MCP server connections."""

    description: Optional[str]

    name: Optional[str]

    oauth_authorize_url: Optional[str]

    oauth_client_id: Optional[str]

    oauth_client_secret: Optional[str]

    oauth_revoke_url: Optional[str]

    oauth_scopes_requested: Optional[str]

    oauth_token_url: Optional[str]

    server_url: Optional[str]

    transport: Optional[Literal["auto", "streamable_http", "sse"]]
    """Transport protocol for MCP server communication."""
