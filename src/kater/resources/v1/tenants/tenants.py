# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .import_ import (
    ImportResource,
    AsyncImportResource,
    ImportResourceWithRawResponse,
    AsyncImportResourceWithRawResponse,
    ImportResourceWithStreamingResponse,
    AsyncImportResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import tenant_create_params, tenant_update_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.tenant import Tenant
from ....types.v1.tenant_list_response import TenantListResponse

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def import_(self) -> ImportResource:
        return ImportResource(self._client)

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

    def create(
        self,
        *,
        tenant_key: str,
        connection_id: Optional[str] | Omit = omit,
        database_name: Optional[str] | Omit = omit,
        group_names: Optional[SequenceNotStr[str]] | Omit = omit,
        tenant_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Create a new tenant.

        Validates the client's tenancy type and creates the tenant accordingly:

        - ROW tenancy: Creates tenant with optional group associations
        - DATABASE tenancy: Requires database_name, creates tenant with database
          association
        - NONE tenancy: Returns error (tenant creation not allowed)

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenant_key: Unique tenant identifier within the client

          connection_id: Connection ID (required for DATABASE tenancy type)

          database_name: Database name (required for DATABASE tenancy type)

          group_names: List of group names to associate with the tenant

          tenant_name: Human-readable tenant name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/tenants",
            body=maybe_transform(
                {
                    "tenant_key": tenant_key,
                    "connection_id": connection_id,
                    "database_name": database_name,
                    "group_names": group_names,
                    "tenant_name": tenant_name,
                },
                tenant_create_params.TenantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    def retrieve(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Get a single tenant by ID.

        Returns the tenant with associated groups and databases.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: TenantNotFoundError: If tenant doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            f"/api/v1/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    def update(
        self,
        tenant_id: str,
        *,
        connection_id: Optional[str] | Omit = omit,
        database_name: Optional[str] | Omit = omit,
        group_names: Optional[SequenceNotStr[str]] | Omit = omit,
        tenant_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Update a tenant.

        Updates tenant metadata, group associations, and/or database associations. Group
        associations use replace semantics:

        - Omit group_names to leave existing associations unchanged
        - Pass empty list to remove all group associations
        - Pass list of names to replace all associations

        Database associations (DATABASE tenancy only):

        - Both connection_id and database_name must be provided together
        - Replaces existing database association

        RLS: Filtered to current client (ClientRLSDB).

        Raises: TenantNotFoundError: If tenant doesn't exist (404)

        Args:
          connection_id: Connection ID for database association (required with database_name)

          database_name: Database name for association (required with connection_id)

          group_names: New list of group names (replaces all existing associations)

          tenant_name: New human-readable tenant name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._patch(
            f"/api/v1/tenants/{tenant_id}",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "database_name": database_name,
                    "group_names": group_names,
                    "tenant_name": tenant_name,
                },
                tenant_update_params.TenantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantListResponse:
        """
        List all tenants for the client.

        Returns tenants with their associated groups and databases.

        RLS: Filtered to current client (ClientRLSDB).
        """
        return self._get(
            "/api/v1/tenants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantListResponse,
        )

    def delete(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a tenant.

        Soft-deletes the tenant and its group/database associations.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: TenantNotFoundError: If tenant doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTenantsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def import_(self) -> AsyncImportResource:
        return AsyncImportResource(self._client)

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

    async def create(
        self,
        *,
        tenant_key: str,
        connection_id: Optional[str] | Omit = omit,
        database_name: Optional[str] | Omit = omit,
        group_names: Optional[SequenceNotStr[str]] | Omit = omit,
        tenant_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Create a new tenant.

        Validates the client's tenancy type and creates the tenant accordingly:

        - ROW tenancy: Creates tenant with optional group associations
        - DATABASE tenancy: Requires database_name, creates tenant with database
          association
        - NONE tenancy: Returns error (tenant creation not allowed)

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenant_key: Unique tenant identifier within the client

          connection_id: Connection ID (required for DATABASE tenancy type)

          database_name: Database name (required for DATABASE tenancy type)

          group_names: List of group names to associate with the tenant

          tenant_name: Human-readable tenant name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/tenants",
            body=await async_maybe_transform(
                {
                    "tenant_key": tenant_key,
                    "connection_id": connection_id,
                    "database_name": database_name,
                    "group_names": group_names,
                    "tenant_name": tenant_name,
                },
                tenant_create_params.TenantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    async def retrieve(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Get a single tenant by ID.

        Returns the tenant with associated groups and databases.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: TenantNotFoundError: If tenant doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            f"/api/v1/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    async def update(
        self,
        tenant_id: str,
        *,
        connection_id: Optional[str] | Omit = omit,
        database_name: Optional[str] | Omit = omit,
        group_names: Optional[SequenceNotStr[str]] | Omit = omit,
        tenant_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Update a tenant.

        Updates tenant metadata, group associations, and/or database associations. Group
        associations use replace semantics:

        - Omit group_names to leave existing associations unchanged
        - Pass empty list to remove all group associations
        - Pass list of names to replace all associations

        Database associations (DATABASE tenancy only):

        - Both connection_id and database_name must be provided together
        - Replaces existing database association

        RLS: Filtered to current client (ClientRLSDB).

        Raises: TenantNotFoundError: If tenant doesn't exist (404)

        Args:
          connection_id: Connection ID for database association (required with database_name)

          database_name: Database name for association (required with connection_id)

          group_names: New list of group names (replaces all existing associations)

          tenant_name: New human-readable tenant name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._patch(
            f"/api/v1/tenants/{tenant_id}",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "database_name": database_name,
                    "group_names": group_names,
                    "tenant_name": tenant_name,
                },
                tenant_update_params.TenantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantListResponse:
        """
        List all tenants for the client.

        Returns tenants with their associated groups and databases.

        RLS: Filtered to current client (ClientRLSDB).
        """
        return await self._get(
            "/api/v1/tenants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantListResponse,
        )

    async def delete(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a tenant.

        Soft-deletes the tenant and its group/database associations.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: TenantNotFoundError: If tenant doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.create = to_raw_response_wrapper(
            tenants.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tenants.update,
        )
        self.list = to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = to_raw_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._tenants.batch)

    @cached_property
    def import_(self) -> ImportResourceWithRawResponse:
        return ImportResourceWithRawResponse(self._tenants.import_)


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.create = async_to_raw_response_wrapper(
            tenants.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tenants.update,
        )
        self.list = async_to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._tenants.batch)

    @cached_property
    def import_(self) -> AsyncImportResourceWithRawResponse:
        return AsyncImportResourceWithRawResponse(self._tenants.import_)


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.create = to_streamed_response_wrapper(
            tenants.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tenants.update,
        )
        self.list = to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = to_streamed_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._tenants.batch)

    @cached_property
    def import_(self) -> ImportResourceWithStreamingResponse:
        return ImportResourceWithStreamingResponse(self._tenants.import_)


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.create = async_to_streamed_response_wrapper(
            tenants.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tenants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._tenants.batch)

    @cached_property
    def import_(self) -> AsyncImportResourceWithStreamingResponse:
        return AsyncImportResourceWithStreamingResponse(self._tenants.import_)
