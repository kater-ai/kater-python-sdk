# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CompilerResolveParams"]


class CompilerResolveParams(TypedDict, total=False):
    connection_id: Required[str]
    """Connection to resolve against"""

    query_ref: Required[str]
    """Reference to the query template (e.g. 'ref(MY_QUERY)')"""

    source: Optional[str]

    combination: str
    """Comma-separated slot selections and variable assignments.

    Reserved keys: measure, dimension, filter, calculation. All other keys are
    variable assignments. Example: 'measure=Compliance
    Rate,dimension=Department,breakdown=region'
    """

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
