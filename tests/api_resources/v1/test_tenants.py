# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1 import (
    ImportTenantsResponse,
    TenantGetTenantsSchemaResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tenants_schema(self, client: Kater) -> None:
        tenant = client.v1.tenants.get_tenants_schema()
        assert_matches_type(TenantGetTenantsSchemaResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_tenants_schema(self, client: Kater) -> None:
        response = client.v1.tenants.with_raw_response.get_tenants_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantGetTenantsSchemaResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_tenants_schema(self, client: Kater) -> None:
        with client.v1.tenants.with_streaming_response.get_tenants_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantGetTenantsSchemaResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_csv(self, client: Kater) -> None:
        tenant = client.v1.tenants.import_from_csv(
            file=b"raw file contents",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_csv_with_all_params(self, client: Kater) -> None:
        tenant = client.v1.tenants.import_from_csv(
            file=b"raw file contents",
            source="source",
            attribute_columns="attribute_columns",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import_from_csv(self, client: Kater) -> None:
        response = client.v1.tenants.with_raw_response.import_from_csv(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import_from_csv(self, client: Kater) -> None:
        with client.v1.tenants.with_streaming_response.import_from_csv(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_warehouse(self, client: Kater) -> None:
        tenant = client.v1.tenants.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_from_warehouse_with_all_params(self, client: Kater) -> None:
        tenant = client.v1.tenants.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
            source="source",
            attribute_columns={"foo": "string"},
            tenant_group_column="tenant_group_column",
            tenant_name_column="tenant_name_column",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import_from_warehouse(self, client: Kater) -> None:
        response = client.v1.tenants.with_raw_response.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import_from_warehouse(self, client: Kater) -> None:
        with client.v1.tenants.with_streaming_response.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTenants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tenants_schema(self, async_client: AsyncKater) -> None:
        tenant = await async_client.v1.tenants.get_tenants_schema()
        assert_matches_type(TenantGetTenantsSchemaResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_tenants_schema(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.tenants.with_raw_response.get_tenants_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantGetTenantsSchemaResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_tenants_schema(self, async_client: AsyncKater) -> None:
        async with async_client.v1.tenants.with_streaming_response.get_tenants_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantGetTenantsSchemaResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_csv(self, async_client: AsyncKater) -> None:
        tenant = await async_client.v1.tenants.import_from_csv(
            file=b"raw file contents",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_csv_with_all_params(self, async_client: AsyncKater) -> None:
        tenant = await async_client.v1.tenants.import_from_csv(
            file=b"raw file contents",
            source="source",
            attribute_columns="attribute_columns",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import_from_csv(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.tenants.with_raw_response.import_from_csv(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import_from_csv(self, async_client: AsyncKater) -> None:
        async with async_client.v1.tenants.with_streaming_response.import_from_csv(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_warehouse(self, async_client: AsyncKater) -> None:
        tenant = await async_client.v1.tenants.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_from_warehouse_with_all_params(self, async_client: AsyncKater) -> None:
        tenant = await async_client.v1.tenants.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
            source="source",
            attribute_columns={"foo": "string"},
            tenant_group_column="tenant_group_column",
            tenant_name_column="tenant_name_column",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import_from_warehouse(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.tenants.with_raw_response.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import_from_warehouse(self, async_client: AsyncKater) -> None:
        async with async_client.v1.tenants.with_streaming_response.import_from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(ImportTenantsResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True
