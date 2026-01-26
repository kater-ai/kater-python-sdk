# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
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
from ....types.v1.tenants import batch_create_params, batch_delete_params, batch_update_params
from ....types.v1.create_tenant_param import CreateTenantParam
from ....types.v1.tenants.batch_create_response import BatchCreateResponse
from ....types.v1.tenants.batch_delete_response import BatchDeleteResponse
from ....types.v1.tenants.batch_update_response import BatchUpdateResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        tenants: Iterable[CreateTenantParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCreateResponse:
        """
        Create multiple tenants in a single request.

        Each tenant is processed independently. If one fails, others may succeed.
        Returns lists of succeeded and failed operations.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenants: List of tenants to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/tenants/batch",
            body=maybe_transform({"tenants": tenants}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCreateResponse,
        )

    def update(
        self,
        *,
        tenants: Iterable[batch_update_params.Tenant],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchUpdateResponse:
        """
        Update multiple tenants in a single request.

        Each tenant is processed independently. If one fails, others may succeed.
        Returns lists of succeeded and failed operations.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenants: List of tenant updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/api/v1/tenants/batch",
            body=maybe_transform({"tenants": tenants}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchUpdateResponse,
        )

    def delete(
        self,
        *,
        tenant_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchDeleteResponse:
        """
        Delete multiple tenants in a single request.

        Each tenant is processed independently. If one fails, others may succeed.
        Returns lists of succeeded and failed operations.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenant_ids: List of tenant IDs to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/v1/tenants/batch",
            body=maybe_transform({"tenant_ids": tenant_ids}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        tenants: Iterable[CreateTenantParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCreateResponse:
        """
        Create multiple tenants in a single request.

        Each tenant is processed independently. If one fails, others may succeed.
        Returns lists of succeeded and failed operations.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenants: List of tenants to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/tenants/batch",
            body=await async_maybe_transform({"tenants": tenants}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCreateResponse,
        )

    async def update(
        self,
        *,
        tenants: Iterable[batch_update_params.Tenant],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchUpdateResponse:
        """
        Update multiple tenants in a single request.

        Each tenant is processed independently. If one fails, others may succeed.
        Returns lists of succeeded and failed operations.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenants: List of tenant updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/api/v1/tenants/batch",
            body=await async_maybe_transform({"tenants": tenants}, batch_update_params.BatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchUpdateResponse,
        )

    async def delete(
        self,
        *,
        tenant_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchDeleteResponse:
        """
        Delete multiple tenants in a single request.

        Each tenant is processed independently. If one fails, others may succeed.
        Returns lists of succeeded and failed operations.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          tenant_ids: List of tenant IDs to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/v1/tenants/batch",
            body=await async_maybe_transform({"tenant_ids": tenant_ids}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )
        self.update = to_raw_response_wrapper(
            batch.update,
        )
        self.delete = to_raw_response_wrapper(
            batch.delete,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )
        self.update = async_to_raw_response_wrapper(
            batch.update,
        )
        self.delete = async_to_raw_response_wrapper(
            batch.delete,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )
        self.update = to_streamed_response_wrapper(
            batch.update,
        )
        self.delete = to_streamed_response_wrapper(
            batch.delete,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
        self.update = async_to_streamed_response_wrapper(
            batch.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            batch.delete,
        )
