# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import v1_list_connections_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .tenants.tenants import (
    TenantsResource,
    AsyncTenantsResource,
    TenantsResourceWithRawResponse,
    AsyncTenantsResourceWithRawResponse,
    TenantsResourceWithStreamingResponse,
    AsyncTenantsResourceWithStreamingResponse,
)
from ...types.v1_list_connections_response import V1ListConnectionsResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def tenants(self) -> TenantsResource:
        return TenantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/kater-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/kater-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def list_connections(
        self,
        *,
        status: Literal["approved", "pending", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListConnectionsResponse:
        """
        List warehouse connections for the client.

        Filter connections by approval status using the `status` query parameter:

        - `approved` (default): Only approved connections (is_pending_approval=false)
        - `pending`: Only connections awaiting PR approval (is_pending_approval=true)
        - `all`: All connections regardless of approval status

        Pending connections include their approval PR URLs when available. Returns empty
        list if GitHub is not configured.

        RLS: Filtered to current client (DualClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, v1_list_connections_params.V1ListConnectionsParams),
            ),
            cast_to=V1ListConnectionsResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def tenants(self) -> AsyncTenantsResource:
        return AsyncTenantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/kater-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/kater-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def list_connections(
        self,
        *,
        status: Literal["approved", "pending", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListConnectionsResponse:
        """
        List warehouse connections for the client.

        Filter connections by approval status using the `status` query parameter:

        - `approved` (default): Only approved connections (is_pending_approval=false)
        - `pending`: Only connections awaiting PR approval (is_pending_approval=true)
        - `all`: All connections regardless of approval status

        Pending connections include their approval PR URLs when available. Returns empty
        list if GitHub is not configured.

        RLS: Filtered to current client (DualClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"status": status}, v1_list_connections_params.V1ListConnectionsParams
                ),
            ),
            cast_to=V1ListConnectionsResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.list_connections = to_raw_response_wrapper(
            v1.list_connections,
        )

    @cached_property
    def tenants(self) -> TenantsResourceWithRawResponse:
        return TenantsResourceWithRawResponse(self._v1.tenants)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.list_connections = async_to_raw_response_wrapper(
            v1.list_connections,
        )

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithRawResponse:
        return AsyncTenantsResourceWithRawResponse(self._v1.tenants)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.list_connections = to_streamed_response_wrapper(
            v1.list_connections,
        )

    @cached_property
    def tenants(self) -> TenantsResourceWithStreamingResponse:
        return TenantsResourceWithStreamingResponse(self._v1.tenants)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.list_connections = async_to_streamed_response_wrapper(
            v1.list_connections,
        )

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithStreamingResponse:
        return AsyncTenantsResourceWithStreamingResponse(self._v1.tenants)
