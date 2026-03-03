# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)
from .tenants.tenants import (
    TenantsResource,
    AsyncTenantsResource,
    TenantsResourceWithRawResponse,
    AsyncTenantsResourceWithRawResponse,
    TenantsResourceWithStreamingResponse,
    AsyncTenantsResourceWithStreamingResponse,
)
from .compiler.compiler import (
    CompilerResource,
    AsyncCompilerResource,
    CompilerResourceWithRawResponse,
    AsyncCompilerResourceWithRawResponse,
    CompilerResourceWithStreamingResponse,
    AsyncCompilerResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def compiler(self) -> CompilerResource:
        """Validate, resolve, and compile query templates to SQL"""
        return CompilerResource(self._client)

    @cached_property
    def connections(self) -> ConnectionsResource:
        """Manage database connections to your data warehouse"""
        return ConnectionsResource(self._client)

    @cached_property
    def tenants(self) -> TenantsResource:
        """Manage tenants (your end customers)"""
        return TenantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def compiler(self) -> AsyncCompilerResource:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncCompilerResource(self._client)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        """Manage database connections to your data warehouse"""
        return AsyncConnectionsResource(self._client)

    @cached_property
    def tenants(self) -> AsyncTenantsResource:
        """Manage tenants (your end customers)"""
        return AsyncTenantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def compiler(self) -> CompilerResourceWithRawResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return CompilerResourceWithRawResponse(self._v1.compiler)

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        """Manage database connections to your data warehouse"""
        return ConnectionsResourceWithRawResponse(self._v1.connections)

    @cached_property
    def tenants(self) -> TenantsResourceWithRawResponse:
        """Manage tenants (your end customers)"""
        return TenantsResourceWithRawResponse(self._v1.tenants)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def compiler(self) -> AsyncCompilerResourceWithRawResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncCompilerResourceWithRawResponse(self._v1.compiler)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        """Manage database connections to your data warehouse"""
        return AsyncConnectionsResourceWithRawResponse(self._v1.connections)

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithRawResponse:
        """Manage tenants (your end customers)"""
        return AsyncTenantsResourceWithRawResponse(self._v1.tenants)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def compiler(self) -> CompilerResourceWithStreamingResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return CompilerResourceWithStreamingResponse(self._v1.compiler)

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        """Manage database connections to your data warehouse"""
        return ConnectionsResourceWithStreamingResponse(self._v1.connections)

    @cached_property
    def tenants(self) -> TenantsResourceWithStreamingResponse:
        """Manage tenants (your end customers)"""
        return TenantsResourceWithStreamingResponse(self._v1.tenants)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def compiler(self) -> AsyncCompilerResourceWithStreamingResponse:
        """Validate, resolve, and compile query templates to SQL"""
        return AsyncCompilerResourceWithStreamingResponse(self._v1.compiler)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """Manage database connections to your data warehouse"""
        return AsyncConnectionsResourceWithStreamingResponse(self._v1.connections)

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithStreamingResponse:
        """Manage tenants (your end customers)"""
        return AsyncTenantsResourceWithStreamingResponse(self._v1.tenants)
