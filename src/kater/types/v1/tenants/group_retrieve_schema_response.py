# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["GroupRetrieveSchemaResponse", "TenantGroup"]


class TenantGroup(BaseModel):
    kater_id: str
    """Unique Kater identifier"""

    name: str
    """Name identifier"""

    description: Optional[str] = None
    """Description text"""


class GroupRetrieveSchemaResponse(BaseModel):
    """Schema for tenant group configuration files"""

    tenant_groups: List[TenantGroup]
    """Array of tenant group configurations"""
