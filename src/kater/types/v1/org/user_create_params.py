# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..client_user_role import ClientUserRole

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    email: Required[str]

    password: Required[str]

    first_name: Optional[str]

    last_name: Optional[str]

    role: ClientUserRole
    """Role of a user within a client organization."""

    username: Optional[str]
