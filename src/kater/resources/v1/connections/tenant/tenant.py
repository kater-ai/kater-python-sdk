# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .mcp.mcp import (
    McpResource,
    AsyncMcpResource,
    McpResourceWithRawResponse,
    AsyncMcpResourceWithRawResponse,
    McpResourceWithStreamingResponse,
    AsyncMcpResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TenantResource", "AsyncTenantResource"]


class TenantResource(SyncAPIResource):
    @cached_property
    def mcp(self) -> McpResource:
        """Tenant MCP credential management"""
        return McpResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TenantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return TenantResourceWithStreamingResponse(self)


class AsyncTenantResource(AsyncAPIResource):
    @cached_property
    def mcp(self) -> AsyncMcpResource:
        """Tenant MCP credential management"""
        return AsyncMcpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncTenantResourceWithStreamingResponse(self)


class TenantResourceWithRawResponse:
    def __init__(self, tenant: TenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def mcp(self) -> McpResourceWithRawResponse:
        """Tenant MCP credential management"""
        return McpResourceWithRawResponse(self._tenant.mcp)


class AsyncTenantResourceWithRawResponse:
    def __init__(self, tenant: AsyncTenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithRawResponse:
        """Tenant MCP credential management"""
        return AsyncMcpResourceWithRawResponse(self._tenant.mcp)


class TenantResourceWithStreamingResponse:
    def __init__(self, tenant: TenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def mcp(self) -> McpResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return McpResourceWithStreamingResponse(self._tenant.mcp)


class AsyncTenantResourceWithStreamingResponse:
    def __init__(self, tenant: AsyncTenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithStreamingResponse:
        """Tenant MCP credential management"""
        return AsyncMcpResourceWithStreamingResponse(self._tenant.mcp)
