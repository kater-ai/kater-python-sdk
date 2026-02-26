# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .manifest import Manifest
from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = [
    "CompilerValidateResponse",
    "ConnectionResult",
    "ConnectionResultDependencyGraph",
    "ConnectionResultDependencyGraphNodes",
    "ConnectionResultRefFix",
    "ConnectionResultRefFixReplacement",
]


class ConnectionResultDependencyGraphNodes(BaseModel):
    """A node in the dependency graph."""

    file: str
    """Source file path"""

    fqn: str
    """Fully qualified name (e.g. 'dim_customer.region')"""

    kater_id: str
    """UUID of the schema object"""

    line: int
    """Line number in source file"""

    node_type: str
    """Node type: QUERY, VIEW, DIMENSION, MEASURE, FILTER, EXPRESSION"""

    column: Optional[int] = None
    """Column number in source file"""


class ConnectionResultDependencyGraph(BaseModel):
    """Dependency graph between schema objects."""

    edges: Dict[str, Dict[str, List[str]]]
    """Edge relationships with UUID string keys"""

    nodes: Dict[str, ConnectionResultDependencyGraphNodes]
    """UUID string to node mapping"""


class ConnectionResultRefFixReplacement(BaseModel):
    """A single ref replacement within a file."""

    file_path: str
    """Path to the file containing the replaced ref"""

    line_number: int
    """Line number where the replacement occurred"""

    new_ref: str
    """Updated reference string"""

    old_ref: str
    """Original reference string"""


class ConnectionResultRefFix(BaseModel):
    """A file that was modified by auto-fix with its replacements."""

    file_path: str
    """Path to the modified file"""

    new_content: str
    """Full updated file content after fixes"""

    replacements: List[ConnectionResultRefFixReplacement]
    """Individual ref replacements made in this file"""


class ConnectionResult(BaseModel):
    """Validation result for a single connection."""

    connection_id: str
    """Connection UUID"""

    connection_name: str
    """Connection name"""

    success: bool
    """Whether this connection validated without errors"""

    dependency_graph: Optional[ConnectionResultDependencyGraph] = None
    """Dependency graph between schema objects."""

    errors: Optional[List[CompilerErrorItem]] = None
    """Validation errors for this connection"""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""

    ref_fixes: Optional[List[ConnectionResultRefFix]] = None
    """Files auto-fixed due to renamed refs. None when no renames detected."""

    warnings: Optional[List[CompilerErrorItem]] = None
    """Validation warnings for this connection"""


class CompilerValidateResponse(BaseModel):
    """Response model for schema validation."""

    success: bool
    """Whether validation passed without errors"""

    connection_results: Optional[List[ConnectionResult]] = None
    """Per-connection validation results with dependency graphs"""

    errors: Optional[List[CompilerErrorItem]] = None
    """Validation errors"""

    request_id: Optional[str] = None
    """Write-back request ID.

    Non-null when files were dispatched to CLI via WebSocket.
    """

    warnings: Optional[List[CompilerErrorItem]] = None
    """Validation warnings"""
