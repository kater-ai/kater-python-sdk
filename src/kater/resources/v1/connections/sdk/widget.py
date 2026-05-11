# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, strip_not_given, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.connections.sdk import widget_render_params
from .....types.v1.connections.sdk.widget_render_response import WidgetRenderResponse

__all__ = ["WidgetResource", "AsyncWidgetResource"]


class WidgetResource(SyncAPIResource):
    """SDK token management for embedded analytics"""

    @cached_property
    def with_raw_response(self) -> WidgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WidgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WidgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return WidgetResourceWithStreamingResponse(self)

    def render(
        self,
        *,
        connection_id: str,
        dashboard: Optional[widget_render_params.Dashboard],
        field_selection: widget_render_params.FieldSelection,
        filter_state: Iterable[widget_render_params.FilterState],
        pinned_variant: Optional[str],
        presentation: widget_render_params.Presentation,
        query_kater_id: str,
        result_window: widget_render_params.ResultWindow,
        temporal: widget_render_params.Temporal,
        variables: Iterable[widget_render_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WidgetRenderResponse:
        """
        Render a single SDK widget from a `RenderedQueryRequestV1` body.

        The structured replacement for `GET /api/v1/sdk/widget?combination_id=...`. The
        handler:

        1. Resolves the SDK filesystem (reusing the legacy `_resolve_sdk_filesystem`
           helper).
        2. Calls `share_render_request_resolution(...)` with the SDK auth context.
           Tenant key comes from the SDK token's `tenant_key` claim.
        3. Awaits `RenderService.render(...)` for the full pipeline.
        4. Calls `share_response_metadata_builder(...)` with
           `route_label="sdk.widget_render"` and `validate_sort_by=True`.
        5. Projects the `RenderResponse` onto `SdkWidgetResponse` (the existing model
           from `routes/client/sdk/models.py:156`).

        Pydantic `extra="forbid"` (inherited from `RenderedQueryRequestV1`) rejects
        `combination` / `combination_id` fields with HTTP 422.

        Args:
          dashboard: Dashboard context block in `RenderedQueryRequestV1`.

          field_selection: Structured field selection: source field IDs plus optional grain overrides.

          presentation: Presentation config block in `RenderedQueryRequestV1`.

          result_window: Result window block in `RenderedQueryRequestV1` (consumers do not supply
              backend-computed `query_limit`, `max_row_limit`, `effective_limit`).

          temporal: Request clock block in `RenderedQueryRequestV1`. Either field may be `null` on
              the request; the backend resolves both before canonicalization (the canonical
              `temporal` block requires non-null `timezone` and `as_of`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/sdk/widget/render",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "dashboard": dashboard,
                    "field_selection": field_selection,
                    "filter_state": filter_state,
                    "pinned_variant": pinned_variant,
                    "presentation": presentation,
                    "query_kater_id": query_kater_id,
                    "result_window": result_window,
                    "temporal": temporal,
                    "variables": variables,
                },
                widget_render_params.WidgetRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, widget_render_params.WidgetRenderParams),
                security={},
            ),
            cast_to=WidgetRenderResponse,
        )


class AsyncWidgetResource(AsyncAPIResource):
    """SDK token management for embedded analytics"""

    @cached_property
    def with_raw_response(self) -> AsyncWidgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWidgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWidgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncWidgetResourceWithStreamingResponse(self)

    async def render(
        self,
        *,
        connection_id: str,
        dashboard: Optional[widget_render_params.Dashboard],
        field_selection: widget_render_params.FieldSelection,
        filter_state: Iterable[widget_render_params.FilterState],
        pinned_variant: Optional[str],
        presentation: widget_render_params.Presentation,
        query_kater_id: str,
        result_window: widget_render_params.ResultWindow,
        temporal: widget_render_params.Temporal,
        variables: Iterable[widget_render_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WidgetRenderResponse:
        """
        Render a single SDK widget from a `RenderedQueryRequestV1` body.

        The structured replacement for `GET /api/v1/sdk/widget?combination_id=...`. The
        handler:

        1. Resolves the SDK filesystem (reusing the legacy `_resolve_sdk_filesystem`
           helper).
        2. Calls `share_render_request_resolution(...)` with the SDK auth context.
           Tenant key comes from the SDK token's `tenant_key` claim.
        3. Awaits `RenderService.render(...)` for the full pipeline.
        4. Calls `share_response_metadata_builder(...)` with
           `route_label="sdk.widget_render"` and `validate_sort_by=True`.
        5. Projects the `RenderResponse` onto `SdkWidgetResponse` (the existing model
           from `routes/client/sdk/models.py:156`).

        Pydantic `extra="forbid"` (inherited from `RenderedQueryRequestV1`) rejects
        `combination` / `combination_id` fields with HTTP 422.

        Args:
          dashboard: Dashboard context block in `RenderedQueryRequestV1`.

          field_selection: Structured field selection: source field IDs plus optional grain overrides.

          presentation: Presentation config block in `RenderedQueryRequestV1`.

          result_window: Result window block in `RenderedQueryRequestV1` (consumers do not supply
              backend-computed `query_limit`, `max_row_limit`, `effective_limit`).

          temporal: Request clock block in `RenderedQueryRequestV1`. Either field may be `null` on
              the request; the backend resolves both before canonicalization (the canonical
              `temporal` block requires non-null `timezone` and `as_of`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/sdk/widget/render",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "dashboard": dashboard,
                    "field_selection": field_selection,
                    "filter_state": filter_state,
                    "pinned_variant": pinned_variant,
                    "presentation": presentation,
                    "query_kater_id": query_kater_id,
                    "result_window": result_window,
                    "temporal": temporal,
                    "variables": variables,
                },
                widget_render_params.WidgetRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, widget_render_params.WidgetRenderParams),
                security={},
            ),
            cast_to=WidgetRenderResponse,
        )


class WidgetResourceWithRawResponse:
    def __init__(self, widget: WidgetResource) -> None:
        self._widget = widget

        self.render = to_raw_response_wrapper(
            widget.render,
        )


class AsyncWidgetResourceWithRawResponse:
    def __init__(self, widget: AsyncWidgetResource) -> None:
        self._widget = widget

        self.render = async_to_raw_response_wrapper(
            widget.render,
        )


class WidgetResourceWithStreamingResponse:
    def __init__(self, widget: WidgetResource) -> None:
        self._widget = widget

        self.render = to_streamed_response_wrapper(
            widget.render,
        )


class AsyncWidgetResourceWithStreamingResponse:
    def __init__(self, widget: AsyncWidgetResource) -> None:
        self._widget = widget

        self.render = async_to_streamed_response_wrapper(
            widget.render,
        )
