# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.compiler import CacheInvalidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invalidate(self, client: Kater) -> None:
        cache = client.v1.compiler.cache.invalidate(
            client_id="client_id",
        )
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invalidate_with_all_params(self, client: Kater) -> None:
        cache = client.v1.compiler.cache.invalidate(
            client_id="client_id",
            connection_id="connection_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_invalidate(self, client: Kater) -> None:
        response = client.v1.compiler.cache.with_raw_response.invalidate(
            client_id="client_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_invalidate(self, client: Kater) -> None:
        with client.v1.compiler.cache.with_streaming_response.invalidate(
            client_id="client_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCache:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invalidate(self, async_client: AsyncKater) -> None:
        cache = await async_client.v1.compiler.cache.invalidate(
            client_id="client_id",
        )
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invalidate_with_all_params(self, async_client: AsyncKater) -> None:
        cache = await async_client.v1.compiler.cache.invalidate(
            client_id="client_id",
            connection_id="connection_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_invalidate(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.cache.with_raw_response.invalidate(
            client_id="client_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_invalidate(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.cache.with_streaming_response.invalidate(
            client_id="client_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True
