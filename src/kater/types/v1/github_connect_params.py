# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["GitHubConnectParams"]


class GitHubConnectParams(TypedDict, total=False):
    return_to: Optional[str]
    """
    Frontend path to redirect to after OAuth success (e.g., '/' or
    '/settings/github')
    """
