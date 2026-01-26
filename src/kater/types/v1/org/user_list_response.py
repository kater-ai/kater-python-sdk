# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ..client_user import ClientUser

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    """Response schema for listing client users."""

    total: int

    users: List[ClientUser]
