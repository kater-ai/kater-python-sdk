# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from .repos import (
    ReposResource,
    AsyncReposResource,
    ReposResourceWithRawResponse,
    AsyncReposResourceWithRawResponse,
    ReposResourceWithStreamingResponse,
    AsyncReposResourceWithStreamingResponse,
)
from .scaffold import (
    ScaffoldResource,
    AsyncScaffoldResource,
    ScaffoldResourceWithRawResponse,
    AsyncScaffoldResourceWithRawResponse,
    ScaffoldResourceWithStreamingResponse,
    AsyncScaffoldResourceWithStreamingResponse,
)
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
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
from ....types.v1.github_sync_response import GitHubSyncResponse
from ....types.v1.github_disconnect_response import GitHubDisconnectResponse
from ....types.v1.github_get_status_response import GitHubGetStatusResponse
from ....types.v1.github_check_installations_response import GitHubCheckInstallationsResponse

__all__ = ["GitHubResource", "AsyncGitHubResource"]


class GitHubResource(SyncAPIResource):
    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def scaffold(self) -> ScaffoldResource:
        return ScaffoldResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> GitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/kater-python#accessing-raw-response-data-eg-headers
        """
        return GitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/kater-python#with_streaming_response
        """
        return GitHubResourceWithStreamingResponse(self)

    def check_installations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubCheckInstallationsResponse:
        """Checks if the GitHub App is already installed on any organizations/accounts."""
        return self._get(
            "/api/v1/github/check-installations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubCheckInstallationsResponse,
        )

    def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubDisconnectResponse:
        """Disconnects the GitHub connection."""
        return self._post(
            "/api/v1/github/disconnect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubDisconnectResponse,
        )

    def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubGetStatusResponse:
        """Returns the current GitHub connection status for the client."""
        return self._get(
            "/api/v1/github/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubGetStatusResponse,
        )

    def sync(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubSyncResponse:
        """Verifies the GitHub connection and updates the last sync timestamp."""
        return self._post(
            "/api/v1/github/sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubSyncResponse,
        )


class AsyncGitHubResource(AsyncAPIResource):
    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def scaffold(self) -> AsyncScaffoldResource:
        return AsyncScaffoldResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/kater-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/kater-python#with_streaming_response
        """
        return AsyncGitHubResourceWithStreamingResponse(self)

    async def check_installations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubCheckInstallationsResponse:
        """Checks if the GitHub App is already installed on any organizations/accounts."""
        return await self._get(
            "/api/v1/github/check-installations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubCheckInstallationsResponse,
        )

    async def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubDisconnectResponse:
        """Disconnects the GitHub connection."""
        return await self._post(
            "/api/v1/github/disconnect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubDisconnectResponse,
        )

    async def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubGetStatusResponse:
        """Returns the current GitHub connection status for the client."""
        return await self._get(
            "/api/v1/github/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubGetStatusResponse,
        )

    async def sync(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubSyncResponse:
        """Verifies the GitHub connection and updates the last sync timestamp."""
        return await self._post(
            "/api/v1/github/sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubSyncResponse,
        )


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.check_installations = to_raw_response_wrapper(
            github.check_installations,
        )
        self.disconnect = to_raw_response_wrapper(
            github.disconnect,
        )
        self.get_status = to_raw_response_wrapper(
            github.get_status,
        )
        self.sync = to_raw_response_wrapper(
            github.sync,
        )

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> ScaffoldResourceWithRawResponse:
        return ScaffoldResourceWithRawResponse(self._github.scaffold)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._github.webhooks)

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._github.admin)


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.check_installations = async_to_raw_response_wrapper(
            github.check_installations,
        )
        self.disconnect = async_to_raw_response_wrapper(
            github.disconnect,
        )
        self.get_status = async_to_raw_response_wrapper(
            github.get_status,
        )
        self.sync = async_to_raw_response_wrapper(
            github.sync,
        )

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> AsyncScaffoldResourceWithRawResponse:
        return AsyncScaffoldResourceWithRawResponse(self._github.scaffold)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._github.webhooks)

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._github.admin)


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.check_installations = to_streamed_response_wrapper(
            github.check_installations,
        )
        self.disconnect = to_streamed_response_wrapper(
            github.disconnect,
        )
        self.get_status = to_streamed_response_wrapper(
            github.get_status,
        )
        self.sync = to_streamed_response_wrapper(
            github.sync,
        )

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> ScaffoldResourceWithStreamingResponse:
        return ScaffoldResourceWithStreamingResponse(self._github.scaffold)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._github.webhooks)

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._github.admin)


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.check_installations = async_to_streamed_response_wrapper(
            github.check_installations,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            github.disconnect,
        )
        self.get_status = async_to_streamed_response_wrapper(
            github.get_status,
        )
        self.sync = async_to_streamed_response_wrapper(
            github.sync,
        )

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> AsyncScaffoldResourceWithStreamingResponse:
        return AsyncScaffoldResourceWithStreamingResponse(self._github.scaffold)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._github.webhooks)

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._github.admin)
