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
from ....types.v1.compiler import cache_invalidate_params
from ....types.v1.compiler.cache_invalidate_response import CacheInvalidateResponse

__all__ = ["CacheResource", "AsyncCacheResource"]


class CacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return CacheResourceWithStreamingResponse(self)

    def invalidate(
        self,
        *,
        client_id: str,
        connection_id: Optional[str] | Omit = omit,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CacheInvalidateResponse:
        """
        Invalidate cache entries scoped by client, tenant, or connection.

        The caller's client_id must match the request client_id (auth scoping). No
        cross-client invalidation is permitted.

        Args:
          client_id: Client ID to invalidate cache entries for (mandatory)

          connection_id: Optional connection ID for connection-scoped invalidation

          tenant_id: Optional tenant ID for tenant-scoped invalidation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/compiler/cache/invalidate",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "connection_id": connection_id,
                    "tenant_id": tenant_id,
                },
                cache_invalidate_params.CacheInvalidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CacheInvalidateResponse,
        )


class AsyncCacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncCacheResourceWithStreamingResponse(self)

    async def invalidate(
        self,
        *,
        client_id: str,
        connection_id: Optional[str] | Omit = omit,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CacheInvalidateResponse:
        """
        Invalidate cache entries scoped by client, tenant, or connection.

        The caller's client_id must match the request client_id (auth scoping). No
        cross-client invalidation is permitted.

        Args:
          client_id: Client ID to invalidate cache entries for (mandatory)

          connection_id: Optional connection ID for connection-scoped invalidation

          tenant_id: Optional tenant ID for tenant-scoped invalidation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/compiler/cache/invalidate",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "connection_id": connection_id,
                    "tenant_id": tenant_id,
                },
                cache_invalidate_params.CacheInvalidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CacheInvalidateResponse,
        )


class CacheResourceWithRawResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.invalidate = to_raw_response_wrapper(
            cache.invalidate,
        )


class AsyncCacheResourceWithRawResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.invalidate = async_to_raw_response_wrapper(
            cache.invalidate,
        )


class CacheResourceWithStreamingResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.invalidate = to_streamed_response_wrapper(
            cache.invalidate,
        )


class AsyncCacheResourceWithStreamingResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.invalidate = async_to_streamed_response_wrapper(
            cache.invalidate,
        )
