# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Query, Headers, NoneType, NotGiven, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.v1.connections.tenant.mcp import credential_revoke_params

__all__ = ["CredentialsResource", "AsyncCredentialsResource"]


class CredentialsResource(SyncAPIResource):
    """Tenant MCP credential management"""

    @cached_property
    def with_raw_response(self) -> CredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return CredentialsResourceWithStreamingResponse(self)

    def revoke(
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
    ) -> None:
        """
        Revoke an MCP credential, disconnecting the user from the server.

        Soft-deletes both the credential and mcp_credential_settings rows, setting
        status to 'revoked'. This allows the user to reconnect later by creating a new
        credential (the UNIQUE constraint uses deleted_at IS NULL).

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
            f"/api/v1/tenant/mcp/{mcp_id}/credentials",
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
                    credential_revoke_params.CredentialRevokeParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=NoneType,
        )


class AsyncCredentialsResource(AsyncAPIResource):
    """Tenant MCP credential management"""

    @cached_property
    def with_raw_response(self) -> AsyncCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncCredentialsResourceWithStreamingResponse(self)

    async def revoke(
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
    ) -> None:
        """
        Revoke an MCP credential, disconnecting the user from the server.

        Soft-deletes both the credential and mcp_credential_settings rows, setting
        status to 'revoked'. This allows the user to reconnect later by creating a new
        credential (the UNIQUE constraint uses deleted_at IS NULL).

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
            f"/api/v1/tenant/mcp/{mcp_id}/credentials",
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
                    credential_revoke_params.CredentialRevokeParams,
                ),
                security={"propel_auth": True},
            ),
            cast_to=NoneType,
        )


class CredentialsResourceWithRawResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.revoke = to_raw_response_wrapper(
            credentials.revoke,
        )


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.revoke = async_to_raw_response_wrapper(
            credentials.revoke,
        )


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.revoke = to_streamed_response_wrapper(
            credentials.revoke,
        )


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.revoke = async_to_streamed_response_wrapper(
            credentials.revoke,
        )
