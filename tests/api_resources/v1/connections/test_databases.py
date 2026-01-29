# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.connections import (
    DatabaseUpdateResponse,
    DatabaseUpdateSchemaResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Kater) -> None:
        database = client.v1.connections.databases.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kater) -> None:
        database = client.v1.connections.databases.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auto_merge=True,
            description="description",
            label="label",
            name="name",
        )
        assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kater) -> None:
        response = client.v1.connections.databases.with_raw_response.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kater) -> None:
        with client.v1.connections.databases.with_streaming_response.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.databases.with_raw_response.update(
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.v1.connections.databases.with_raw_response.update(
                database_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_schema(self, client: Kater) -> None:
        database = client.v1.connections.databases.delete_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert database is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_schema(self, client: Kater) -> None:
        response = client.v1.connections.databases.with_raw_response.delete_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert database is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_schema(self, client: Kater) -> None:
        with client.v1.connections.databases.with_streaming_response.delete_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_schema(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.databases.with_raw_response.delete_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.v1.connections.databases.with_raw_response.delete_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.v1.connections.databases.with_raw_response.delete_schema(
                schema_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_schema(self, client: Kater) -> None:
        database = client.v1.connections.databases.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_schema_with_all_params(self, client: Kater) -> None:
        database = client.v1.connections.databases.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auto_merge=True,
            description="description",
            label="label",
            name="name",
        )
        assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_schema(self, client: Kater) -> None:
        response = client.v1.connections.databases.with_raw_response.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_schema(self, client: Kater) -> None:
        with client.v1.connections.databases.with_streaming_response.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_schema(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.databases.with_raw_response.update_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.v1.connections.databases.with_raw_response.update_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.v1.connections.databases.with_raw_response.update_schema(
                schema_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncDatabases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKater) -> None:
        database = await async_client.v1.connections.databases.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKater) -> None:
        database = await async_client.v1.connections.databases.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auto_merge=True,
            description="description",
            label="label",
            name="name",
        )
        assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.databases.with_raw_response.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.databases.with_streaming_response.update(
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseUpdateResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.update(
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.update(
                database_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_schema(self, async_client: AsyncKater) -> None:
        database = await async_client.v1.connections.databases.delete_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert database is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_schema(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.databases.with_raw_response.delete_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert database is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_schema(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.databases.with_streaming_response.delete_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_schema(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.delete_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.delete_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.delete_schema(
                schema_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_schema(self, async_client: AsyncKater) -> None:
        database = await async_client.v1.connections.databases.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_schema_with_all_params(self, async_client: AsyncKater) -> None:
        database = await async_client.v1.connections.databases.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auto_merge=True,
            description="description",
            label="label",
            name="name",
        )
        assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_schema(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.databases.with_raw_response.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_schema(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.databases.with_streaming_response.update_schema(
            schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseUpdateSchemaResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_schema(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.update_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.update_schema(
                schema_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.v1.connections.databases.with_raw_response.update_schema(
                schema_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                database_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
