# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.groups import TenantAddResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Kater) -> None:
        tenant = client.v1.groups.tenants.add(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(TenantAddResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Kater) -> None:
        response = client.v1.groups.tenants.with_raw_response.add(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantAddResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Kater) -> None:
        with client.v1.groups.tenants.with_streaming_response.add(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantAddResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.v1.groups.tenants.with_raw_response.add(
                group_id="",
                tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Kater) -> None:
        tenant = client.v1.groups.tenants.remove(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Kater) -> None:
        response = client.v1.groups.tenants.with_raw_response.remove(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Kater) -> None:
        with client.v1.groups.tenants.with_streaming_response.remove(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.v1.groups.tenants.with_raw_response.remove(
                tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.v1.groups.tenants.with_raw_response.remove(
                tenant_id="",
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncTenants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncKater) -> None:
        tenant = await async_client.v1.groups.tenants.add(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(TenantAddResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.groups.tenants.with_raw_response.add(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantAddResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncKater) -> None:
        async with async_client.v1.groups.tenants.with_streaming_response.add(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantAddResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.v1.groups.tenants.with_raw_response.add(
                group_id="",
                tenant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncKater) -> None:
        tenant = await async_client.v1.groups.tenants.remove(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.groups.tenants.with_raw_response.remove(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncKater) -> None:
        async with async_client.v1.groups.tenants.with_streaming_response.remove(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.v1.groups.tenants.with_raw_response.remove(
                tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.v1.groups.tenants.with_raw_response.remove(
                tenant_id="",
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
