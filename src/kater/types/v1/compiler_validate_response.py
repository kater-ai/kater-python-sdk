# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = [
    "CompilerValidateResponse",
    "ConnectionResult",
    "ConnectionResultDependencyGraph",
    "ConnectionResultDependencyGraphNodes",
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


class ConnectionResultDependencyGraph(BaseModel):
    """Dependency graph between schema objects."""

    edges: Dict[str, Dict[str, List[str]]]
    """Edge relationships with UUID string keys"""

    nodes: Dict[str, ConnectionResultDependencyGraphNodes]
    """UUID string to node mapping"""


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

    warnings: Optional[List[CompilerErrorItem]] = None
    """Validation warnings"""
