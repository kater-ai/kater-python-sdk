# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CompilerCompileDashboardParams"]


class CompilerCompileDashboardParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection to compile against"""

    dashboard_path: Required[str]
    """Relative path within the connection (e.g. 'dashboards/compliance_overview')"""

    source: Optional[str]

    filters: Optional[Dict[str, Union[str, SequenceNotStr[str], None]]]
    """Optional filter overrides from UI"""

    tenant_key: Optional[str]
    """Optional tenant key for multi-tenant execution"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
