# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.connections.tenant import (
    McpListResponse,
    McpGetAuditHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kater) -> None:
        mcp = client.v1.connections.tenant.mcp.list(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kater) -> None:
        response = client.v1.connections.tenant.mcp.with_raw_response.list(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kater) -> None:
        with client.v1.connections.tenant.mcp.with_streaming_response.list(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_audit_history(self, client: Kater) -> None:
        mcp = client.v1.connections.tenant.mcp.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_audit_history_with_all_params(self, client: Kater) -> None:
        mcp = client.v1.connections.tenant.mcp.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_audit_history(self, client: Kater) -> None:
        response = client.v1.connections.tenant.mcp.with_raw_response.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_audit_history(self, client: Kater) -> None:
        with client.v1.connections.tenant.mcp.with_streaming_response.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_audit_history(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            client.v1.connections.tenant.mcp.with_raw_response.get_audit_history(
                mcp_id="",
                tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKater) -> None:
        mcp = await async_client.v1.connections.tenant.mcp.list(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.tenant.mcp.with_raw_response.list(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.tenant.mcp.with_streaming_response.list(
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_audit_history(self, async_client: AsyncKater) -> None:
        mcp = await async_client.v1.connections.tenant.mcp.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_audit_history_with_all_params(self, async_client: AsyncKater) -> None:
        mcp = await async_client.v1.connections.tenant.mcp.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_audit_history(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.tenant.mcp.with_raw_response.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_audit_history(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.tenant.mcp.with_streaming_response.get_audit_history(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpGetAuditHistoryResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_audit_history(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            await async_client.v1.connections.tenant.mcp.with_raw_response.get_audit_history(
                mcp_id="",
                tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
