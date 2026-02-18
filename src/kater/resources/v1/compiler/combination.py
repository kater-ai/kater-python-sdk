# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.compiler import combination_preview_params
from ....types.v1.compiler.combination_preview_response import CombinationPreviewResponse

__all__ = ["CombinationResource", "AsyncCombinationResource"]


class CombinationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CombinationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CombinationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CombinationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return CombinationResourceWithStreamingResponse(self)

    def preview(
        self,
        *,
        combination: str,
        connection_id: str,
        query_ref: str,
        source: Optional[str] | Omit = omit,
        tenant_key: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CombinationPreviewResponse:
        """
        Preview a single combination: resolve, compile, execute, and build config.

        Chains existing services to provide a single-call preview for the query gallery.
        Returns data + WidgetConfig for immediate rendering.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          combination: Comma-separated slot selections, same format as ResolveRequest.combination.
              Example: 'dimension=due_month,measure=compliance_rate'

          connection_id: Connection to preview against

          query_ref: Query template reference (e.g. 'q:compliance_trend.\\__base')

          tenant_key: Optional tenant key for multi-tenant execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/combination/preview",
            body=maybe_transform(
                {
                    "combination": combination,
                    "connection_id": connection_id,
                    "query_ref": query_ref,
                    "tenant_key": tenant_key,
                },
                combination_preview_params.CombinationPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, combination_preview_params.CombinationPreviewParams),
            ),
            cast_to=CombinationPreviewResponse,
        )


class AsyncCombinationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCombinationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCombinationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCombinationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncCombinationResourceWithStreamingResponse(self)

    async def preview(
        self,
        *,
        combination: str,
        connection_id: str,
        query_ref: str,
        source: Optional[str] | Omit = omit,
        tenant_key: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CombinationPreviewResponse:
        """
        Preview a single combination: resolve, compile, execute, and build config.

        Chains existing services to provide a single-call preview for the query gallery.
        Returns data + WidgetConfig for immediate rendering.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          combination: Comma-separated slot selections, same format as ResolveRequest.combination.
              Example: 'dimension=due_month,measure=compliance_rate'

          connection_id: Connection to preview against

          query_ref: Query template reference (e.g. 'q:compliance_trend.\\__base')

          tenant_key: Optional tenant key for multi-tenant execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/combination/preview",
            body=await async_maybe_transform(
                {
                    "combination": combination,
                    "connection_id": connection_id,
                    "query_ref": query_ref,
                    "tenant_key": tenant_key,
                },
                combination_preview_params.CombinationPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"source": source}, combination_preview_params.CombinationPreviewParams
                ),
            ),
            cast_to=CombinationPreviewResponse,
        )


class CombinationResourceWithRawResponse:
    def __init__(self, combination: CombinationResource) -> None:
        self._combination = combination

        self.preview = to_raw_response_wrapper(
            combination.preview,
        )


class AsyncCombinationResourceWithRawResponse:
    def __init__(self, combination: AsyncCombinationResource) -> None:
        self._combination = combination

        self.preview = async_to_raw_response_wrapper(
            combination.preview,
        )


class CombinationResourceWithStreamingResponse:
    def __init__(self, combination: CombinationResource) -> None:
        self._combination = combination

        self.preview = to_streamed_response_wrapper(
            combination.preview,
        )


class AsyncCombinationResourceWithStreamingResponse:
    def __init__(self, combination: AsyncCombinationResource) -> None:
        self._combination = combination

        self.preview = async_to_streamed_response_wrapper(
            combination.preview,
        )
