# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.v1.connections import oauth_handle_callback_params
from ....types.v1.connections.oauth_handle_callback_response import OAuthHandleCallbackResponse

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

    def handle_callback(
        self,
        *,
        code: str,
        state: str,
        tenant_id: str,
        tenant_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthHandleCallbackResponse:
        """
        Handle OAuth callback from an MCP provider.

        Validates the state token, exchanges the authorization code for tokens, encrypts
        them, and stores them in the database. The state token is consumed (deleted) on
        first use to prevent replay attacks.

        Args:
          code: Authorization code from OAuth provider

          state: State token for CSRF validation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/oauth/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "state": state,
                        "tenant_id": tenant_id,
                        "tenant_user_id": tenant_user_id,
                    },
                    oauth_handle_callback_params.OAuthHandleCallbackParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=OAuthHandleCallbackResponse,
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

    async def handle_callback(
        self,
        *,
        code: str,
        state: str,
        tenant_id: str,
        tenant_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthHandleCallbackResponse:
        """
        Handle OAuth callback from an MCP provider.

        Validates the state token, exchanges the authorization code for tokens, encrypts
        them, and stores them in the database. The state token is consumed (deleted) on
        first use to prevent replay attacks.

        Args:
          code: Authorization code from OAuth provider

          state: State token for CSRF validation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/oauth/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "state": state,
                        "tenant_id": tenant_id,
                        "tenant_user_id": tenant_user_id,
                    },
                    oauth_handle_callback_params.OAuthHandleCallbackParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=OAuthHandleCallbackResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.handle_callback = to_raw_response_wrapper(
            oauth.handle_callback,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.handle_callback = async_to_raw_response_wrapper(
            oauth.handle_callback,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.handle_callback = to_streamed_response_wrapper(
            oauth.handle_callback,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.handle_callback = async_to_streamed_response_wrapper(
            oauth.handle_callback,
        )
