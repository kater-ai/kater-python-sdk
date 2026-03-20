# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Query, Headers, NotGiven, not_given
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
from ......types.v1.connections.tenant.mcp import oauth_initiate_params
from ......types.v1.connections.tenant.mcp.oauth_initiate_response import OAuthInitiateResponse

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    """Tenant MCP credential management"""

    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)

    def initiate(
        self,
        mcp_id: str,
        *,
        tenant_id: str,
        tenant_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthInitiateResponse:
        """
        Initiate OAuth authorization flow for an MCP server.

        Generates a cryptographically random state token, stores it in
        oauth_pending_state with a 10-minute TTL, and returns the provider's
        authorization URL for the frontend to redirect to.

        Returns the URL in the response body (not an HTTP redirect) so the SPA frontend
        can handle navigation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return self._get(
            path_template("/api/v1/tenant/mcp/{mcp_id}/oauth/authorize", mcp_id=mcp_id),
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
                    oauth_initiate_params.OAuthInitiateParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=OAuthInitiateResponse,
        )


class AsyncOAuthResource(AsyncAPIResource):
    """Tenant MCP credential management"""

    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)

    async def initiate(
        self,
        mcp_id: str,
        *,
        tenant_id: str,
        tenant_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthInitiateResponse:
        """
        Initiate OAuth authorization flow for an MCP server.

        Generates a cryptographically random state token, stores it in
        oauth_pending_state with a 10-minute TTL, and returns the provider's
        authorization URL for the frontend to redirect to.

        Returns the URL in the response body (not an HTTP redirect) so the SPA frontend
        can handle navigation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_id:
            raise ValueError(f"Expected a non-empty value for `mcp_id` but received {mcp_id!r}")
        return await self._get(
            path_template("/api/v1/tenant/mcp/{mcp_id}/oauth/authorize", mcp_id=mcp_id),
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
                    oauth_initiate_params.OAuthInitiateParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=OAuthInitiateResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.initiate = to_raw_response_wrapper(
            oauth.initiate,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.initiate = async_to_raw_response_wrapper(
            oauth.initiate,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.initiate = to_streamed_response_wrapper(
            oauth.initiate,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.initiate = async_to_streamed_response_wrapper(
            oauth.initiate,
        )
