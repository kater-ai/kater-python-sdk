# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, SequenceNotStr, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.groups import tenant_add_params
from ....types.v1.groups.tenant_add_response import TenantAddResponse

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return TenantsResourceWithStreamingResponse(self)

    def add(
        self,
        group_id: str,
        *,
        tenant_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantAddResponse:
        """Add tenants to a group.

        Accepts a list of tenant IDs.

        Returns detailed results showing which tenants
        were added, which were already members, and which don't exist.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: GroupNotFoundError: If group doesn't exist (404)

        Args:
          tenant_ids: List of tenant IDs to add to the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            f"/api/v1/groups/{group_id}/tenants",
            body=maybe_transform({"tenant_ids": tenant_ids}, tenant_add_params.TenantAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantAddResponse,
        )

    def remove(
        self,
        tenant_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a tenant from a group.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: GroupNotFoundError: If group doesn't exist (404) TenantNotFoundError: If
        tenant is not a member of the group (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/groups/{group_id}/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTenantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncTenantsResourceWithStreamingResponse(self)

    async def add(
        self,
        group_id: str,
        *,
        tenant_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantAddResponse:
        """Add tenants to a group.

        Accepts a list of tenant IDs.

        Returns detailed results showing which tenants
        were added, which were already members, and which don't exist.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: GroupNotFoundError: If group doesn't exist (404)

        Args:
          tenant_ids: List of tenant IDs to add to the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            f"/api/v1/groups/{group_id}/tenants",
            body=await async_maybe_transform({"tenant_ids": tenant_ids}, tenant_add_params.TenantAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantAddResponse,
        )

    async def remove(
        self,
        tenant_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a tenant from a group.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: GroupNotFoundError: If group doesn't exist (404) TenantNotFoundError: If
        tenant is not a member of the group (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/groups/{group_id}/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.add = to_raw_response_wrapper(
            tenants.add,
        )
        self.remove = to_raw_response_wrapper(
            tenants.remove,
        )


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.add = async_to_raw_response_wrapper(
            tenants.add,
        )
        self.remove = async_to_raw_response_wrapper(
            tenants.remove,
        )


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.add = to_streamed_response_wrapper(
            tenants.add,
        )
        self.remove = to_streamed_response_wrapper(
            tenants.remove,
        )


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.add = async_to_streamed_response_wrapper(
            tenants.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            tenants.remove,
        )
