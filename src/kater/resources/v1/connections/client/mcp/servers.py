# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ......_types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.v1.connections.client.mcp import (
    server_create_params,
    server_update_params,
    server_update_config_params,
    server_update_api_key_params,
)
from ......types.v1.connections.client.mcp.server_list_response import ServerListResponse
from ......types.v1.connections.client.mcp.server_create_response import ServerCreateResponse
from ......types.v1.connections.client.mcp.server_update_response import ServerUpdateResponse
from ......types.v1.connections.client.mcp.server_discover_response import ServerDiscoverResponse
from ......types.v1.connections.client.mcp.server_rediscover_response import ServerRediscoverResponse
from ......types.v1.connections.client.mcp.server_update_config_response import ServerUpdateConfigResponse

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    """Manage MCP server integrations"""

    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return ServersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        server_url: str,
        slug: str,
        api_key: Optional[str] | Omit = omit,
        auth_type: Literal["api_key", "oauth2", "none"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        oauth_authorize_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_client_secret: Optional[str] | Omit = omit,
        oauth_revoke_url: Optional[str] | Omit = omit,
        oauth_scopes_requested: Optional[str] | Omit = omit,
        oauth_token_url: Optional[str] | Omit = omit,
        terms_acknowledged: bool | Omit = omit,
        transport: Literal["auto", "streamable_http", "sse"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerCreateResponse:
        """
        Register a new MCP server for the client organization.

        Validates URL safety (SSRF prevention), slug format, and OAuth fields. The MCP
        server is NOT contacted during registration.

        Args:
          name: Display name

          server_url: HTTPS URL of the MCP server

          slug: Unique snake_case identifier

          api_key: API key (for auth_type=api_key). Stored as shared client-level credential.

          auth_type: Authentication type

          description: Optional description

          oauth_authorize_url: OAuth2 authorize URL

          oauth_client_id: OAuth2 client ID

          oauth_client_secret: OAuth2 client secret (encrypted)

          oauth_revoke_url: OAuth2 revoke URL (optional)

          oauth_scopes_requested: OAuth2 scopes

          oauth_token_url: OAuth2 token URL

          terms_acknowledged: Must be true to accept security terms

          transport: Transport protocol

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/client/mcp/servers",
            body=maybe_transform(
                {
                    "name": name,
                    "server_url": server_url,
                    "slug": slug,
                    "api_key": api_key,
                    "auth_type": auth_type,
                    "description": description,
                    "oauth_authorize_url": oauth_authorize_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "oauth_revoke_url": oauth_revoke_url,
                    "oauth_scopes_requested": oauth_scopes_requested,
                    "oauth_token_url": oauth_token_url,
                    "terms_acknowledged": terms_acknowledged,
                    "transport": transport,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerCreateResponse,
        )

    def update(
        self,
        mcp_id: str,
        *,
        allowed_capabilities: Optional[Iterable[server_update_params.AllowedCapability]] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        """
        Activate an MCP server by selecting capabilities to expose.

        Validates that all submitted capability names exist in the server's discovered
        capabilities. Sets status to 'active' when allowed_capabilities is non-empty.

        Args:
          allowed_capabilities: Capabilities to expose as LLM tools

          enabled: Enable/disable toggle

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return self._put(
            path_template("/api/v1/client/mcp/servers/{mcp_id}", mcp_id=mcp_id),
            body=maybe_transform(
                {
                    "allowed_capabilities": allowed_capabilities,
                    "enabled": enabled,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerUpdateResponse,
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
    ) -> ServerListResponse:
        """
        List all MCP servers for the authenticated client.

        RLS automatically scopes results to the client's organization. Only non-deleted
        servers are returned.
        """
        return self._get(
            "/api/v1/client/mcp/servers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerListResponse,
        )

    def delete(
        self,
        mcp_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete an MCP server and cascade to credential settings.

        Cascades:

        1.

        All mcp_credential_settings rows set to status='revoked' + deleted_at
        2. OAuth client secret credential soft-deleted (if exists)
        3. MCP server row soft-deleted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/client/mcp/servers/{mcp_id}", mcp_id=mcp_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=NoneType,
        )

    def discover(
        self,
        mcp_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDiscoverResponse:
        """
        Discover capabilities from a registered MCP server.

        For api_key servers with a stored credential, uses the API key for discovery.
        Discovery does NOT change server status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return self._post(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/discover", mcp_id=mcp_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerDiscoverResponse,
        )

    def rediscover(
        self,
        mcp_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerRediscoverResponse:
        """
        Re-discover capabilities and merge with existing data.

        New capabilities are added. Existing capabilities that are in
        allowed_capabilities preserve their is_write classification. The
        allowed_capabilities list and status are NOT modified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return self._post(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/rediscover", mcp_id=mcp_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerRediscoverResponse,
        )

    def update_api_key(
        self,
        mcp_id: str,
        *,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Replace the shared API key credential for an api_key MCP server.

        Soft-deletes the old credential and creates a new one.

        Args:
          api_key: New API key value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/api-key", mcp_id=mcp_id),
            body=maybe_transform({"api_key": api_key}, server_update_api_key_params.ServerUpdateAPIKeyParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=NoneType,
        )

    def update_config(
        self,
        mcp_id: str,
        *,
        auth_type: Optional[Literal["api_key", "oauth2", "none"]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        oauth_authorize_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_client_secret: Optional[str] | Omit = omit,
        oauth_revoke_url: Optional[str] | Omit = omit,
        oauth_scopes_requested: Optional[str] | Omit = omit,
        oauth_token_url: Optional[str] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        transport: Optional[Literal["auto", "streamable_http", "sse"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateConfigResponse:
        """
        Update the configuration of a registered MCP server.

        Slug is not editable (used in tool naming). Changing server_url or auth_type
        resets server to pending_setup and revokes all tenant credential settings.

        Args:
          auth_type: Authentication type for MCP server connections.

          transport: Transport protocol for MCP server communication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return self._patch(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/config", mcp_id=mcp_id),
            body=maybe_transform(
                {
                    "auth_type": auth_type,
                    "description": description,
                    "name": name,
                    "oauth_authorize_url": oauth_authorize_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "oauth_revoke_url": oauth_revoke_url,
                    "oauth_scopes_requested": oauth_scopes_requested,
                    "oauth_token_url": oauth_token_url,
                    "server_url": server_url,
                    "transport": transport,
                },
                server_update_config_params.ServerUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerUpdateConfigResponse,
        )


class AsyncServersResource(AsyncAPIResource):
    """Manage MCP server integrations"""

    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncServersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        server_url: str,
        slug: str,
        api_key: Optional[str] | Omit = omit,
        auth_type: Literal["api_key", "oauth2", "none"] | Omit = omit,
        description: Optional[str] | Omit = omit,
        oauth_authorize_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_client_secret: Optional[str] | Omit = omit,
        oauth_revoke_url: Optional[str] | Omit = omit,
        oauth_scopes_requested: Optional[str] | Omit = omit,
        oauth_token_url: Optional[str] | Omit = omit,
        terms_acknowledged: bool | Omit = omit,
        transport: Literal["auto", "streamable_http", "sse"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerCreateResponse:
        """
        Register a new MCP server for the client organization.

        Validates URL safety (SSRF prevention), slug format, and OAuth fields. The MCP
        server is NOT contacted during registration.

        Args:
          name: Display name

          server_url: HTTPS URL of the MCP server

          slug: Unique snake_case identifier

          api_key: API key (for auth_type=api_key). Stored as shared client-level credential.

          auth_type: Authentication type

          description: Optional description

          oauth_authorize_url: OAuth2 authorize URL

          oauth_client_id: OAuth2 client ID

          oauth_client_secret: OAuth2 client secret (encrypted)

          oauth_revoke_url: OAuth2 revoke URL (optional)

          oauth_scopes_requested: OAuth2 scopes

          oauth_token_url: OAuth2 token URL

          terms_acknowledged: Must be true to accept security terms

          transport: Transport protocol

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/client/mcp/servers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "server_url": server_url,
                    "slug": slug,
                    "api_key": api_key,
                    "auth_type": auth_type,
                    "description": description,
                    "oauth_authorize_url": oauth_authorize_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "oauth_revoke_url": oauth_revoke_url,
                    "oauth_scopes_requested": oauth_scopes_requested,
                    "oauth_token_url": oauth_token_url,
                    "terms_acknowledged": terms_acknowledged,
                    "transport": transport,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerCreateResponse,
        )

    async def update(
        self,
        mcp_id: str,
        *,
        allowed_capabilities: Optional[Iterable[server_update_params.AllowedCapability]] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateResponse:
        """
        Activate an MCP server by selecting capabilities to expose.

        Validates that all submitted capability names exist in the server's discovered
        capabilities. Sets status to 'active' when allowed_capabilities is non-empty.

        Args:
          allowed_capabilities: Capabilities to expose as LLM tools

          enabled: Enable/disable toggle

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return await self._put(
            path_template("/api/v1/client/mcp/servers/{mcp_id}", mcp_id=mcp_id),
            body=await async_maybe_transform(
                {
                    "allowed_capabilities": allowed_capabilities,
                    "enabled": enabled,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerUpdateResponse,
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
    ) -> ServerListResponse:
        """
        List all MCP servers for the authenticated client.

        RLS automatically scopes results to the client's organization. Only non-deleted
        servers are returned.
        """
        return await self._get(
            "/api/v1/client/mcp/servers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerListResponse,
        )

    async def delete(
        self,
        mcp_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete an MCP server and cascade to credential settings.

        Cascades:

        1.

        All mcp_credential_settings rows set to status='revoked' + deleted_at
        2. OAuth client secret credential soft-deleted (if exists)
        3. MCP server row soft-deleted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/client/mcp/servers/{mcp_id}", mcp_id=mcp_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=NoneType,
        )

    async def discover(
        self,
        mcp_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDiscoverResponse:
        """
        Discover capabilities from a registered MCP server.

        For api_key servers with a stored credential, uses the API key for discovery.
        Discovery does NOT change server status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return await self._post(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/discover", mcp_id=mcp_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerDiscoverResponse,
        )

    async def rediscover(
        self,
        mcp_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerRediscoverResponse:
        """
        Re-discover capabilities and merge with existing data.

        New capabilities are added. Existing capabilities that are in
        allowed_capabilities preserve their is_write classification. The
        allowed_capabilities list and status are NOT modified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return await self._post(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/rediscover", mcp_id=mcp_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerRediscoverResponse,
        )

    async def update_api_key(
        self,
        mcp_id: str,
        *,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Replace the shared API key credential for an api_key MCP server.

        Soft-deletes the old credential and creates a new one.

        Args:
          api_key: New API key value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/api-key", mcp_id=mcp_id),
            body=await async_maybe_transform(
                {"api_key": api_key}, server_update_api_key_params.ServerUpdateAPIKeyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=NoneType,
        )

    async def update_config(
        self,
        mcp_id: str,
        *,
        auth_type: Optional[Literal["api_key", "oauth2", "none"]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        oauth_authorize_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_client_secret: Optional[str] | Omit = omit,
        oauth_revoke_url: Optional[str] | Omit = omit,
        oauth_scopes_requested: Optional[str] | Omit = omit,
        oauth_token_url: Optional[str] | Omit = omit,
        server_url: Optional[str] | Omit = omit,
        transport: Optional[Literal["auto", "streamable_http", "sse"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerUpdateConfigResponse:
        """
        Update the configuration of a registered MCP server.

        Slug is not editable (used in tool naming). Changing server_url or auth_type
        resets server to pending_setup and revokes all tenant credential settings.

        Args:
          auth_type: Authentication type for MCP server connections.

          transport: Transport protocol for MCP server communication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return await self._patch(
            path_template("/api/v1/client/mcp/servers/{mcp_id}/config", mcp_id=mcp_id),
            body=await async_maybe_transform(
                {
                    "auth_type": auth_type,
                    "description": description,
                    "name": name,
                    "oauth_authorize_url": oauth_authorize_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "oauth_revoke_url": oauth_revoke_url,
                    "oauth_scopes_requested": oauth_scopes_requested,
                    "oauth_token_url": oauth_token_url,
                    "server_url": server_url,
                    "transport": transport,
                },
                server_update_config_params.ServerUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"propel_auth": True},
            ),
            cast_to=ServerUpdateConfigResponse,
        )


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.create = to_raw_response_wrapper(
            servers.create,
        )
        self.update = to_raw_response_wrapper(
            servers.update,
        )
        self.list = to_raw_response_wrapper(
            servers.list,
        )
        self.delete = to_raw_response_wrapper(
            servers.delete,
        )
        self.discover = to_raw_response_wrapper(
            servers.discover,
        )
        self.rediscover = to_raw_response_wrapper(
            servers.rediscover,
        )
        self.update_api_key = to_raw_response_wrapper(
            servers.update_api_key,
        )
        self.update_config = to_raw_response_wrapper(
            servers.update_config,
        )


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_raw_response_wrapper(
            servers.create,
        )
        self.update = async_to_raw_response_wrapper(
            servers.update,
        )
        self.list = async_to_raw_response_wrapper(
            servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            servers.delete,
        )
        self.discover = async_to_raw_response_wrapper(
            servers.discover,
        )
        self.rediscover = async_to_raw_response_wrapper(
            servers.rediscover,
        )
        self.update_api_key = async_to_raw_response_wrapper(
            servers.update_api_key,
        )
        self.update_config = async_to_raw_response_wrapper(
            servers.update_config,
        )


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.create = to_streamed_response_wrapper(
            servers.create,
        )
        self.update = to_streamed_response_wrapper(
            servers.update,
        )
        self.list = to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            servers.delete,
        )
        self.discover = to_streamed_response_wrapper(
            servers.discover,
        )
        self.rediscover = to_streamed_response_wrapper(
            servers.rediscover,
        )
        self.update_api_key = to_streamed_response_wrapper(
            servers.update_api_key,
        )
        self.update_config = to_streamed_response_wrapper(
            servers.update_config,
        )


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.create = async_to_streamed_response_wrapper(
            servers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            servers.delete,
        )
        self.discover = async_to_streamed_response_wrapper(
            servers.discover,
        )
        self.rediscover = async_to_streamed_response_wrapper(
            servers.rediscover,
        )
        self.update_api_key = async_to_streamed_response_wrapper(
            servers.update_api_key,
        )
        self.update_config = async_to_streamed_response_wrapper(
            servers.update_config,
        )
