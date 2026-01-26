# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.v1.org import TenancyType, client_update_params
from ....types.v1.org.client import Client
from ....types.v1.org.tenancy_type import TenancyType

__all__ = ["ClientResource", "AsyncClientResource"]


class ClientResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return ClientResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Client:
        """
        Get the current user's organization details.

        RLS: Filtered to current client (ClientRLSDB).
        """
        return self._get(
            "/api/v1/org/client",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Client,
        )

    def update(
        self,
        *,
        can_auto_join_by_domain: Optional[bool] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        members_must_have_matching_domain: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tenancy_type: Optional[TenancyType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Client:
        """
        Update the current user's organization details.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenancy_type: Type of tenancy for a client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/api/v1/org/client",
            body=maybe_transform(
                {
                    "can_auto_join_by_domain": can_auto_join_by_domain,
                    "domain": domain,
                    "logo_url": logo_url,
                    "members_must_have_matching_domain": members_must_have_matching_domain,
                    "name": name,
                    "tenancy_type": tenancy_type,
                },
                client_update_params.ClientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Client,
        )


class AsyncClientResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncClientResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Client:
        """
        Get the current user's organization details.

        RLS: Filtered to current client (ClientRLSDB).
        """
        return await self._get(
            "/api/v1/org/client",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Client,
        )

    async def update(
        self,
        *,
        can_auto_join_by_domain: Optional[bool] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        members_must_have_matching_domain: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tenancy_type: Optional[TenancyType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Client:
        """
        Update the current user's organization details.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenancy_type: Type of tenancy for a client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/api/v1/org/client",
            body=await async_maybe_transform(
                {
                    "can_auto_join_by_domain": can_auto_join_by_domain,
                    "domain": domain,
                    "logo_url": logo_url,
                    "members_must_have_matching_domain": members_must_have_matching_domain,
                    "name": name,
                    "tenancy_type": tenancy_type,
                },
                client_update_params.ClientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Client,
        )


class ClientResourceWithRawResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

        self.retrieve = to_raw_response_wrapper(
            client.retrieve,
        )
        self.update = to_raw_response_wrapper(
            client.update,
        )


class AsyncClientResourceWithRawResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

        self.retrieve = async_to_raw_response_wrapper(
            client.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            client.update,
        )


class ClientResourceWithStreamingResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

        self.retrieve = to_streamed_response_wrapper(
            client.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            client.update,
        )


class AsyncClientResourceWithStreamingResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

        self.retrieve = async_to_streamed_response_wrapper(
            client.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            client.update,
        )
