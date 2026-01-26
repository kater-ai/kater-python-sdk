# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .tenant import Tenant

__all__ = ["TenantListResponse"]

TenantListResponse: TypeAlias = List[Tenant]
