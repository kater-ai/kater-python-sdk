# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .manifest import Manifest
from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = ["CompilerCompileResponse", "Metadata"]


class Metadata(BaseModel):
    """Compilation metadata from the compiler."""

    dialect: str
    """SQL dialect used (e.g. 'snowflake')"""

    query_ref: str
    """Reference to the compiled query"""

    dimensions_used: Optional[List[str]] = None
    """Dimension names used in compilation"""

    filters_used: Optional[List[str]] = None
    """Filter names used in compilation"""

    measures_used: Optional[List[str]] = None
    """Measure names used in compilation"""

    views_used: Optional[List[str]] = None
    """View names used in compilation"""


class CompilerCompileResponse(BaseModel):
    """Response model for SQL compilation."""

    dialect: str
    """SQL dialect used (e.g. 'snowflake')"""

    success: bool
    """Whether compilation succeeded"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Compilation errors"""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""

    metadata: Optional[Metadata] = None
    """Compilation metadata from the compiler."""

    sql: Optional[str] = None
    """Generated SQL statement"""
