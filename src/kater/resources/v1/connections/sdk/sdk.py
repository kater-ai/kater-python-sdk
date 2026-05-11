# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .widget import (
    WidgetResource,
    AsyncWidgetResource,
    WidgetResourceWithRawResponse,
    AsyncWidgetResourceWithRawResponse,
    WidgetResourceWithStreamingResponse,
    AsyncWidgetResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SDKResource", "AsyncSDKResource"]


class SDKResource(SyncAPIResource):
    @cached_property
    def widget(self) -> WidgetResource:
        """SDK token management for embedded analytics"""
        return WidgetResource(self._client)

    @cached_property
    def with_raw_response(self) -> SDKResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SDKResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SDKResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return SDKResourceWithStreamingResponse(self)


class AsyncSDKResource(AsyncAPIResource):
    @cached_property
    def widget(self) -> AsyncWidgetResource:
        """SDK token management for embedded analytics"""
        return AsyncWidgetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSDKResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSDKResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSDKResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncSDKResourceWithStreamingResponse(self)


class SDKResourceWithRawResponse:
    def __init__(self, sdk: SDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def widget(self) -> WidgetResourceWithRawResponse:
        """SDK token management for embedded analytics"""
        return WidgetResourceWithRawResponse(self._sdk.widget)


class AsyncSDKResourceWithRawResponse:
    def __init__(self, sdk: AsyncSDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def widget(self) -> AsyncWidgetResourceWithRawResponse:
        """SDK token management for embedded analytics"""
        return AsyncWidgetResourceWithRawResponse(self._sdk.widget)


class SDKResourceWithStreamingResponse:
    def __init__(self, sdk: SDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def widget(self) -> WidgetResourceWithStreamingResponse:
        """SDK token management for embedded analytics"""
        return WidgetResourceWithStreamingResponse(self._sdk.widget)


class AsyncSDKResourceWithStreamingResponse:
    def __init__(self, sdk: AsyncSDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def widget(self) -> AsyncWidgetResourceWithStreamingResponse:
        """SDK token management for embedded analytics"""
        return AsyncWidgetResourceWithStreamingResponse(self._sdk.widget)
