# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ManifestRegenerateAndCreatePrParams"]


class ManifestRegenerateAndCreatePrParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection kater_id to regenerate and commit manifest for"""

    source: Optional[str]

    include_dependency_graph: bool
    """Also include .kater/dependency_graph.yaml in the PR when available."""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
