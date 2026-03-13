# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["ServerRediscoverResponse"]


class ServerRediscoverResponse(BaseModel):
    """Response model for MCP server capability discovery."""

    capabilities: List[Dict[str, object]]

    capabilities_count: int

    status: Literal["pending_setup", "active"]
    """Lifecycle status of an MCP server registration."""

    can_skip: Optional[bool] = None

    error: Optional[str] = None
