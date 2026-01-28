# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1 import GitHubGetStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitHub:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Kater) -> None:
        github = client.v1.github.get_status()
        assert_matches_type(GitHubGetStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Kater) -> None:
        response = client.v1.github.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert_matches_type(GitHubGetStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Kater) -> None:
        with client.v1.github.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert_matches_type(GitHubGetStatusResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGitHub:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncKater) -> None:
        github = await async_client.v1.github.get_status()
        assert_matches_type(GitHubGetStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.github.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert_matches_type(GitHubGetStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncKater) -> None:
        async with async_client.v1.github.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert_matches_type(GitHubGetStatusResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True
