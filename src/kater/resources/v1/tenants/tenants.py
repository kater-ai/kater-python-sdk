# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import tenant_import_from_csv_params, tenant_import_from_warehouse_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.tenants.import_tenants_response import ImportTenantsResponse

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/kater-python#accessing-raw-response-data-eg-headers
        """
        return TenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/kater-python#with_streaming_response
        """
        return TenantsResourceWithStreamingResponse(self)

    def import_from_csv(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportTenantsResponse:
        """
        Import tenants from a CSV file using upsert semantics.

        Expected CSV format:

        - tenant_key (required): Unique tenant identifier
        - tenant_name (optional): Human-readable name
        - group_names (optional): Comma-separated list of group names

        Creates new tenants and updates existing ones with new name/groups. Groups are
        added additively (not replaced) and auto-created if needed.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ValidationError: If CSV format is invalid (400)
        TenantCreationNotAllowedError: If tenancy type is NONE (400)

        Args:
          file: CSV file with tenant data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/tenants/import/csv",
            body=maybe_transform(body, tenant_import_from_csv_params.TenantImportFromCsvParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportTenantsResponse,
        )

    def import_from_warehouse(
        self,
        *,
        connection_id: str,
        database: str,
        schema: str,
        table: str,
        tenant_key_column: str,
        tenant_group_column: Optional[str] | Omit = omit,
        tenant_name_column: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportTenantsResponse:
        """
        Import tenants from a warehouse table using upsert semantics.

        Creates new tenants and updates existing ones with new name/groups. Groups are
        added additively (not replaced).

        Streams data from the warehouse in batches to handle large datasets without
        loading everything into memory.

        For tenants with groups, groups are aggregated per tenant key and auto-created
        if they don't exist.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ConnectionNotFoundError: If the connection doesn't exist (404)
        TenantCreationNotAllowedError: If tenancy type is NONE (400)

        Args:
          connection_id: Warehouse connection ID to query

          database: Database name containing the tenant table

          schema: Schema name containing the tenant table

          table: Table name containing tenant data

          tenant_key_column: Column name for tenant key

          tenant_group_column: Column name for tenant group (optional)

          tenant_name_column: Column name for tenant display name (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/tenants/import/warehouse",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "database": database,
                    "schema": schema,
                    "table": table,
                    "tenant_key_column": tenant_key_column,
                    "tenant_group_column": tenant_group_column,
                    "tenant_name_column": tenant_name_column,
                },
                tenant_import_from_warehouse_params.TenantImportFromWarehouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportTenantsResponse,
        )


class AsyncTenantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/kater-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/kater-python#with_streaming_response
        """
        return AsyncTenantsResourceWithStreamingResponse(self)

    async def import_from_csv(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportTenantsResponse:
        """
        Import tenants from a CSV file using upsert semantics.

        Expected CSV format:

        - tenant_key (required): Unique tenant identifier
        - tenant_name (optional): Human-readable name
        - group_names (optional): Comma-separated list of group names

        Creates new tenants and updates existing ones with new name/groups. Groups are
        added additively (not replaced) and auto-created if needed.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ValidationError: If CSV format is invalid (400)
        TenantCreationNotAllowedError: If tenancy type is NONE (400)

        Args:
          file: CSV file with tenant data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/tenants/import/csv",
            body=await async_maybe_transform(body, tenant_import_from_csv_params.TenantImportFromCsvParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportTenantsResponse,
        )

    async def import_from_warehouse(
        self,
        *,
        connection_id: str,
        database: str,
        schema: str,
        table: str,
        tenant_key_column: str,
        tenant_group_column: Optional[str] | Omit = omit,
        tenant_name_column: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportTenantsResponse:
        """
        Import tenants from a warehouse table using upsert semantics.

        Creates new tenants and updates existing ones with new name/groups. Groups are
        added additively (not replaced).

        Streams data from the warehouse in batches to handle large datasets without
        loading everything into memory.

        For tenants with groups, groups are aggregated per tenant key and auto-created
        if they don't exist.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ConnectionNotFoundError: If the connection doesn't exist (404)
        TenantCreationNotAllowedError: If tenancy type is NONE (400)

        Args:
          connection_id: Warehouse connection ID to query

          database: Database name containing the tenant table

          schema: Schema name containing the tenant table

          table: Table name containing tenant data

          tenant_key_column: Column name for tenant key

          tenant_group_column: Column name for tenant group (optional)

          tenant_name_column: Column name for tenant display name (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/tenants/import/warehouse",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "database": database,
                    "schema": schema,
                    "table": table,
                    "tenant_key_column": tenant_key_column,
                    "tenant_group_column": tenant_group_column,
                    "tenant_name_column": tenant_name_column,
                },
                tenant_import_from_warehouse_params.TenantImportFromWarehouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportTenantsResponse,
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.import_from_csv = to_raw_response_wrapper(
            tenants.import_from_csv,
        )
        self.import_from_warehouse = to_raw_response_wrapper(
            tenants.import_from_warehouse,
        )


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.import_from_csv = async_to_raw_response_wrapper(
            tenants.import_from_csv,
        )
        self.import_from_warehouse = async_to_raw_response_wrapper(
            tenants.import_from_warehouse,
        )


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.import_from_csv = to_streamed_response_wrapper(
            tenants.import_from_csv,
        )
        self.import_from_warehouse = to_streamed_response_wrapper(
            tenants.import_from_warehouse,
        )


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.import_from_csv = async_to_streamed_response_wrapper(
            tenants.import_from_csv,
        )
        self.import_from_warehouse = async_to_streamed_response_wrapper(
            tenants.import_from_warehouse,
        )
