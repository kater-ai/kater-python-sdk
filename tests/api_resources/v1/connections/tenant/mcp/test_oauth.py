# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.connections.tenant.mcp import OAuthInitiateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate(self, client: Kater) -> None:
        oauth = client.v1.connections.tenant.mcp.oauth.initiate(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OAuthInitiateResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate(self, client: Kater) -> None:
        response = client.v1.connections.tenant.mcp.oauth.with_raw_response.initiate(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthInitiateResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate(self, client: Kater) -> None:
        with client.v1.connections.tenant.mcp.oauth.with_streaming_response.initiate(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthInitiateResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_initiate(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            client.v1.connections.tenant.mcp.oauth.with_raw_response.initiate(
                mcp_id="",
                tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate(self, async_client: AsyncKater) -> None:
        oauth = await async_client.v1.connections.tenant.mcp.oauth.initiate(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OAuthInitiateResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.tenant.mcp.oauth.with_raw_response.initiate(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthInitiateResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.tenant.mcp.oauth.with_streaming_response.initiate(
            mcp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthInitiateResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_initiate(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_id` but received ''"):
            await async_client.v1.connections.tenant.mcp.oauth.with_raw_response.initiate(
                mcp_id="",
                tenant_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                tenant_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
