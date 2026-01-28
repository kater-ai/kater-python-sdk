# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.v1.github_get_status_response import GitHubGetStatusResponse

__all__ = ["GitHubResource", "AsyncGitHubResource"]


class GitHubResource(SyncAPIResource):
    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def scaffold(self) -> ScaffoldResource:
        return ScaffoldResource(self._client)

    @cached_property
    def with_raw_response(self) -> GitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return GitHubResourceWithStreamingResponse(self)

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


class AsyncGitHubResource(AsyncAPIResource):
    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def scaffold(self) -> AsyncScaffoldResource:
        return AsyncScaffoldResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncGitHubResourceWithStreamingResponse(self)

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


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.get_status = to_raw_response_wrapper(
            github.get_status,
        )

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> ScaffoldResourceWithRawResponse:
        return ScaffoldResourceWithRawResponse(self._github.scaffold)


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.get_status = async_to_raw_response_wrapper(
            github.get_status,
        )

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> AsyncScaffoldResourceWithRawResponse:
        return AsyncScaffoldResourceWithRawResponse(self._github.scaffold)


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.get_status = to_streamed_response_wrapper(
            github.get_status,
        )

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> ScaffoldResourceWithStreamingResponse:
        return ScaffoldResourceWithStreamingResponse(self._github.scaffold)


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.get_status = async_to_streamed_response_wrapper(
            github.get_status,
        )

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._github.repos)

    @cached_property
    def scaffold(self) -> AsyncScaffoldResourceWithStreamingResponse:
        return AsyncScaffoldResourceWithStreamingResponse(self._github.scaffold)
