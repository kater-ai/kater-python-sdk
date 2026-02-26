# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["TenantImportFromCsvParams"]


class TenantImportFromCsvParams(TypedDict, total=False):
    file: Required[FileTypes]
    """CSV file with tenant data"""

    source: Optional[str]

    attribute_columns: Optional[str]
    """JSON mapping: attribute_name -> csv_column_name"""

    x_kater_cli_id: Annotated[str, PropertyInfo(alias="X-Kater-CLI-ID")]
