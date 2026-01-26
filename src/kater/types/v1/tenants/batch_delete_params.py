# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["BatchDeleteParams"]


class BatchDeleteParams(TypedDict, total=False):
    tenant_ids: Required[SequenceNotStr[str]]
    """List of tenant IDs to delete"""
