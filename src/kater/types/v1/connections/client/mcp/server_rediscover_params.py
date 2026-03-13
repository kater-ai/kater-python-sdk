# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ServerRediscoverParams"]


class ServerRediscoverParams(TypedDict, total=False):
    test_api_key: Optional[str]
    """Test API key (never persisted)"""

    test_bearer_token: Optional[str]
    """Test bearer token (never persisted)"""
