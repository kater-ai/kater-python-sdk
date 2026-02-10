# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .manifest import Manifest
from ...._models import BaseModel
from .compiler_error_item import CompilerErrorItem

__all__ = ["CompilerValidateResponse", "DependencyGraph", "DependencyGraphNodes"]


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


class CompilerValidateResponse(BaseModel):
    """Response model for schema validation."""

    success: bool
    """Whether validation passed without errors"""

    dependency_graph: Optional[DependencyGraph] = None
    """Dependency graph between schema objects."""

    errors: Optional[List[CompilerErrorItem]] = None
    """Validation errors"""

    manifest: Optional[Manifest] = None
    """Compilation manifest with all named objects."""

    warnings: Optional[List[CompilerErrorItem]] = None
    """Validation warnings"""
