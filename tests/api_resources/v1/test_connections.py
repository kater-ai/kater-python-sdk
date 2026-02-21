# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1 import ConnectionListConnectionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_connections(self, client: Kater) -> None:
        connection = client.v1.connections.list_connections()
        assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_connections_with_all_params(self, client: Kater) -> None:
        connection = client.v1.connections.list_connections(
            status="approved",
        )
        assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_connections(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.list_connections()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_connections(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.list_connections() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_connections(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.list_connections()
        assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_connections_with_all_params(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.list_connections(
            status="approved",
        )
        assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_connections(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.list_connections()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_connections(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.list_connections() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListConnectionsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True
