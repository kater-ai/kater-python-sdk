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
from ....types.v1.compiler import manifest_regenerate_and_create_pr_params
from ....types.v1.compiler.manifest_regenerate_and_create_pr_response import ManifestRegenerateAndCreatePrResponse

__all__ = ["ManifestResource", "AsyncManifestResource"]


class ManifestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManifestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ManifestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManifestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return ManifestResourceWithStreamingResponse(self)

    def regenerate_and_create_pr(
        self,
        *,
        connection_id: str,
        source: Optional[str] | Omit = omit,
        include_dependency_graph: bool | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManifestRegenerateAndCreatePrResponse:
        """
        Regenerate manifest through compiler validation and open a PR.

        This endpoint is remote-source only. It regenerates compiler artifacts from the
        selected connection, then creates a GitHub PR with updated
        `.kater/manifest.yaml` (and dependency graph when requested).

        Args:
          connection_id: Connection kater_id to regenerate and commit manifest for

          include_dependency_graph: Also include .kater/dependency_graph.yaml in the PR when available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/manifest/recovery-pr",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "include_dependency_graph": include_dependency_graph,
                },
                manifest_regenerate_and_create_pr_params.ManifestRegenerateAndCreatePrParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"source": source}, manifest_regenerate_and_create_pr_params.ManifestRegenerateAndCreatePrParams
                ),
            ),
            cast_to=ManifestRegenerateAndCreatePrResponse,
        )


class AsyncManifestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManifestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncManifestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManifestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncManifestResourceWithStreamingResponse(self)

    async def regenerate_and_create_pr(
        self,
        *,
        connection_id: str,
        source: Optional[str] | Omit = omit,
        include_dependency_graph: bool | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManifestRegenerateAndCreatePrResponse:
        """
        Regenerate manifest through compiler validation and open a PR.

        This endpoint is remote-source only. It regenerates compiler artifacts from the
        selected connection, then creates a GitHub PR with updated
        `.kater/manifest.yaml` (and dependency graph when requested).

        Args:
          connection_id: Connection kater_id to regenerate and commit manifest for

          include_dependency_graph: Also include .kater/dependency_graph.yaml in the PR when available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/manifest/recovery-pr",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "include_dependency_graph": include_dependency_graph,
                },
                manifest_regenerate_and_create_pr_params.ManifestRegenerateAndCreatePrParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"source": source}, manifest_regenerate_and_create_pr_params.ManifestRegenerateAndCreatePrParams
                ),
            ),
            cast_to=ManifestRegenerateAndCreatePrResponse,
        )


class ManifestResourceWithRawResponse:
    def __init__(self, manifest: ManifestResource) -> None:
        self._manifest = manifest

        self.regenerate_and_create_pr = to_raw_response_wrapper(
            manifest.regenerate_and_create_pr,
        )


class AsyncManifestResourceWithRawResponse:
    def __init__(self, manifest: AsyncManifestResource) -> None:
        self._manifest = manifest

        self.regenerate_and_create_pr = async_to_raw_response_wrapper(
            manifest.regenerate_and_create_pr,
        )


class ManifestResourceWithStreamingResponse:
    def __init__(self, manifest: ManifestResource) -> None:
        self._manifest = manifest

        self.regenerate_and_create_pr = to_streamed_response_wrapper(
            manifest.regenerate_and_create_pr,
        )


class AsyncManifestResourceWithStreamingResponse:
    def __init__(self, manifest: AsyncManifestResource) -> None:
        self._manifest = manifest

        self.regenerate_and_create_pr = async_to_streamed_response_wrapper(
            manifest.regenerate_and_create_pr,
        )
