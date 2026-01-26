# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..client_user_role import ClientUserRole

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    email: Optional[str]

    first_name: Optional[str]

    last_name: Optional[str]

    password: Optional[str]

    picture_url: Optional[str]

    role: Optional[ClientUserRole]
    """Role of a user within a client organization."""

    username: Optional[str]
