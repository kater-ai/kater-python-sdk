# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel

__all__ = [
    "CompilerEnumerateResponse",
    "Combination",
    "RequiredFields",
    "VariableDefinition",
    "VariableDefinitionAllowedValuesStatic",
    "VariableDefinitionConstraints",
]


class Combination(BaseModel):
    """A single valid query configuration."""

    query_ref: str
    """Query template reference (e.g. 'q:COMPLIANCE_OVERVIEW')"""

    widget_category: str
    """Widget category (e.g. 'axis', 'table')"""

    combination_id: Optional[str] = None
    """Deterministic UUID v5 for this combination"""

    query_kater_id: Optional[str] = None
    """UUID of the query template"""

    query_label: Optional[str] = None
    """Human-readable label for the query"""

    roles: Optional[Dict[str, str]] = None
    """Field-to-role mapping (e.g. {'due_month': 'x_axis'})"""

    selected_calculations: Optional[List[str]] = None
    """Selected optional calculation names"""

    selected_dimensions: Optional[List[str]] = None
    """Selected optional dimension names"""

    selected_filters: Optional[List[str]] = None
    """Selected optional filter names"""

    selected_measures: Optional[List[str]] = None
    """Selected optional measure names"""

    variable_assignments: Optional[Dict[str, object]] = None
    """Variable name to value assignments"""

    widget_type: Optional[str] = None
    """Resolved widget type (e.g. 'axis_metric_by_dimensiondate')"""


class RequiredFields(BaseModel):
    """Required slot fields for a query (always included in every combination)."""

    calculations: Optional[List[str]] = None

    dimensions: Optional[List[str]] = None

    filters: Optional[List[str]] = None

    measures: Optional[List[str]] = None


class VariableDefinitionAllowedValuesStatic(BaseModel):
    """A value with optional display label"""

    value: Union[str, float, bool]
    """The actual value"""

    label: Optional[str] = None
    """Human-readable label for the value"""


class VariableDefinitionConstraints(BaseModel):
    """Serialisable constraints for a variable."""

    max: Optional[float] = None

    max_length: Optional[int] = None

    min: Optional[float] = None

    step: Optional[float] = None


class VariableDefinition(BaseModel):
    """A variable's schema exposed to the query-builder UI."""

    is_runtime: bool
    """
    True = dynamic (entered at run time); False = static (values baked into
    combinations)
    """

    name: str

    type: str
    """Variable data type, e.g. STRING, INT, DATE, BOOL, STRING[]"""

    allowed_values_column_kater_id: Optional[str] = None
    """kater_id of the dimension column for from_column variables"""

    allowed_values_static: Optional[List[VariableDefinitionAllowedValuesStatic]] = None
    """Non-null when is_runtime=False or type has a static list"""

    constraints: Optional[VariableDefinitionConstraints] = None
    """Serialisable constraints for a variable."""

    default: Union[str, float, bool, List[Union[str, float, bool]], None] = None

    filter_names: Optional[List[str]] = None
    """
    Names of the optional filters that use this variable (non-empty when filter_only
    is true)
    """

    filter_only: Optional[bool] = None
    """True if the variable is used only in optional filter SQL"""

    label: Optional[str] = None


class CompilerEnumerateResponse(BaseModel):
    """Response model for query combination enumeration."""

    combinations: List[Combination]
    """All valid query configurations"""

    total_count: int
    """Total number of combinations"""

    field_labels: Optional[Dict[str, Dict[str, str]]] = None
    """Display labels for slot fields, keyed by query_kater_id then field name"""

    required_fields: Optional[Dict[str, RequiredFields]] = None
    """Required slot fields keyed by query_kater_id"""

    variable_definitions: Optional[Dict[str, List[VariableDefinition]]] = None
    """Variable definitions keyed by query_kater_id"""
