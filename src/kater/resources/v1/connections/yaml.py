# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.v1.connections import yaml_commit_yaml_params
from ....types.v1.connections.yaml_commit_yaml_response import YamlCommitYamlResponse
from ....types.v1.connections.yaml_retrieve_yaml_response import YamlRetrieveYamlResponse

__all__ = ["YamlResource", "AsyncYamlResource"]


class YamlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> YamlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return YamlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> YamlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return YamlResourceWithStreamingResponse(self)

    def commit_yaml(
        self,
        connection_id: str,
        *,
        yaml_content: str,
        auto_merge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YamlCommitYamlResponse:
        """
        Commit updated YAML to a new branch and create a PR.

        Args:
          yaml_content: Updated YAML content

          auto_merge: If true, auto-merge the PR after creation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/api/v1/connections/{connection_id}/yaml",
            body=maybe_transform(
                {
                    "yaml_content": yaml_content,
                    "auto_merge": auto_merge,
                },
                yaml_commit_yaml_params.YamlCommitYamlParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YamlCommitYamlResponse,
        )

    def retrieve_yaml(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YamlRetrieveYamlResponse:
        """
        Read connection.yaml from the main branch of the repo.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/api/v1/connections/{connection_id}/yaml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YamlRetrieveYamlResponse,
        )


class AsyncYamlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncYamlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncYamlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncYamlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncYamlResourceWithStreamingResponse(self)

    async def commit_yaml(
        self,
        connection_id: str,
        *,
        yaml_content: str,
        auto_merge: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YamlCommitYamlResponse:
        """
        Commit updated YAML to a new branch and create a PR.

        Args:
          yaml_content: Updated YAML content

          auto_merge: If true, auto-merge the PR after creation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/api/v1/connections/{connection_id}/yaml",
            body=await async_maybe_transform(
                {
                    "yaml_content": yaml_content,
                    "auto_merge": auto_merge,
                },
                yaml_commit_yaml_params.YamlCommitYamlParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YamlCommitYamlResponse,
        )

    async def retrieve_yaml(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YamlRetrieveYamlResponse:
        """
        Read connection.yaml from the main branch of the repo.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/api/v1/connections/{connection_id}/yaml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YamlRetrieveYamlResponse,
        )


class YamlResourceWithRawResponse:
    def __init__(self, yaml: YamlResource) -> None:
        self._yaml = yaml

        self.commit_yaml = to_raw_response_wrapper(
            yaml.commit_yaml,
        )
        self.retrieve_yaml = to_raw_response_wrapper(
            yaml.retrieve_yaml,
        )


class AsyncYamlResourceWithRawResponse:
    def __init__(self, yaml: AsyncYamlResource) -> None:
        self._yaml = yaml

        self.commit_yaml = async_to_raw_response_wrapper(
            yaml.commit_yaml,
        )
        self.retrieve_yaml = async_to_raw_response_wrapper(
            yaml.retrieve_yaml,
        )


class YamlResourceWithStreamingResponse:
    def __init__(self, yaml: YamlResource) -> None:
        self._yaml = yaml

        self.commit_yaml = to_streamed_response_wrapper(
            yaml.commit_yaml,
        )
        self.retrieve_yaml = to_streamed_response_wrapper(
            yaml.retrieve_yaml,
        )


class AsyncYamlResourceWithStreamingResponse:
    def __init__(self, yaml: AsyncYamlResource) -> None:
        self._yaml = yaml

        self.commit_yaml = async_to_streamed_response_wrapper(
            yaml.commit_yaml,
        )
        self.retrieve_yaml = async_to_streamed_response_wrapper(
            yaml.retrieve_yaml,
        )
