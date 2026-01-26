# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .client import (
    ClientResource,
    AsyncClientResource,
    ClientResourceWithRawResponse,
    AsyncClientResourceWithRawResponse,
    ClientResourceWithStreamingResponse,
    AsyncClientResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def client(self) -> ClientResource:
        return ClientResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def client(self) -> AsyncClientResource:
        return AsyncClientResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def client(self) -> ClientResourceWithRawResponse:
        return ClientResourceWithRawResponse(self._org.client)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._org.users)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def client(self) -> AsyncClientResourceWithRawResponse:
        return AsyncClientResourceWithRawResponse(self._org.client)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._org.users)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def client(self) -> ClientResourceWithStreamingResponse:
        return ClientResourceWithStreamingResponse(self._org.client)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._org.users)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def client(self) -> AsyncClientResourceWithStreamingResponse:
        return AsyncClientResourceWithStreamingResponse(self._org.client)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._org.users)
