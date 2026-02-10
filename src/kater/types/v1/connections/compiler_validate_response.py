# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = [
    "CompilerValidateResponse",
    "DependencyGraph",
    "DependencyGraphNodes",
    "Error",
    "Manifest",
    "ManifestObjects",
    "Warning",
]


class DependencyGraphNodes(BaseModel):
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


class DependencyGraph(BaseModel):
    """Dependency graph between schema objects."""

    edges: Dict[str, Dict[str, List[str]]]
    """Edge relationships with UUID string keys"""

    nodes: Dict[str, DependencyGraphNodes]
    """UUID string to node mapping"""


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


class Warning(BaseModel):
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


class CompilerValidateResponse(BaseModel):
    """Response model for schema validation."""

    success: bool
    """Whether validation passed without errors"""

    dependency_graph: Optional[DependencyGraph] = None
    """Dependency graph between schema objects."""

    errors: Optional[List[Error]] = None
    """Validation errors"""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""

    warnings: Optional[List[Warning]] = None
    """Validation warnings"""
