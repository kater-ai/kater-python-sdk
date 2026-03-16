# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["ServerUpdateParams", "AllowedCapability"]


class ServerUpdateParams(TypedDict, total=False):
    allowed_capabilities: Optional[Iterable[AllowedCapability]]
    """Capabilities to expose as LLM tools"""

    enabled: Optional[bool]
    """Enable/disable toggle"""


class AllowedCapability(TypedDict, total=False):
    """A capability selected by the admin for LLM tool exposure."""

    description: Required[str]

    input_schema: Required[Annotated[Dict[str, object], PropertyInfo(alias="inputSchema")]]

    name: Required[str]
