# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GitHubCallbackParams"]


class GitHubCallbackParams(TypedDict, total=False):
    state: Required[str]
    """State token for CSRF validation"""

    code: Optional[str]
    """OAuth authorization code"""

    error: Optional[str]
    """OAuth error code from GitHub"""

    error_description: Optional[str]
    """OAuth error description"""

    installation_id: Optional[int]
    """GitHub App installation ID"""
