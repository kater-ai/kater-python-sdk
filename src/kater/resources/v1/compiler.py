# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    compiler_compile_params,
    compiler_execute_params,
    compiler_resolve_params,
    compiler_validate_params,
    compiler_enumerate_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.compiler_compile_response import CompilerCompileResponse
from ...types.v1.compiler_execute_response import CompilerExecuteResponse
from ...types.v1.compiler_resolve_response import CompilerResolveResponse
from ...types.v1.compiler_validate_response import CompilerValidateResponse
from ...types.v1.compiler_enumerate_response import CompilerEnumerateResponse

__all__ = ["CompilerResource", "AsyncCompilerResource"]


class CompilerResource(SyncAPIResource):
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
        resolved_query: compiler_compile_params.ResolvedQuery,
        source: Optional[str] | Omit = omit,
        tenant_key: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerCompileResponse:
        """
        Compile a resolved query to SQL.

        Takes a previously resolved query and generates the final SQL statement for the
        target dialect.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to compile against

          resolved_query: Previously resolved query object from /resolve

          tenant_key: Tenant key for multi-tenant compilation. For database tenancy, maps to the
              tenant's database. For row tenancy, used as the row-level filter value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/compile",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "resolved_query": resolved_query,
                    "tenant_key": tenant_key,
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

    def enumerate(
        self,
        *,
        connection_id: str,
        source: Optional[str] | Omit = omit,
        query_refs: Optional[SequenceNotStr[str]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerEnumerateResponse:
        """
        Enumerate every valid query configuration for a connection.

        Generates all valid combinations of optional dimensions, measures, calculations,
        filters, and variable values, constrained by widget category rules.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to enumerate against

          query_refs: Optional query refs to limit enumeration. If omitted, enumerates all queries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/enumerate",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "query_refs": query_refs,
                },
                compiler_enumerate_params.CompilerEnumerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, compiler_enumerate_params.CompilerEnumerateParams),
            ),
            cast_to=CompilerEnumerateResponse,
        )

    def execute(
        self,
        *,
        connection_id: str,
        resolved_query: compiler_execute_params.ResolvedQuery,
        source: Optional[str] | Omit = omit,
        tenant_key: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerExecuteResponse:
        """
        Execute a query with transparent caching.

        Compiles the resolved query to SQL, checks the cache for existing results,
        executes against the warehouse on cache miss, and stores the result for future
        requests. Cache failures are invisible to the caller.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to execute against

          resolved_query: Previously resolved query object from /resolve

          tenant_key: Tenant key for multi-tenant execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/execute",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "resolved_query": resolved_query,
                    "tenant_key": tenant_key,
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

    def resolve(
        self,
        *,
        connection_id: str,
        query_ref: str,
        source: Optional[str] | Omit = omit,
        combination: str | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerResolveResponse:
        """
        Resolve a query template with user-selected parameters.

        Takes a query reference and variable selections, returns the fully resolved
        query object ready for compilation.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to resolve against

          query_ref: Reference to the query template (e.g. 'ref(MY_QUERY)')

          combination:
              Comma-separated slot selections and variable assignments. Reserved keys:
              measure, dimension, filter, calculation. All other keys are variable
              assignments. Example: 'measure=Compliance
              Rate,dimension=Department,breakdown=region'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/resolve",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "query_ref": query_ref,
                    "combination": combination,
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
          connection_ids: Optional connection IDs to validate. If omitted, validates all connections.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return self._post(
            "/api/v1/compiler/validate",
            body=maybe_transform({"connection_ids": connection_ids}, compiler_validate_params.CompilerValidateParams),
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
        resolved_query: compiler_compile_params.ResolvedQuery,
        source: Optional[str] | Omit = omit,
        tenant_key: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerCompileResponse:
        """
        Compile a resolved query to SQL.

        Takes a previously resolved query and generates the final SQL statement for the
        target dialect.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to compile against

          resolved_query: Previously resolved query object from /resolve

          tenant_key: Tenant key for multi-tenant compilation. For database tenancy, maps to the
              tenant's database. For row tenancy, used as the row-level filter value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/compile",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "resolved_query": resolved_query,
                    "tenant_key": tenant_key,
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

    async def enumerate(
        self,
        *,
        connection_id: str,
        source: Optional[str] | Omit = omit,
        query_refs: Optional[SequenceNotStr[str]] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerEnumerateResponse:
        """
        Enumerate every valid query configuration for a connection.

        Generates all valid combinations of optional dimensions, measures, calculations,
        filters, and variable values, constrained by widget category rules.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to enumerate against

          query_refs: Optional query refs to limit enumeration. If omitted, enumerates all queries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/enumerate",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "query_refs": query_refs,
                },
                compiler_enumerate_params.CompilerEnumerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"source": source}, compiler_enumerate_params.CompilerEnumerateParams
                ),
            ),
            cast_to=CompilerEnumerateResponse,
        )

    async def execute(
        self,
        *,
        connection_id: str,
        resolved_query: compiler_execute_params.ResolvedQuery,
        source: Optional[str] | Omit = omit,
        tenant_key: Optional[str] | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerExecuteResponse:
        """
        Execute a query with transparent caching.

        Compiles the resolved query to SQL, checks the cache for existing results,
        executes against the warehouse on cache miss, and stores the result for future
        requests. Cache failures are invisible to the caller.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to execute against

          resolved_query: Previously resolved query object from /resolve

          tenant_key: Tenant key for multi-tenant execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/execute",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "resolved_query": resolved_query,
                    "tenant_key": tenant_key,
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

    async def resolve(
        self,
        *,
        connection_id: str,
        query_ref: str,
        source: Optional[str] | Omit = omit,
        combination: str | Omit = omit,
        x_kater_cli_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompilerResolveResponse:
        """
        Resolve a query template with user-selected parameters.

        Takes a query reference and variable selections, returns the fully resolved
        query object ready for compilation.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          connection_id: Connection to resolve against

          query_ref: Reference to the query template (e.g. 'ref(MY_QUERY)')

          combination:
              Comma-separated slot selections and variable assignments. Reserved keys:
              measure, dimension, filter, calculation. All other keys are variable
              assignments. Example: 'measure=Compliance
              Rate,dimension=Department,breakdown=region'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Kater-CLI-ID": x_kater_cli_id}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/compiler/resolve",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "query_ref": query_ref,
                    "combination": combination,
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
                {"connection_ids": connection_ids}, compiler_validate_params.CompilerValidateParams
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
        self.enumerate = to_raw_response_wrapper(
            compiler.enumerate,
        )
        self.execute = to_raw_response_wrapper(
            compiler.execute,
        )
        self.resolve = to_raw_response_wrapper(
            compiler.resolve,
        )
        self.validate = to_raw_response_wrapper(
            compiler.validate,
        )


class AsyncCompilerResourceWithRawResponse:
    def __init__(self, compiler: AsyncCompilerResource) -> None:
        self._compiler = compiler

        self.compile = async_to_raw_response_wrapper(
            compiler.compile,
        )
        self.enumerate = async_to_raw_response_wrapper(
            compiler.enumerate,
        )
        self.execute = async_to_raw_response_wrapper(
            compiler.execute,
        )
        self.resolve = async_to_raw_response_wrapper(
            compiler.resolve,
        )
        self.validate = async_to_raw_response_wrapper(
            compiler.validate,
        )


class CompilerResourceWithStreamingResponse:
    def __init__(self, compiler: CompilerResource) -> None:
        self._compiler = compiler

        self.compile = to_streamed_response_wrapper(
            compiler.compile,
        )
        self.enumerate = to_streamed_response_wrapper(
            compiler.enumerate,
        )
        self.execute = to_streamed_response_wrapper(
            compiler.execute,
        )
        self.resolve = to_streamed_response_wrapper(
            compiler.resolve,
        )
        self.validate = to_streamed_response_wrapper(
            compiler.validate,
        )


class AsyncCompilerResourceWithStreamingResponse:
    def __init__(self, compiler: AsyncCompilerResource) -> None:
        self._compiler = compiler

        self.compile = async_to_streamed_response_wrapper(
            compiler.compile,
        )
        self.enumerate = async_to_streamed_response_wrapper(
            compiler.enumerate,
        )
        self.execute = async_to_streamed_response_wrapper(
            compiler.execute,
        )
        self.resolve = async_to_streamed_response_wrapper(
            compiler.resolve,
        )
        self.validate = async_to_streamed_response_wrapper(
            compiler.validate,
        )
