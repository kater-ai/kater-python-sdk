# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from .credentials import (
    CredentialsResource,
    AsyncCredentialsResource,
    CredentialsResourceWithRawResponse,
    AsyncCredentialsResourceWithRawResponse,
    CredentialsResourceWithStreamingResponse,
    AsyncCredentialsResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.v1.connections.tenant import mcp_list_params, mcp_get_audit_history_params
from ......types.v1.connections.tenant.mcp_list_response import McpListResponse
from ......types.v1.connections.tenant.mcp_get_audit_history_response import McpGetAuditHistoryResponse

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    """Tenant MCP credential management"""

    @cached_property
    def credentials(self) -> CredentialsResource:
        """Tenant MCP credential management"""
        return CredentialsResource(self._client)

    @cached_property
    def oauth(self) -> OAuthResource:
        """Tenant MCP credential management"""
        return OAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> McpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return McpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return McpResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        tenant_id: str,
        tenant_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpListResponse:
        """
        List active MCP servers for the client with per-user connection status.

        Returns servers where status='active', enabled=true, deleted_at IS NULL. For
        auth_type='none' servers, connection_status is always "connected". For other
        servers, connection status reflects the user's credential state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/tenant/mcp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tenant_id": tenant_id,
                        "tenant_user_id": tenant_user_id,
                    },
                    mcp_list_params.McpListParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=McpListResponse,
        )

    def get_audit_history(
        self,
        mcp_id: str,
        *,
        tenant_id: str,
        tenant_user_id: str,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpGetAuditHistoryResponse:
        """
        Get credential audit history for the current user's MCP server connection.

        Returns audit records across all credential rotations using the shared
        credential_key, ordered by created_at DESC.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return self._get(
            f"/api/v1/tenant/mcp/{mcp_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tenant_id": tenant_id,
                        "tenant_user_id": tenant_user_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    mcp_get_audit_history_params.McpGetAuditHistoryParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=McpGetAuditHistoryResponse,
        )


class AsyncMcpResource(AsyncAPIResource):
    """Tenant MCP credential management"""

    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        """Tenant MCP credential management"""
        return AsyncCredentialsResource(self._client)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        """Tenant MCP credential management"""
        return AsyncOAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncMcpResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        tenant_id: str,
        tenant_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpListResponse:
        """
        List active MCP servers for the client with per-user connection status.

        Returns servers where status='active', enabled=true, deleted_at IS NULL. For
        auth_type='none' servers, connection_status is always "connected". For other
        servers, connection status reflects the user's credential state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/tenant/mcp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tenant_id": tenant_id,
                        "tenant_user_id": tenant_user_id,
                    },
                    mcp_list_params.McpListParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=McpListResponse,
        )

    async def get_audit_history(
        self,
        mcp_id: str,
        *,
        tenant_id: str,
        tenant_user_id: str,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpGetAuditHistoryResponse:
        """
        Get credential audit history for the current user's MCP server connection.

        Returns audit records across all credential rotations using the shared
        credential_key, ordered by created_at DESC.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return await self._get(
            f"/api/v1/tenant/mcp/{mcp_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tenant_id": tenant_id,
                        "tenant_user_id": tenant_user_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    mcp_get_audit_history_params.McpGetAuditHistoryParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=McpGetAuditHistoryResponse,
        )


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.list = to_raw_response_wrapper(
            mcp.list,
        )
        self.get_audit_history = to_raw_response_wrapper(
            mcp.get_audit_history,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        """Tenant MCP credential management"""
        return CredentialsResourceWithRawResponse(self._mcp.credentials)

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        """Tenant MCP credential management"""
        return OAuthResourceWithRawResponse(self._mcp.oauth)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.list = async_to_raw_response_wrapper(
            mcp.list,
        )
        self.get_audit_history = async_to_raw_response_wrapper(
            mcp.get_audit_history,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        """Tenant MCP credential management"""
        return AsyncCredentialsResourceWithRawResponse(self._mcp.credentials)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        """Tenant MCP credential management"""
        return AsyncOAuthResourceWithRawResponse(self._mcp.oauth)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.list = to_streamed_response_wrapper(
            mcp.list,
        )
        self.get_audit_history = to_streamed_response_wrapper(
            mcp.get_audit_history,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return CredentialsResourceWithStreamingResponse(self._mcp.credentials)

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return OAuthResourceWithStreamingResponse(self._mcp.oauth)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.list = async_to_streamed_response_wrapper(
            mcp.list,
        )
        self.get_audit_history = async_to_streamed_response_wrapper(
            mcp.get_audit_history,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return AsyncCredentialsResourceWithStreamingResponse(self._mcp.credentials)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return AsyncOAuthResourceWithStreamingResponse(self._mcp.oauth)
