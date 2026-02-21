# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CombinationPreviewParams"]


class CombinationPreviewParams(TypedDict, total=False):
    combination: Required[str]
    """Comma-separated slot selections, same format as ResolveRequest.combination.

    Example: 'dimension=due_month,measure=compliance_rate'
    """

    connection_id: Required[str]
    """Connection to preview against"""

    query_ref: Required[str]
    """Query template reference (e.g. 'q:compliance_trend.\\__base')"""

    source: Optional[str]

    tenant_key: Optional[str]
    """Optional tenant key for multi-tenant execution"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
