# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..create_tenant_param import CreateTenantParam

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    tenants: Required[Iterable[CreateTenantParam]]
    """List of tenants to create"""
