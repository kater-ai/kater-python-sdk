# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .servers import (
    ServersResource,
    AsyncServersResource,
    ServersResourceWithRawResponse,
    AsyncServersResourceWithRawResponse,
    ServersResourceWithStreamingResponse,
    AsyncServersResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    @cached_property
    def servers(self) -> ServersResource:
        """Manage MCP server integrations"""
        return ServersResource(self._client)

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


class AsyncMcpResource(AsyncAPIResource):
    @cached_property
    def servers(self) -> AsyncServersResource:
        """Manage MCP server integrations"""
        return AsyncServersResource(self._client)

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


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

    @cached_property
    def servers(self) -> ServersResourceWithRawResponse:
        """Manage MCP server integrations"""
        return ServersResourceWithRawResponse(self._mcp.servers)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

    @cached_property
    def servers(self) -> AsyncServersResourceWithRawResponse:
        """Manage MCP server integrations"""
        return AsyncServersResourceWithRawResponse(self._mcp.servers)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

    @cached_property
    def servers(self) -> ServersResourceWithStreamingResponse:
        """Manage MCP server integrations"""
        return ServersResourceWithStreamingResponse(self._mcp.servers)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

    @cached_property
    def servers(self) -> AsyncServersResourceWithStreamingResponse:
        """Manage MCP server integrations"""
        return AsyncServersResourceWithStreamingResponse(self._mcp.servers)
