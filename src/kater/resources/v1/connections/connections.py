# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import connection_list_connections_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .client.client import (
    ClientResource,
    AsyncClientResource,
    ClientResourceWithRawResponse,
    AsyncClientResourceWithRawResponse,
    ClientResourceWithStreamingResponse,
    AsyncClientResourceWithStreamingResponse,
)
from .tenant.tenant import (
    TenantResource,
    AsyncTenantResource,
    TenantResourceWithRawResponse,
    AsyncTenantResourceWithRawResponse,
    TenantResourceWithStreamingResponse,
    AsyncTenantResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.v1.connection_list_connections_response import ConnectionListConnectionsResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    """Manage database connections to your data warehouse"""

    @cached_property
    def client(self) -> ClientResource:
        return ClientResource(self._client)

    @cached_property
    def oauth(self) -> OAuthResource:
        """Tenant MCP credential management"""
        return OAuthResource(self._client)

    @cached_property
    def tenant(self) -> TenantResource:
        return TenantResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return ConnectionsResourceWithStreamingResponse(self)

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
    ) -> ConnectionListConnectionsResponse:
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
                query=maybe_transform(
                    {"status": status}, connection_list_connections_params.ConnectionListConnectionsParams
                ),
            ),
            cast_to=ConnectionListConnectionsResponse,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    """Manage database connections to your data warehouse"""

    @cached_property
    def client(self) -> AsyncClientResource:
        return AsyncClientResource(self._client)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        """Tenant MCP credential management"""
        return AsyncOAuthResource(self._client)

    @cached_property
    def tenant(self) -> AsyncTenantResource:
        return AsyncTenantResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncConnectionsResourceWithStreamingResponse(self)

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
    ) -> ConnectionListConnectionsResponse:
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
                    {"status": status}, connection_list_connections_params.ConnectionListConnectionsParams
                ),
            ),
            cast_to=ConnectionListConnectionsResponse,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.list_connections = to_raw_response_wrapper(
            connections.list_connections,
        )

    @cached_property
    def client(self) -> ClientResourceWithRawResponse:
        return ClientResourceWithRawResponse(self._connections.client)

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        """Tenant MCP credential management"""
        return OAuthResourceWithRawResponse(self._connections.oauth)

    @cached_property
    def tenant(self) -> TenantResourceWithRawResponse:
        return TenantResourceWithRawResponse(self._connections.tenant)


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.list_connections = async_to_raw_response_wrapper(
            connections.list_connections,
        )

    @cached_property
    def client(self) -> AsyncClientResourceWithRawResponse:
        return AsyncClientResourceWithRawResponse(self._connections.client)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        """Tenant MCP credential management"""
        return AsyncOAuthResourceWithRawResponse(self._connections.oauth)

    @cached_property
    def tenant(self) -> AsyncTenantResourceWithRawResponse:
        return AsyncTenantResourceWithRawResponse(self._connections.tenant)


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.list_connections = to_streamed_response_wrapper(
            connections.list_connections,
        )

    @cached_property
    def client(self) -> ClientResourceWithStreamingResponse:
        return ClientResourceWithStreamingResponse(self._connections.client)

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return OAuthResourceWithStreamingResponse(self._connections.oauth)

    @cached_property
    def tenant(self) -> TenantResourceWithStreamingResponse:
        return TenantResourceWithStreamingResponse(self._connections.tenant)


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.list_connections = async_to_streamed_response_wrapper(
            connections.list_connections,
        )

    @cached_property
    def client(self) -> AsyncClientResourceWithStreamingResponse:
        return AsyncClientResourceWithStreamingResponse(self._connections.client)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return AsyncOAuthResourceWithStreamingResponse(self._connections.oauth)

    @cached_property
    def tenant(self) -> AsyncTenantResourceWithStreamingResponse:
        return AsyncTenantResourceWithStreamingResponse(self._connections.tenant)
