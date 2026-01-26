# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .tenancy_type import TenancyType

__all__ = ["Client"]


class Client(BaseModel):
    """Response schema for a client/organization."""

    id: str

    can_auto_join_by_domain: bool

    created_at: datetime

    members_must_have_matching_domain: bool

    name: str

    tenancy_type: TenancyType
    """Type of tenancy for a client."""

    updated_at: datetime

    domain: Optional[str] = None

    logo_url: Optional[str] = None
