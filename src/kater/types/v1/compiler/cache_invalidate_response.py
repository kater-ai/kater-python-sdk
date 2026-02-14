# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CacheInvalidateResponse"]


class CacheInvalidateResponse(BaseModel):
    """Response from cache invalidation."""

    entries_invalidated: int
    """Number of cache entries removed"""
