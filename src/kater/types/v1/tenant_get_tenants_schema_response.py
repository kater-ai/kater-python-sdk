# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TenantGetTenantsSchemaResponse", "Tenant"]


class Tenant(BaseModel):
    kater_id: str
    """Unique Kater identifier"""

    tenant_key: str
    """Unique key identifier for the tenant (e.g., 'acme_corp')"""

    groups: Optional[List[str]] = None
    """References to tenant groups this tenant belongs to"""

    name: Optional[str] = None
    """Human-readable display name for the tenant"""


class TenantGetTenantsSchemaResponse(BaseModel):
    """Schema for tenant configuration files"""

    tenants: List[Tenant]
    """Array of tenant configurations"""
