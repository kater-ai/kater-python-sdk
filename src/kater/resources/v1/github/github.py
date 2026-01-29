# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import github_connect_params, github_callback_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.github_connect_response import GitHubConnectResponse
from ....types.v1.github_get_status_response import GitHubGetStatusResponse
from ....types.v1.github_get_installation_link_response import GitHubGetInstallationLinkResponse

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

    def callback(
        self,
        *,
        state: str,
        code: Optional[str] | Omit = omit,
        error: Optional[str] | Omit = omit,
        error_description: Optional[str] | Omit = omit,
        installation_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles the OAuth callback from GitHub after user authorization.

        Args:
          state: State token for CSRF validation

          code: OAuth authorization code

          error: OAuth error code from GitHub

          error_description: OAuth error description

          installation_id: GitHub App installation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/github/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "state": state,
                        "code": code,
                        "error": error,
                        "error_description": error_description,
                        "installation_id": installation_id,
                    },
                    github_callback_params.GitHubCallbackParams,
                ),
            ),
            cast_to=object,
        )

    def connect(
        self,
        *,
        return_to: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubConnectResponse:
        """
        Initiates the GitHub App installation flow.

        Args:
          return_to: Frontend path to redirect to after OAuth success (e.g., '/' or
              '/settings/github')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/github/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"return_to": return_to}, github_connect_params.GitHubConnectParams),
            ),
            cast_to=GitHubConnectResponse,
        )

    def get_installation_link(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubGetInstallationLinkResponse:
        """Generates a shareable GitHub App installation link."""
        return self._get(
            "/api/v1/github/installation-link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubGetInstallationLinkResponse,
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

    async def callback(
        self,
        *,
        state: str,
        code: Optional[str] | Omit = omit,
        error: Optional[str] | Omit = omit,
        error_description: Optional[str] | Omit = omit,
        installation_id: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles the OAuth callback from GitHub after user authorization.

        Args:
          state: State token for CSRF validation

          code: OAuth authorization code

          error: OAuth error code from GitHub

          error_description: OAuth error description

          installation_id: GitHub App installation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/github/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "state": state,
                        "code": code,
                        "error": error,
                        "error_description": error_description,
                        "installation_id": installation_id,
                    },
                    github_callback_params.GitHubCallbackParams,
                ),
            ),
            cast_to=object,
        )

    async def connect(
        self,
        *,
        return_to: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubConnectResponse:
        """
        Initiates the GitHub App installation flow.

        Args:
          return_to: Frontend path to redirect to after OAuth success (e.g., '/' or
              '/settings/github')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/github/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"return_to": return_to}, github_connect_params.GitHubConnectParams),
            ),
            cast_to=GitHubConnectResponse,
        )

    async def get_installation_link(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubGetInstallationLinkResponse:
        """Generates a shareable GitHub App installation link."""
        return await self._get(
            "/api/v1/github/installation-link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubGetInstallationLinkResponse,
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


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.callback = to_raw_response_wrapper(
            github.callback,
        )
        self.connect = to_raw_response_wrapper(
            github.connect,
        )
        self.get_installation_link = to_raw_response_wrapper(
            github.get_installation_link,
        )
        self.get_status = to_raw_response_wrapper(
            github.get_status,
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


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.callback = async_to_raw_response_wrapper(
            github.callback,
        )
        self.connect = async_to_raw_response_wrapper(
            github.connect,
        )
        self.get_installation_link = async_to_raw_response_wrapper(
            github.get_installation_link,
        )
        self.get_status = async_to_raw_response_wrapper(
            github.get_status,
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


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.callback = to_streamed_response_wrapper(
            github.callback,
        )
        self.connect = to_streamed_response_wrapper(
            github.connect,
        )
        self.get_installation_link = to_streamed_response_wrapper(
            github.get_installation_link,
        )
        self.get_status = to_streamed_response_wrapper(
            github.get_status,
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


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.callback = async_to_streamed_response_wrapper(
            github.callback,
        )
        self.connect = async_to_streamed_response_wrapper(
            github.connect,
        )
        self.get_installation_link = async_to_streamed_response_wrapper(
            github.get_installation_link,
        )
        self.get_status = async_to_streamed_response_wrapper(
            github.get_status,
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
