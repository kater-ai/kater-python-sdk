# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .manifest import (
    ManifestResource,
    AsyncManifestResource,
    ManifestResourceWithRawResponse,
    AsyncManifestResourceWithRawResponse,
    ManifestResourceWithStreamingResponse,
    AsyncManifestResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    compiler_render_params,
    compiler_compile_params,
    compiler_execute_params,
    compiler_resolve_params,
    compiler_validate_params,
    compiler_compile_dashboard_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .capabilities import (
    CapabilitiesResource,
    AsyncCapabilitiesResource,
    CapabilitiesResourceWithRawResponse,
    AsyncCapabilitiesResourceWithRawResponse,
    CapabilitiesResourceWithStreamingResponse,
    AsyncCapabilitiesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.v1.compiler_render_response import CompilerRenderResponse
from ....types.v1.compiler_compile_response import CompilerCompileResponse
from ....types.v1.compiler_execute_response import CompilerExecuteResponse
from ....types.v1.compiler_resolve_response import CompilerResolveResponse
from ....types.v1.compiler_validate_response import CompilerValidateResponse
from ....types.v1.compiler_compile_dashboard_response import CompilerCompileDashboardResponse

__all__ = ["CompilerResource", "AsyncCompilerResource"]


class CompilerResource(SyncAPIResource):
    """Validate, resolve, and compile query templates to SQL"""

    @cached_property
    def manifest(self) -> ManifestResource:
        """Validate, resolve, and compile query templates to SQL"""
        return ManifestResource(self._client)

    @cached_property
    def capabilities(self) -> CapabilitiesResource:
        """Validate, resolve, and compile query templates to SQL"""
        return CapabilitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompilerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CompilerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompilerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return CompilerResourceWithStreamingResponse(self)

    def compile(
        self,
        *,
        connection_id: str,
        dashboard: Optional[compiler_compile_params.Dashboard],
        field_selection: compiler_compile_params.FieldSelection,
        filter_state: Iterable[compiler_compile_params.FilterState],
        pinned_variant: Optional[str],
        presentation: compiler_compile_params.Presentation,
        query_kater_id: str,
        result_window: compiler_compile_params.ResultWindow,
        temporal: compiler_compile_params.Temporal,
        variables: Iterable[compiler_compile_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerCompileResponse:
        """
        Compile a structured query request to SQL.

        The structured replacement for `POST /api/v1/compiler/compile`. The handler:

        1. Calls `share_render_request_resolution(...)` to construct per-request
           services.
        2. Calls `RenderService.render(...)` for the full pipeline, then projects the
           response into the compile-stage shape (zeroing execute-only fields). This
           keeps the compile route's canonical-key path identical to the render route's.
        3. Calls `share_response_metadata_builder(...)` with `validate_sort_by=True`.
        4. Projects the `RenderResponse` onto `StructuredCompileResponse` (with
           execute-only fields zeroed).

        Failure mode: resolver/compile failures return HTTP 200 with `success=False`,
        `rendered_query_key=None`, `errors=[...]`. `InvalidSortByError` from the shared
        metadata builder maps to HTTP 400.

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
            "/api/v1/compiler/compile/structured",
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
                compiler_compile_params.CompilerCompileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, compiler_compile_params.CompilerCompileParams),
            ),
            cast_to=CompilerCompileResponse,
        )

    def compile_dashboard(
        self,
        *,
        connection_id: str,
        dashboard_path: str,
        tenant_key: str,
        source: Optional[str] | Omit = omit,
        filter_state: Optional[Iterable[compiler_compile_dashboard_params.FilterState]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerCompileDashboardResponse:
        """
        Compile a dashboard YAML file into fully resolved widget data.

        Reads a dashboard YAML from the client repo, resolves all data slots, executes
        queries, applies filters, and returns renderable widget data.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to compile against

          dashboard_path: Relative path within the connection (e.g. 'dashboards/compliance_overview')

          tenant_key: Tenant key for multi-tenant execution. Use 'kater_global_tenant' for no-tenancy
              clients.

          filter_state: Optional V2 runtime filter-state payload keyed by dashboard filter IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/dashboard",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "dashboard_path": dashboard_path,
                    "tenant_key": tenant_key,
                    "filter_state": filter_state,
                },
                compiler_compile_dashboard_params.CompilerCompileDashboardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"source": source}, compiler_compile_dashboard_params.CompilerCompileDashboardParams
                ),
            ),
            cast_to=CompilerCompileDashboardResponse,
        )

    def execute(
        self,
        *,
        connection_id: str,
        dashboard: Optional[compiler_execute_params.Dashboard],
        field_selection: compiler_execute_params.FieldSelection,
        filter_state: Iterable[compiler_execute_params.FilterState],
        pinned_variant: Optional[str],
        presentation: compiler_execute_params.Presentation,
        query_kater_id: str,
        result_window: compiler_execute_params.ResultWindow,
        temporal: compiler_execute_params.Temporal,
        variables: Iterable[compiler_execute_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerExecuteResponse:
        """
        Execute a structured query request.

        The structured replacement for `POST /api/v1/compiler/execute`. The handler:

        1. Calls `share_render_request_resolution(...)` to construct per-request
           services.
        2. Awaits `RenderService.render(...)` for the full pipeline (resolve
           - compile + execute + widget metadata + canonical key).
        3. Calls `share_response_metadata_builder(...)` with `validate_sort_by=True`.
        4. Projects the `RenderResponse` onto `StructuredExecuteResponse`.

        Failure mode: resolver/compile/execute failures return HTTP 200 with
        `success=False`, `rendered_query_key=None`, `errors=[...]`. `InvalidSortByError`
        from the shared metadata builder maps to HTTP 400.

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
            "/api/v1/compiler/execute/structured",
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
                compiler_execute_params.CompilerExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, compiler_execute_params.CompilerExecuteParams),
            ),
            cast_to=CompilerExecuteResponse,
        )

    def render(
        self,
        *,
        connection_id: str,
        dashboard: Optional[compiler_render_params.Dashboard],
        field_selection: compiler_render_params.FieldSelection,
        filter_state: Iterable[compiler_render_params.FilterState],
        pinned_variant: Optional[str],
        presentation: compiler_render_params.Presentation,
        query_kater_id: str,
        result_window: compiler_render_params.ResultWindow,
        temporal: compiler_render_params.Temporal,
        variables: Iterable[compiler_render_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerRenderResponse:
        """
        Render a query result from a `RenderedQueryRequestV1`.

        This is the structured replacement for
        `POST /api/v1/compiler/combination/preview`. The handler:

        1. Builds per-request `CredentialService`, `ConnectionService`, and
           `CompilerApiService` instances (matching the legacy preview pattern so
           consumer migrations need only swap URL paths).
        2. Resolves tenant parameters via `resolve_tenant_params(...)`. The request body
           itself does not carry a `tenant_key` field today; `NO_TENANT_KEY` is the safe
           migration default.
        3. Wraps the render call in `stage_span("compiler.render", ...)` and records
           pipeline duration in a `finally` block for parity with the legacy preview
           observability.
        4. Awaits `RenderService.render(...)` exactly once.
        5. On success, validates `request.result_window.sort_by` against the compiled
           `column_map` (route-boundary enforcement of the PRD's column_key invariant).
           Invalid `sort_by` raises `ApiError(400, code="invalid_sort_by")` so the
           client receives a clean 400 instead of a successful response with bad
           ordering.
        6. Projects the `RenderResponse` onto `RenderResponseModel` via
           `from_render_response(...)` and returns it.

        Failure-mode contract: resolver/compile/execute failures produce HTTP 200
        responses with `success=False` and `rendered_query_key=None`, matching the
        legacy preview-route behavior so consumers can migrate without changing
        failure-handling logic. `InvalidSortByError` is the sole HTTP 400 path because
        it represents a client request validation error rather than a render-pipeline
        failure.

        Consumer surfaces this route serves (post Stories 4.4, 5.2, 6.1, 6.4, 6.5):
        Query Builder preview/save, SDK widget fetch, dashboard slot render, CLI
        `kater run`, VSCode `runQuery`, chat tool execute.

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
            "/api/v1/compiler/render",
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
                compiler_render_params.CompilerRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, compiler_render_params.CompilerRenderParams),
            ),
            cast_to=CompilerRenderResponse,
        )

    def resolve(
        self,
        *,
        connection_id: str,
        field_selection: compiler_resolve_params.FieldSelection,
        query_kater_id: str,
        source: Optional[str] | Omit = omit,
        auto_fix: bool | Omit = omit,
        dashboard: Optional[compiler_resolve_params.Dashboard] | Omit = omit,
        filter_state: Iterable[compiler_resolve_params.FilterState] | Omit = omit,
        pinned_variant: Optional[str] | Omit = omit,
        presentation: compiler_resolve_params.Presentation | Omit = omit,
        temporal: compiler_resolve_params.Temporal | Omit = omit,
        variables: Iterable[compiler_resolve_params.Variable] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerResolveResponse:
        """
        Resolve a query template from a structured field selection.

        The structured replacement for `POST /api/v1/compiler/resolve`. The handler:

        1. Calls `share_render_request_resolution(...)` to construct per-request
           services + resolve tenant parameters.
        2. Synthesizes a transient `RenderedQueryRequestV1` so the existing
           `RenderService` stage hooks are usable.
        3. Calls `render_service._load_sources(...)`.
        4. Calls `render_service._resolve_selection(...)`. On
           `FieldSelectionValidationError` returns a failure response.
        5. Calls `share_response_metadata_builder(...)` with `validate_sort_by=False`
           (the resolve stage does not produce a `column_map`).
        6. Projects the resolver output onto `StructuredResolveResponse`.

        The route does NOT run compile or execute (Stories 4.4/5.2 issue follow-up
        structured compile/execute calls when the user advances through their workflow).

        Consumer surfaces this route serves (post Stories 4.4, 5.2, 6.1, 6.4, 6.5):
        Query Builder save, SDK pre-fetch, dashboard slot resolve, CLI `kater run`,
        VSCode `runQuery`, chat tool resolve.

        Args:
          field_selection: Structured field selection: source field IDs plus optional grain overrides.

          dashboard: Dashboard context block in `RenderedQueryRequestV1`.

          presentation: Presentation config block in `RenderedQueryRequestV1`.

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
            "/api/v1/compiler/resolve/structured",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "field_selection": field_selection,
                    "query_kater_id": query_kater_id,
                    "auto_fix": auto_fix,
                    "dashboard": dashboard,
                    "filter_state": filter_state,
                    "pinned_variant": pinned_variant,
                    "presentation": presentation,
                    "temporal": temporal,
                    "variables": variables,
                },
                compiler_resolve_params.CompilerResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, compiler_resolve_params.CompilerResolveParams),
            ),
            cast_to=CompilerResolveResponse,
        )

    def validate(
        self,
        *,
        source: Optional[str] | Omit = omit,
        auto_fix: bool | Omit = omit,
        connection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerValidateResponse:
        """
        Validate a schema file set against a connection.

        Checks all views, queries, and related schemas for correctness and returns any
        errors or warnings found.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          auto_fix: Automatically fix broken refs caused by renames. Defaults to True.

          connection_ids: Optional connection IDs to validate. If omitted, validates all connections.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/validate",
            body=maybe_transform(
                {
                    "auto_fix": auto_fix,
                    "connection_ids": connection_ids,
                },
                compiler_validate_params.CompilerValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, compiler_validate_params.CompilerValidateParams),
            ),
            cast_to=CompilerValidateResponse,
        )


class AsyncCompilerResource(AsyncAPIResource):
    """Validate, resolve, and compile query templates to SQL"""

    @cached_property
    def manifest(self) -> AsyncManifestResource:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncManifestResource(self._client)

    @cached_property
    def capabilities(self) -> AsyncCapabilitiesResource:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncCapabilitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompilerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCompilerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompilerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncCompilerResourceWithStreamingResponse(self)

    async def compile(
        self,
        *,
        connection_id: str,
        dashboard: Optional[compiler_compile_params.Dashboard],
        field_selection: compiler_compile_params.FieldSelection,
        filter_state: Iterable[compiler_compile_params.FilterState],
        pinned_variant: Optional[str],
        presentation: compiler_compile_params.Presentation,
        query_kater_id: str,
        result_window: compiler_compile_params.ResultWindow,
        temporal: compiler_compile_params.Temporal,
        variables: Iterable[compiler_compile_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerCompileResponse:
        """
        Compile a structured query request to SQL.

        The structured replacement for `POST /api/v1/compiler/compile`. The handler:

        1. Calls `share_render_request_resolution(...)` to construct per-request
           services.
        2. Calls `RenderService.render(...)` for the full pipeline, then projects the
           response into the compile-stage shape (zeroing execute-only fields). This
           keeps the compile route's canonical-key path identical to the render route's.
        3. Calls `share_response_metadata_builder(...)` with `validate_sort_by=True`.
        4. Projects the `RenderResponse` onto `StructuredCompileResponse` (with
           execute-only fields zeroed).

        Failure mode: resolver/compile failures return HTTP 200 with `success=False`,
        `rendered_query_key=None`, `errors=[...]`. `InvalidSortByError` from the shared
        metadata builder maps to HTTP 400.

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
            "/api/v1/compiler/compile/structured",
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
                compiler_compile_params.CompilerCompileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, compiler_compile_params.CompilerCompileParams),
            ),
            cast_to=CompilerCompileResponse,
        )

    async def compile_dashboard(
        self,
        *,
        connection_id: str,
        dashboard_path: str,
        tenant_key: str,
        source: Optional[str] | Omit = omit,
        filter_state: Optional[Iterable[compiler_compile_dashboard_params.FilterState]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerCompileDashboardResponse:
        """
        Compile a dashboard YAML file into fully resolved widget data.

        Reads a dashboard YAML from the client repo, resolves all data slots, executes
        queries, applies filters, and returns renderable widget data.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to compile against

          dashboard_path: Relative path within the connection (e.g. 'dashboards/compliance_overview')

          tenant_key: Tenant key for multi-tenant execution. Use 'kater_global_tenant' for no-tenancy
              clients.

          filter_state: Optional V2 runtime filter-state payload keyed by dashboard filter IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/dashboard",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "dashboard_path": dashboard_path,
                    "tenant_key": tenant_key,
                    "filter_state": filter_state,
                },
                compiler_compile_dashboard_params.CompilerCompileDashboardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"source": source}, compiler_compile_dashboard_params.CompilerCompileDashboardParams
                ),
            ),
            cast_to=CompilerCompileDashboardResponse,
        )

    async def execute(
        self,
        *,
        connection_id: str,
        dashboard: Optional[compiler_execute_params.Dashboard],
        field_selection: compiler_execute_params.FieldSelection,
        filter_state: Iterable[compiler_execute_params.FilterState],
        pinned_variant: Optional[str],
        presentation: compiler_execute_params.Presentation,
        query_kater_id: str,
        result_window: compiler_execute_params.ResultWindow,
        temporal: compiler_execute_params.Temporal,
        variables: Iterable[compiler_execute_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerExecuteResponse:
        """
        Execute a structured query request.

        The structured replacement for `POST /api/v1/compiler/execute`. The handler:

        1. Calls `share_render_request_resolution(...)` to construct per-request
           services.
        2. Awaits `RenderService.render(...)` for the full pipeline (resolve
           - compile + execute + widget metadata + canonical key).
        3. Calls `share_response_metadata_builder(...)` with `validate_sort_by=True`.
        4. Projects the `RenderResponse` onto `StructuredExecuteResponse`.

        Failure mode: resolver/compile/execute failures return HTTP 200 with
        `success=False`, `rendered_query_key=None`, `errors=[...]`. `InvalidSortByError`
        from the shared metadata builder maps to HTTP 400.

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
            "/api/v1/compiler/execute/structured",
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
                compiler_execute_params.CompilerExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, compiler_execute_params.CompilerExecuteParams),
            ),
            cast_to=CompilerExecuteResponse,
        )

    async def render(
        self,
        *,
        connection_id: str,
        dashboard: Optional[compiler_render_params.Dashboard],
        field_selection: compiler_render_params.FieldSelection,
        filter_state: Iterable[compiler_render_params.FilterState],
        pinned_variant: Optional[str],
        presentation: compiler_render_params.Presentation,
        query_kater_id: str,
        result_window: compiler_render_params.ResultWindow,
        temporal: compiler_render_params.Temporal,
        variables: Iterable[compiler_render_params.Variable],
        source: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerRenderResponse:
        """
        Render a query result from a `RenderedQueryRequestV1`.

        This is the structured replacement for
        `POST /api/v1/compiler/combination/preview`. The handler:

        1. Builds per-request `CredentialService`, `ConnectionService`, and
           `CompilerApiService` instances (matching the legacy preview pattern so
           consumer migrations need only swap URL paths).
        2. Resolves tenant parameters via `resolve_tenant_params(...)`. The request body
           itself does not carry a `tenant_key` field today; `NO_TENANT_KEY` is the safe
           migration default.
        3. Wraps the render call in `stage_span("compiler.render", ...)` and records
           pipeline duration in a `finally` block for parity with the legacy preview
           observability.
        4. Awaits `RenderService.render(...)` exactly once.
        5. On success, validates `request.result_window.sort_by` against the compiled
           `column_map` (route-boundary enforcement of the PRD's column_key invariant).
           Invalid `sort_by` raises `ApiError(400, code="invalid_sort_by")` so the
           client receives a clean 400 instead of a successful response with bad
           ordering.
        6. Projects the `RenderResponse` onto `RenderResponseModel` via
           `from_render_response(...)` and returns it.

        Failure-mode contract: resolver/compile/execute failures produce HTTP 200
        responses with `success=False` and `rendered_query_key=None`, matching the
        legacy preview-route behavior so consumers can migrate without changing
        failure-handling logic. `InvalidSortByError` is the sole HTTP 400 path because
        it represents a client request validation error rather than a render-pipeline
        failure.

        Consumer surfaces this route serves (post Stories 4.4, 5.2, 6.1, 6.4, 6.5):
        Query Builder preview/save, SDK widget fetch, dashboard slot render, CLI
        `kater run`, VSCode `runQuery`, chat tool execute.

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
            "/api/v1/compiler/render",
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
                compiler_render_params.CompilerRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, compiler_render_params.CompilerRenderParams),
            ),
            cast_to=CompilerRenderResponse,
        )

    async def resolve(
        self,
        *,
        connection_id: str,
        field_selection: compiler_resolve_params.FieldSelection,
        query_kater_id: str,
        source: Optional[str] | Omit = omit,
        auto_fix: bool | Omit = omit,
        dashboard: Optional[compiler_resolve_params.Dashboard] | Omit = omit,
        filter_state: Iterable[compiler_resolve_params.FilterState] | Omit = omit,
        pinned_variant: Optional[str] | Omit = omit,
        presentation: compiler_resolve_params.Presentation | Omit = omit,
        temporal: compiler_resolve_params.Temporal | Omit = omit,
        variables: Iterable[compiler_resolve_params.Variable] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerResolveResponse:
        """
        Resolve a query template from a structured field selection.

        The structured replacement for `POST /api/v1/compiler/resolve`. The handler:

        1. Calls `share_render_request_resolution(...)` to construct per-request
           services + resolve tenant parameters.
        2. Synthesizes a transient `RenderedQueryRequestV1` so the existing
           `RenderService` stage hooks are usable.
        3. Calls `render_service._load_sources(...)`.
        4. Calls `render_service._resolve_selection(...)`. On
           `FieldSelectionValidationError` returns a failure response.
        5. Calls `share_response_metadata_builder(...)` with `validate_sort_by=False`
           (the resolve stage does not produce a `column_map`).
        6. Projects the resolver output onto `StructuredResolveResponse`.

        The route does NOT run compile or execute (Stories 4.4/5.2 issue follow-up
        structured compile/execute calls when the user advances through their workflow).

        Consumer surfaces this route serves (post Stories 4.4, 5.2, 6.1, 6.4, 6.5):
        Query Builder save, SDK pre-fetch, dashboard slot resolve, CLI `kater run`,
        VSCode `runQuery`, chat tool resolve.

        Args:
          field_selection: Structured field selection: source field IDs plus optional grain overrides.

          dashboard: Dashboard context block in `RenderedQueryRequestV1`.

          presentation: Presentation config block in `RenderedQueryRequestV1`.

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
            "/api/v1/compiler/resolve/structured",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "field_selection": field_selection,
                    "query_kater_id": query_kater_id,
                    "auto_fix": auto_fix,
                    "dashboard": dashboard,
                    "filter_state": filter_state,
                    "pinned_variant": pinned_variant,
                    "presentation": presentation,
                    "temporal": temporal,
                    "variables": variables,
                },
                compiler_resolve_params.CompilerResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, compiler_resolve_params.CompilerResolveParams),
            ),
            cast_to=CompilerResolveResponse,
        )

    async def validate(
        self,
        *,
        source: Optional[str] | Omit = omit,
        auto_fix: bool | Omit = omit,
        connection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerValidateResponse:
        """
        Validate a schema file set against a connection.

        Checks all views, queries, and related schemas for correctness and returns any
        errors or warnings found.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          auto_fix: Automatically fix broken refs caused by renames. Defaults to True.

          connection_ids: Optional connection IDs to validate. If omitted, validates all connections.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/validate",
            body=await async_maybe_transform(
                {
                    "auto_fix": auto_fix,
                    "connection_ids": connection_ids,
                },
                compiler_validate_params.CompilerValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"source": source}, compiler_validate_params.CompilerValidateParams),
            ),
            cast_to=CompilerValidateResponse,
        )


class CompilerResourceWithRawResponse:
    def __init__(self, compiler: CompilerResource) -> None:
        self._compiler = compiler

        self.compile = to_raw_response_wrapper(
            compiler.compile,
        )
        self.compile_dashboard = to_raw_response_wrapper(
            compiler.compile_dashboard,
        )
        self.execute = to_raw_response_wrapper(
            compiler.execute,
        )
        self.render = to_raw_response_wrapper(
            compiler.render,
        )
        self.resolve = to_raw_response_wrapper(
            compiler.resolve,
        )
        self.validate = to_raw_response_wrapper(
            compiler.validate,
        )

    @cached_property
    def manifest(self) -> ManifestResourceWithRawResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return ManifestResourceWithRawResponse(self._compiler.manifest)

    @cached_property
    def capabilities(self) -> CapabilitiesResourceWithRawResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return CapabilitiesResourceWithRawResponse(self._compiler.capabilities)


class AsyncCompilerResourceWithRawResponse:
    def __init__(self, compiler: AsyncCompilerResource) -> None:
        self._compiler = compiler

        self.compile = async_to_raw_response_wrapper(
            compiler.compile,
        )
        self.compile_dashboard = async_to_raw_response_wrapper(
            compiler.compile_dashboard,
        )
        self.execute = async_to_raw_response_wrapper(
            compiler.execute,
        )
        self.render = async_to_raw_response_wrapper(
            compiler.render,
        )
        self.resolve = async_to_raw_response_wrapper(
            compiler.resolve,
        )
        self.validate = async_to_raw_response_wrapper(
            compiler.validate,
        )

    @cached_property
    def manifest(self) -> AsyncManifestResourceWithRawResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncManifestResourceWithRawResponse(self._compiler.manifest)

    @cached_property
    def capabilities(self) -> AsyncCapabilitiesResourceWithRawResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncCapabilitiesResourceWithRawResponse(self._compiler.capabilities)


class CompilerResourceWithStreamingResponse:
    def __init__(self, compiler: CompilerResource) -> None:
        self._compiler = compiler

        self.compile = to_streamed_response_wrapper(
            compiler.compile,
        )
        self.compile_dashboard = to_streamed_response_wrapper(
            compiler.compile_dashboard,
        )
        self.execute = to_streamed_response_wrapper(
            compiler.execute,
        )
        self.render = to_streamed_response_wrapper(
            compiler.render,
        )
        self.resolve = to_streamed_response_wrapper(
            compiler.resolve,
        )
        self.validate = to_streamed_response_wrapper(
            compiler.validate,
        )

    @cached_property
    def manifest(self) -> ManifestResourceWithStreamingResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return ManifestResourceWithStreamingResponse(self._compiler.manifest)

    @cached_property
    def capabilities(self) -> CapabilitiesResourceWithStreamingResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return CapabilitiesResourceWithStreamingResponse(self._compiler.capabilities)


class AsyncCompilerResourceWithStreamingResponse:
    def __init__(self, compiler: AsyncCompilerResource) -> None:
        self._compiler = compiler

        self.compile = async_to_streamed_response_wrapper(
            compiler.compile,
        )
        self.compile_dashboard = async_to_streamed_response_wrapper(
            compiler.compile_dashboard,
        )
        self.execute = async_to_streamed_response_wrapper(
            compiler.execute,
        )
        self.render = async_to_streamed_response_wrapper(
            compiler.render,
        )
        self.resolve = async_to_streamed_response_wrapper(
            compiler.resolve,
        )
        self.validate = async_to_streamed_response_wrapper(
            compiler.validate,
        )

    @cached_property
    def manifest(self) -> AsyncManifestResourceWithStreamingResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncManifestResourceWithStreamingResponse(self._compiler.manifest)

    @cached_property
    def capabilities(self) -> AsyncCapabilitiesResourceWithStreamingResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncCapabilitiesResourceWithStreamingResponse(self._compiler.capabilities)
