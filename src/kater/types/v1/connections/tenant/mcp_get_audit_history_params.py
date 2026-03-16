# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["McpGetAuditHistoryParams"]


class McpGetAuditHistoryParams(TypedDict, total=False):
    tenant_id: Required[str]

    tenant_user_id: Required[str]

    cursor: Optional[str]

    limit: int
