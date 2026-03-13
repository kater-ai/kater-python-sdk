# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServerCreateParams"]


class ServerCreateParams(TypedDict, total=False):
    name: Required[str]
    """Display name"""

    server_url: Required[str]
    """HTTPS URL of the MCP server"""

    slug: Required[str]
    """Unique snake_case identifier"""

    auth_type: Literal["api_key", "oauth2", "none"]
    """Authentication type"""

    description: Optional[str]
    """Optional description"""

    oauth_authorize_url: Optional[str]
    """OAuth2 authorize URL"""

    oauth_client_id: Optional[str]
    """OAuth2 client ID"""

    oauth_client_secret: Optional[str]
    """OAuth2 client secret (encrypted)"""

    oauth_revoke_url: Optional[str]
    """OAuth2 revoke URL (optional)"""

    oauth_scopes_requested: Optional[str]
    """OAuth2 scopes"""

    oauth_token_url: Optional[str]
    """OAuth2 token URL"""

    terms_acknowledged: bool
    """Must be true to accept security terms"""

    transport: Literal["auto", "streamable_http", "sse"]
    """Transport protocol"""
