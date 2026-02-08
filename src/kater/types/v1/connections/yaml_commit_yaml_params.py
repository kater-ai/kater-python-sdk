# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["YamlCommitYamlParams"]


class YamlCommitYamlParams(TypedDict, total=False):
    yaml_content: Required[str]
    """Updated YAML content"""

    auto_merge: bool
    """If true, auto-merge the PR after creation"""
