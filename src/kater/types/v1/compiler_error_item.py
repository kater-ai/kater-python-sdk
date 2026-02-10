# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CompilerErrorItem"]


class CompilerErrorItem(BaseModel):
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
