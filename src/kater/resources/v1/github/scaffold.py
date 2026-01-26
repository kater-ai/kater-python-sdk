# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.github.scaffold_trigger import ScaffoldTrigger
from ....types.v1.github.scaffold_get_status_response import ScaffoldGetStatusResponse

__all__ = ["ScaffoldResource", "AsyncScaffoldResource"]


class ScaffoldResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScaffoldResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScaffoldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScaffoldResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return ScaffoldResourceWithStreamingResponse(self)

    def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScaffoldGetStatusResponse:
        """Get the current scaffolding status for the connected repository."""
        return self._get(
            "/api/v1/github/scaffold/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScaffoldGetStatusResponse,
        )

    def retry(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScaffoldTrigger:
        """Clean up partial state and retry scaffolding from scratch."""
        return self._post(
            "/api/v1/github/scaffold/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScaffoldTrigger,
        )

    def trigger(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScaffoldTrigger:
        """Create the Kater folder structure and PR in the selected repository."""
        return self._post(
            "/api/v1/github/scaffold",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScaffoldTrigger,
        )


class AsyncScaffoldResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScaffoldResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScaffoldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScaffoldResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncScaffoldResourceWithStreamingResponse(self)

    async def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScaffoldGetStatusResponse:
        """Get the current scaffolding status for the connected repository."""
        return await self._get(
            "/api/v1/github/scaffold/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScaffoldGetStatusResponse,
        )

    async def retry(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScaffoldTrigger:
        """Clean up partial state and retry scaffolding from scratch."""
        return await self._post(
            "/api/v1/github/scaffold/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScaffoldTrigger,
        )

    async def trigger(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScaffoldTrigger:
        """Create the Kater folder structure and PR in the selected repository."""
        return await self._post(
            "/api/v1/github/scaffold",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScaffoldTrigger,
        )


class ScaffoldResourceWithRawResponse:
    def __init__(self, scaffold: ScaffoldResource) -> None:
        self._scaffold = scaffold

        self.get_status = to_raw_response_wrapper(
            scaffold.get_status,
        )
        self.retry = to_raw_response_wrapper(
            scaffold.retry,
        )
        self.trigger = to_raw_response_wrapper(
            scaffold.trigger,
        )


class AsyncScaffoldResourceWithRawResponse:
    def __init__(self, scaffold: AsyncScaffoldResource) -> None:
        self._scaffold = scaffold

        self.get_status = async_to_raw_response_wrapper(
            scaffold.get_status,
        )
        self.retry = async_to_raw_response_wrapper(
            scaffold.retry,
        )
        self.trigger = async_to_raw_response_wrapper(
            scaffold.trigger,
        )


class ScaffoldResourceWithStreamingResponse:
    def __init__(self, scaffold: ScaffoldResource) -> None:
        self._scaffold = scaffold

        self.get_status = to_streamed_response_wrapper(
            scaffold.get_status,
        )
        self.retry = to_streamed_response_wrapper(
            scaffold.retry,
        )
        self.trigger = to_streamed_response_wrapper(
            scaffold.trigger,
        )


class AsyncScaffoldResourceWithStreamingResponse:
    def __init__(self, scaffold: AsyncScaffoldResource) -> None:
        self._scaffold = scaffold

        self.get_status = async_to_streamed_response_wrapper(
            scaffold.get_status,
        )
        self.retry = async_to_streamed_response_wrapper(
            scaffold.retry,
        )
        self.trigger = async_to_streamed_response_wrapper(
            scaffold.trigger,
        )
