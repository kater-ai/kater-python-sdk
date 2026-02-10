# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["CompilerResolveParams"]


class CompilerResolveParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection to resolve against"""

    query_ref: Required[str]
    """Reference to the query template (e.g. 'ref(MY_QUERY)')"""

    source: Optional[str]

    include_calculations: SequenceNotStr[str]
    """Calculation names to include"""

    include_dimensions: SequenceNotStr[str]
    """Dimension names to include"""

    include_filters: SequenceNotStr[str]
    """Filter names to include"""

    include_measures: SequenceNotStr[str]
    """Measure names to include"""

    variables: Dict[str, object]
    """User-selected variable values"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
