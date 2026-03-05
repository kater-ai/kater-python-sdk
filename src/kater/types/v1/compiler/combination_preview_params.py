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

    query_id: Required[str]
    """UUID of the query template"""

    tenant_key: Required[str]
    """Tenant key for multi-tenant execution.

    Use 'kater_global_tenant' for no-tenancy clients.
    """

    source: Optional[str]

    pinned_variant: Optional[str]
    """Optional pinned variant name (e.g. '\\__base')."""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
