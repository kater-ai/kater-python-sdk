# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.tenants import ImportTenants

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_from_csv(self, client: Kater) -> None:
        import_ = client.v1.tenants.import_.from_csv(
            file=b"raw file contents",
        )
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_from_csv(self, client: Kater) -> None:
        response = client.v1.tenants.import_.with_raw_response.from_csv(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_from_csv(self, client: Kater) -> None:
        with client.v1.tenants.import_.with_streaming_response.from_csv(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(ImportTenants, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_from_warehouse(self, client: Kater) -> None:
        import_ = client.v1.tenants.import_.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_from_warehouse_with_all_params(self, client: Kater) -> None:
        import_ = client.v1.tenants.import_.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
            tenant_group_column="tenant_group_column",
            tenant_name_column="tenant_name_column",
        )
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_from_warehouse(self, client: Kater) -> None:
        response = client.v1.tenants.import_.with_raw_response.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_from_warehouse(self, client: Kater) -> None:
        with client.v1.tenants.import_.with_streaming_response.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(ImportTenants, import_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_from_csv(self, async_client: AsyncKater) -> None:
        import_ = await async_client.v1.tenants.import_.from_csv(
            file=b"raw file contents",
        )
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_from_csv(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.tenants.import_.with_raw_response.from_csv(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_from_csv(self, async_client: AsyncKater) -> None:
        async with async_client.v1.tenants.import_.with_streaming_response.from_csv(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(ImportTenants, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_from_warehouse(self, async_client: AsyncKater) -> None:
        import_ = await async_client.v1.tenants.import_.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_from_warehouse_with_all_params(self, async_client: AsyncKater) -> None:
        import_ = await async_client.v1.tenants.import_.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
            tenant_group_column="tenant_group_column",
            tenant_name_column="tenant_name_column",
        )
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_from_warehouse(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.tenants.import_.with_raw_response.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(ImportTenants, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_from_warehouse(self, async_client: AsyncKater) -> None:
        async with async_client.v1.tenants.import_.with_streaming_response.from_warehouse(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            database="x",
            schema="x",
            table="x",
            tenant_key_column="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(ImportTenants, import_, path=["response"])

        assert cast(Any, response.is_closed) is True
