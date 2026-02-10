# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["CompilerCompileResponse", "Error", "Manifest", "ManifestObjects", "Metadata"]


class Error(BaseModel):
    """A single compiler validation or compilation error."""

    code: str
    """Machine-readable error code"""

    message: str
    """Human-readable error description"""

    file: Optional[str] = None
    """Source file path where the error occurred"""

    line: Optional[int] = None
    """Line number in the source file"""

    ref: Optional[str] = None
    """Reference to the source element (e.g. view or query name)"""

    remediation: Optional[str] = None
    """Suggested fix for this error"""


class ManifestObjects(BaseModel):
    """A single object entry in the manifest."""

    kater_id: str

    name: str

    type: str

    label: Optional[str] = None

    parent_id: Optional[str] = None

    source_file: Optional[str] = None


class Manifest(BaseModel):
    """Compilation manifest with all named objects."""

    generated_at: str

    objects: Dict[str, ManifestObjects]

    schema_version: Optional[str] = None


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

    errors: Optional[List[Error]] = None
    """Compilation errors"""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""

    metadata: Optional[Metadata] = None
    """Compilation metadata from the compiler."""

    sql: Optional[str] = None
    """Generated SQL statement"""
