# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CacheInvalidateParams"]


class CacheInvalidateParams(TypedDict, total=False):
    client_id: Required[str]
    """Client ID to invalidate cache entries for (mandatory)"""

    connection_id: Optional[str]
    """Optional connection ID for connection-scoped invalidation"""

    tenant_id: Optional[str]
    """Optional tenant ID for tenant-scoped invalidation"""
