# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .client_user_role import ClientUserRole

__all__ = ["ClientUser"]


class ClientUser(BaseModel):
    """Response schema for a client user."""

    id: str

    client_id: str

    created_at: datetime

    email: str

    email_confirmed: bool

    role: ClientUserRole
    """Role of a user within a client organization."""

    updated_at: datetime

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    picture_url: Optional[str] = None

    propel_auth_created_at: Optional[datetime] = None

    propel_auth_last_active_at: Optional[datetime] = None

    username: Optional[str] = None
