# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .tenancy_type import TenancyType

__all__ = ["ClientUpdateParams"]


class ClientUpdateParams(TypedDict, total=False):
    can_auto_join_by_domain: Optional[bool]

    domain: Optional[str]

    logo_url: Optional[str]

    members_must_have_matching_domain: Optional[bool]

    name: Optional[str]

    tenancy_type: Optional[TenancyType]
    """Type of tenancy for a client."""
