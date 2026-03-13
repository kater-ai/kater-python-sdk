# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.connections.client.mcp import (
    ServerListResponse,
    ServerCreateResponse,
    ServerUpdateResponse,
    ServerDiscoverResponse,
    ServerRediscoverResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.create(
            name="x",
            server_url="server_url",
            slug="x",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.create(
            name="x",
            server_url="server_url",
            slug="x",
            auth_type="api_key",
            description="description",
            oauth_authorize_url="oauth_authorize_url",
            oauth_client_id="oauth_client_id",
            oauth_client_secret="oauth_client_secret",
            oauth_revoke_url="oauth_revoke_url",
            oauth_scopes_requested="oauth_scopes_requested",
            oauth_token_url="oauth_token_url",
            terms_acknowledged=True,
            transport="auto",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kater) -> None:
        response = client.v1.connections.client.mcp.servers.with_raw_response.create(
            name="x",
            server_url="server_url",
            slug="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kater) -> None:
        with client.v1.connections.client.mcp.servers.with_streaming_response.create(
            name="x",
            server_url="server_url",
            slug="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerCreateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
            enabled=True,
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kater) -> None:
        response = client.v1.connections.client.mcp.servers.with_raw_response.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kater) -> None:
        with client.v1.connections.client.mcp.servers.with_streaming_response.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            client.v1.connections.client.mcp.servers.with_raw_response.update(
                mcp_id="",
                allowed_capabilities=[
                    {
                        "description": "description",
                        "input_schema": {"foo": "bar"},
                        "is_write": True,
                        "name": "name",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.list()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kater) -> None:
        response = client.v1.connections.client.mcp.servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kater) -> None:
        with client.v1.connections.client.mcp.servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerListResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kater) -> None:
        response = client.v1.connections.client.mcp.servers.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kater) -> None:
        with client.v1.connections.client.mcp.servers.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            client.v1.connections.client.mcp.servers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_discover(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServerDiscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_discover_with_all_params(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_api_key="test_api_key",
            test_bearer_token="test_bearer_token",
        )
        assert_matches_type(ServerDiscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_discover(self, client: Kater) -> None:
        response = client.v1.connections.client.mcp.servers.with_raw_response.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerDiscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_discover(self, client: Kater) -> None:
        with client.v1.connections.client.mcp.servers.with_streaming_response.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerDiscoverResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_discover(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            client.v1.connections.client.mcp.servers.with_raw_response.discover(
                mcp_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rediscover(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServerRediscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rediscover_with_all_params(self, client: Kater) -> None:
        server = client.v1.connections.client.mcp.servers.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_api_key="test_api_key",
            test_bearer_token="test_bearer_token",
        )
        assert_matches_type(ServerRediscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rediscover(self, client: Kater) -> None:
        response = client.v1.connections.client.mcp.servers.with_raw_response.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerRediscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rediscover(self, client: Kater) -> None:
        with client.v1.connections.client.mcp.servers.with_streaming_response.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerRediscoverResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rediscover(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            client.v1.connections.client.mcp.servers.with_raw_response.rediscover(
                mcp_id="",
            )


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.create(
            name="x",
            server_url="server_url",
            slug="x",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.create(
            name="x",
            server_url="server_url",
            slug="x",
            auth_type="api_key",
            description="description",
            oauth_authorize_url="oauth_authorize_url",
            oauth_client_id="oauth_client_id",
            oauth_client_secret="oauth_client_secret",
            oauth_revoke_url="oauth_revoke_url",
            oauth_scopes_requested="oauth_scopes_requested",
            oauth_token_url="oauth_token_url",
            terms_acknowledged=True,
            transport="auto",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.client.mcp.servers.with_raw_response.create(
            name="x",
            server_url="server_url",
            slug="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.client.mcp.servers.with_streaming_response.create(
            name="x",
            server_url="server_url",
            slug="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerCreateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
            enabled=True,
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.client.mcp.servers.with_raw_response.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.client.mcp.servers.with_streaming_response.update(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_capabilities=[
                {
                    "description": "description",
                    "input_schema": {"foo": "bar"},
                    "is_write": True,
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            await async_client.v1.connections.client.mcp.servers.with_raw_response.update(
                mcp_id="",
                allowed_capabilities=[
                    {
                        "description": "description",
                        "input_schema": {"foo": "bar"},
                        "is_write": True,
                        "name": "name",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.list()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.client.mcp.servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerListResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.client.mcp.servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerListResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.client.mcp.servers.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.client.mcp.servers.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            await async_client.v1.connections.client.mcp.servers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_discover(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServerDiscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_discover_with_all_params(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_api_key="test_api_key",
            test_bearer_token="test_bearer_token",
        )
        assert_matches_type(ServerDiscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.client.mcp.servers.with_raw_response.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerDiscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.client.mcp.servers.with_streaming_response.discover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerDiscoverResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_discover(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            await async_client.v1.connections.client.mcp.servers.with_raw_response.discover(
                mcp_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rediscover(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ServerRediscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rediscover_with_all_params(self, async_client: AsyncKater) -> None:
        server = await async_client.v1.connections.client.mcp.servers.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_api_key="test_api_key",
            test_bearer_token="test_bearer_token",
        )
        assert_matches_type(ServerRediscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rediscover(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.client.mcp.servers.with_raw_response.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerRediscoverResponse, server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rediscover(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.client.mcp.servers.with_streaming_response.rediscover(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerRediscoverResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rediscover(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            await async_client.v1.connections.client.mcp.servers.with_raw_response.rediscover(
                mcp_id="",
            )
