# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.v1.compiler import capability_create_params, capability_sample_params
from ....types.v1.compiler.capability_create_response import CapabilityCreateResponse
from ....types.v1.compiler.capability_sample_response import CapabilitySampleResponse

__all__ = ["CapabilitiesResource", "AsyncCapabilitiesResource"]


class CapabilitiesResource(SyncAPIResource):
    """Validate, resolve, and compile query templates to SQL"""

    @cached_property
    def with_raw_response(self) -> CapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return CapabilitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_id: str,
        source: Optional[str] | Omit = omit,
        query_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilityCreateResponse:
        """Return capabilities for every query in `request.connection_id`.

        The handler:

        1.

        Builds per-request `CredentialService`, `ConnectionService`, and
           `CompilerApiService` instances (matching the structured render route's
           per-request lifetime).
        2. Resolves tenant parameters via
           `resolve_tenant_params(..., tenant_key=NO_TENANT_KEY)` (connection access
           only; capabilities is tenant-agnostic per PRD `#capabilities-service`).
        3. Wraps the build call in `stage_span("compiler.capabilities", ...)` and
           records pipeline duration in a `finally` block via
           `record_pipeline_call(pipeline="compiler_capabilities", ...)`.
        4. Awaits `CapabilitiesService.build(...)` exactly once.
        5. Maps known errors to typed `ApiError` (`ConnectionNotFoundError` → 404,
           `SchemaParseError` → 400). Unexpected exceptions propagate.
        6. Emits one `capabilities_succeeded` log event on success or
           `capabilities_failed` on error. The events log `connection_id` / `client_id`
           / `query_count` only — never variable values, `allowed_values_static`, or
           filter `presets` (PRD NFR8).

        Consumer surfaces this route serves (post Stories 4.2, 5.1, 6.2, 6.3, 6.5):
        Query Builder capabilities loader, SDK request builder defaults, CLI
        `kater capabilities` (Story 6.2 owns command surface), language server
        `kater/queryCapabilities` (Story 6.3 imports the service directly), chat tool
        capabilities lookup.

        Args:
          connection_id: Connection UUID to enumerate capabilities against

          query_ids: Optional list of query UUIDs to limit the response. When omitted (or null), the
              response includes capabilities for every query in the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/capabilities",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "query_ids": query_ids,
                },
                capability_create_params.CapabilityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, capability_create_params.CapabilityCreateParams),
            ),
            cast_to=CapabilityCreateResponse,
        )

    def sample(
        self,
        *,
        connection_id: str,
        n: int,
        query_kater_id: str,
        source: Optional[str] | Omit = omit,
        include_filter_variants: bool | Omit = omit,
        include_pinned_variants: bool | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilitySampleResponse:
        """Sample `n` deterministic representative selections for one query.

        Pipeline:

        1.

        Build per-request `CredentialService`, `ConnectionService`,
           `CompilerApiService`, `CapabilitiesService` instances (matching the
           structured render and capabilities routes' per-request lifetime).
        2. Resolve tenant parameters via
           `resolve_tenant_params(..., tenant_key=NO_TENANT_KEY)` (sampling is
           connection-scoped metadata- derived; tenant_key only controls connection
           access).
        3. Wrap the build + sample calls in
           `stage_span("compiler.capability_sampling", ...)` and record pipeline
           duration in a `finally` block via
           `record_pipeline_call(pipeline="compiler_capability_sampling", ...)`.
        4. Call `CapabilitiesService.build(...)` once with
           `query_kater_ids=[query_kater_id]` to get the input metadata.
        5. Map missing query to HTTP 404 (`query_not_found`); empty `response.queries`
           indicates the query is not present in the connection.
        6. Look up the `QuerySchema` from the in-process index (used by the
           pinned-variant tier when `include_pinned_variants=True`).
        7. Call `sample_field_selections(...)` once to produce the typed result.
        8. Map known errors to typed `ApiError` (`ConnectionNotFoundError` → 404,
           `SchemaParseError` → 400).
        9. Emit one `capability_sampling_succeeded` log on success or
           `capability_sampling_failed` on error. The events log `query UUID` /
           `client UUID` / `n` / `available` / `truncated` only, never variable values,
           allowed-value lists, filter values, or sample payloads (PRD NFR8).

        The response shape matches Story 6.2's CLI shim verbatim so deployed CLIs
        deserialize successfully without redeploying.

        Args:
          connection_id: Connection UUID to sample selections against

          n: Number of representative selections requested (must be >= 1)

          query_kater_id: Query UUID to sample selections for

          include_filter_variants: When true, include tier-8 optional filter variants in the sample

          include_pinned_variants: When true, include pinned-variant variants in the sample

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/capabilities/sample",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "n": n,
                    "query_kater_id": query_kater_id,
                    "include_filter_variants": include_filter_variants,
                    "include_pinned_variants": include_pinned_variants,
                },
                capability_sample_params.CapabilitySampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, capability_sample_params.CapabilitySampleParams),
            ),
            cast_to=CapabilitySampleResponse,
        )


class AsyncCapabilitiesResource(AsyncAPIResource):
    """Validate, resolve, and compile query templates to SQL"""

    @cached_property
    def with_raw_response(self) -> AsyncCapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncCapabilitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_id: str,
        source: Optional[str] | Omit = omit,
        query_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilityCreateResponse:
        """Return capabilities for every query in `request.connection_id`.

        The handler:

        1.

        Builds per-request `CredentialService`, `ConnectionService`, and
           `CompilerApiService` instances (matching the structured render route's
           per-request lifetime).
        2. Resolves tenant parameters via
           `resolve_tenant_params(..., tenant_key=NO_TENANT_KEY)` (connection access
           only; capabilities is tenant-agnostic per PRD `#capabilities-service`).
        3. Wraps the build call in `stage_span("compiler.capabilities", ...)` and
           records pipeline duration in a `finally` block via
           `record_pipeline_call(pipeline="compiler_capabilities", ...)`.
        4. Awaits `CapabilitiesService.build(...)` exactly once.
        5. Maps known errors to typed `ApiError` (`ConnectionNotFoundError` → 404,
           `SchemaParseError` → 400). Unexpected exceptions propagate.
        6. Emits one `capabilities_succeeded` log event on success or
           `capabilities_failed` on error. The events log `connection_id` / `client_id`
           / `query_count` only — never variable values, `allowed_values_static`, or
           filter `presets` (PRD NFR8).

        Consumer surfaces this route serves (post Stories 4.2, 5.1, 6.2, 6.3, 6.5):
        Query Builder capabilities loader, SDK request builder defaults, CLI
        `kater capabilities` (Story 6.2 owns command surface), language server
        `kater/queryCapabilities` (Story 6.3 imports the service directly), chat tool
        capabilities lookup.

        Args:
          connection_id: Connection UUID to enumerate capabilities against

          query_ids: Optional list of query UUIDs to limit the response. When omitted (or null), the
              response includes capabilities for every query in the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/capabilities",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "query_ids": query_ids,
                },
                capability_create_params.CapabilityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, capability_create_params.CapabilityCreateParams),
            ),
            cast_to=CapabilityCreateResponse,
        )

    async def sample(
        self,
        *,
        connection_id: str,
        n: int,
        query_kater_id: str,
        source: Optional[str] | Omit = omit,
        include_filter_variants: bool | Omit = omit,
        include_pinned_variants: bool | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilitySampleResponse:
        """Sample `n` deterministic representative selections for one query.

        Pipeline:

        1.

        Build per-request `CredentialService`, `ConnectionService`,
           `CompilerApiService`, `CapabilitiesService` instances (matching the
           structured render and capabilities routes' per-request lifetime).
        2. Resolve tenant parameters via
           `resolve_tenant_params(..., tenant_key=NO_TENANT_KEY)` (sampling is
           connection-scoped metadata- derived; tenant_key only controls connection
           access).
        3. Wrap the build + sample calls in
           `stage_span("compiler.capability_sampling", ...)` and record pipeline
           duration in a `finally` block via
           `record_pipeline_call(pipeline="compiler_capability_sampling", ...)`.
        4. Call `CapabilitiesService.build(...)` once with
           `query_kater_ids=[query_kater_id]` to get the input metadata.
        5. Map missing query to HTTP 404 (`query_not_found`); empty `response.queries`
           indicates the query is not present in the connection.
        6. Look up the `QuerySchema` from the in-process index (used by the
           pinned-variant tier when `include_pinned_variants=True`).
        7. Call `sample_field_selections(...)` once to produce the typed result.
        8. Map known errors to typed `ApiError` (`ConnectionNotFoundError` → 404,
           `SchemaParseError` → 400).
        9. Emit one `capability_sampling_succeeded` log on success or
           `capability_sampling_failed` on error. The events log `query UUID` /
           `client UUID` / `n` / `available` / `truncated` only, never variable values,
           allowed-value lists, filter values, or sample payloads (PRD NFR8).

        The response shape matches Story 6.2's CLI shim verbatim so deployed CLIs
        deserialize successfully without redeploying.

        Args:
          connection_id: Connection UUID to sample selections against

          n: Number of representative selections requested (must be >= 1)

          query_kater_id: Query UUID to sample selections for

          include_filter_variants: When true, include tier-8 optional filter variants in the sample

          include_pinned_variants: When true, include pinned-variant variants in the sample

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/capabilities/sample",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "n": n,
                    "query_kater_id": query_kater_id,
                    "include_filter_variants": include_filter_variants,
                    "include_pinned_variants": include_pinned_variants,
                },
                capability_sample_params.CapabilitySampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, capability_sample_params.CapabilitySampleParams),
            ),
            cast_to=CapabilitySampleResponse,
        )


class CapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.create = to_raw_response_wrapper(
            capabilities.create,
        )
        self.sample = to_raw_response_wrapper(
            capabilities.sample,
        )


class AsyncCapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.create = async_to_raw_response_wrapper(
            capabilities.create,
        )
        self.sample = async_to_raw_response_wrapper(
            capabilities.sample,
        )


class CapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.create = to_streamed_response_wrapper(
            capabilities.create,
        )
        self.sample = to_streamed_response_wrapper(
            capabilities.sample,
        )


class AsyncCapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.create = async_to_streamed_response_wrapper(
            capabilities.create,
        )
        self.sample = async_to_streamed_response_wrapper(
            capabilities.sample,
        )
