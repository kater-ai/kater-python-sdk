# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1 import (
    Connection,
    ConnectionListResponse,
    ConnectionSyncResponse,
    ConnectionRetrieveCredentialResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
            description="description",
            label="label",
            port=1,
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[{"name": "x"}],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
            description="description",
            label="label",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[{"name": "x"}],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[{"name": "x"}],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            access_token="access_token",
            databases=[{"name": "x"}],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            access_token="access_token",
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
            description="description",
            label="label",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.create(
            access_token="access_token",
            databases=[{"name": "x"}],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.create(
            access_token="access_token",
            databases=[{"name": "x"}],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
            description="description",
            label="label",
            port=1,
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Kater) -> None:
        connection = client.v1.connections.create(
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
            description="description",
            label="label",
            port=1,
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kater) -> None:
        connection = client.v1.connections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Kater) -> None:
        connection = client.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_credential(self, client: Kater) -> None:
        connection = client.v1.connections.retrieve_credential(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectionRetrieveCredentialResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_credential(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.retrieve_credential(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionRetrieveCredentialResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_credential(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.retrieve_credential(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionRetrieveCredentialResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_credential(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.retrieve_credential(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_sync(self, client: Kater) -> None:
        connection = client.v1.connections.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectionSyncResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: Kater) -> None:
        response = client.v1.connections.with_raw_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionSyncResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: Kater) -> None:
        with client.v1.connections.with_streaming_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionSyncResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_sync(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.sync(
                "",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
            description="description",
            label="label",
            port=1,
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="postgresql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[{"name": "x"}],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
            description="description",
            label="label",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[{"name": "x"}],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.create(
            account="account",
            auth={
                "auth_type": "password",
                "password": "password",
            },
            databases=[{"name": "x"}],
            name="x",
            role="role",
            username="username",
            warehouse="warehouse",
            warehouse_type="snowflake",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            access_token="access_token",
            databases=[{"name": "x"}],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            access_token="access_token",
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
            description="description",
            label="label",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.create(
            access_token="access_token",
            databases=[{"name": "x"}],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.create(
            access_token="access_token",
            databases=[{"name": "x"}],
            http_path="http_path",
            name="x",
            server_hostname="server_hostname",
            warehouse_type="databricks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
            description="description",
            label="label",
            port=1,
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="clickhouse",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.create(
            databases=[
                {
                    "name": "x",
                    "description": "description",
                    "label": "label",
                    "schemas": [
                        {
                            "name": "x",
                            "description": "description",
                            "label": "label",
                        }
                    ],
                    "timezone": "UTC",
                }
            ],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
            description="description",
            label="label",
            port=1,
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.create(
            databases=[{"name": "x"}],
            host="host",
            name="x",
            password="password",
            username="username",
            warehouse_type="mssql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_credential(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.retrieve_credential(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectionRetrieveCredentialResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_credential(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.retrieve_credential(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionRetrieveCredentialResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_credential(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.retrieve_credential(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionRetrieveCredentialResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_credential(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.retrieve_credential(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncKater) -> None:
        connection = await async_client.v1.connections.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectionSyncResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.with_raw_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionSyncResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.with_streaming_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionSyncResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_sync(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.sync(
                "",
            )
