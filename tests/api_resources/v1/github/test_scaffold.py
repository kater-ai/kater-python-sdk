# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.github import ScaffoldTrigger

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScaffold:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retry(self, client: Kater) -> None:
        scaffold = client.v1.github.scaffold.retry()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: Kater) -> None:
        response = client.v1.github.scaffold.with_raw_response.retry()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scaffold = response.parse()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: Kater) -> None:
        with client.v1.github.scaffold.with_streaming_response.retry() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scaffold = response.parse()
            assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger(self, client: Kater) -> None:
        scaffold = client.v1.github.scaffold.trigger()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger(self, client: Kater) -> None:
        response = client.v1.github.scaffold.with_raw_response.trigger()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scaffold = response.parse()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger(self, client: Kater) -> None:
        with client.v1.github.scaffold.with_streaming_response.trigger() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scaffold = response.parse()
            assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScaffold:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncKater) -> None:
        scaffold = await async_client.v1.github.scaffold.retry()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.github.scaffold.with_raw_response.retry()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scaffold = await response.parse()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncKater) -> None:
        async with async_client.v1.github.scaffold.with_streaming_response.retry() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scaffold = await response.parse()
            assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger(self, async_client: AsyncKater) -> None:
        scaffold = await async_client.v1.github.scaffold.trigger()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.github.scaffold.with_raw_response.trigger()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scaffold = await response.parse()
        assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncKater) -> None:
        async with async_client.v1.github.scaffold.with_streaming_response.trigger() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scaffold = await response.parse()
            assert_matches_type(ScaffoldTrigger, scaffold, path=["response"])

        assert cast(Any, response.is_closed) is True
