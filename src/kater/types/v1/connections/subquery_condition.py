# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SubqueryCondition"]


class SubqueryCondition(BaseModel):
    """A subquery condition for EXISTS/NOT EXISTS filters"""

    from_: str = FieldInfo(alias="from")
    """Reference to the source view/table for the subquery"""

    where: List[str]
    """WHERE conditions for the subquery"""
