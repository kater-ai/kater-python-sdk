# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.compiler import (
    CapabilityCreateResponse,
    CapabilitySampleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCapabilities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kater) -> None:
        capability = client.v1.compiler.capabilities.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kater) -> None:
        capability = client.v1.compiler.capabilities.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            query_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kater) -> None:
        response = client.v1.compiler.capabilities.with_raw_response.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kater) -> None:
        with client.v1.compiler.capabilities.with_streaming_response.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sample(self, client: Kater) -> None:
        capability = client.v1.compiler.capabilities.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sample_with_all_params(self, client: Kater) -> None:
        capability = client.v1.compiler.capabilities.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            include_filter_variants=True,
            include_pinned_variants=True,
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sample(self, client: Kater) -> None:
        response = client.v1.compiler.capabilities.with_raw_response.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sample(self, client: Kater) -> None:
        with client.v1.compiler.capabilities.with_streaming_response.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCapabilities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKater) -> None:
        capability = await async_client.v1.compiler.capabilities.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKater) -> None:
        capability = await async_client.v1.compiler.capabilities.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            query_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.capabilities.with_raw_response.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.capabilities.with_streaming_response.create(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(CapabilityCreateResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sample(self, async_client: AsyncKater) -> None:
        capability = await async_client.v1.compiler.capabilities.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sample_with_all_params(self, async_client: AsyncKater) -> None:
        capability = await async_client.v1.compiler.capabilities.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            include_filter_variants=True,
            include_pinned_variants=True,
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sample(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.capabilities.with_raw_response.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sample(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.capabilities.with_streaming_response.sample(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n=1,
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(CapabilitySampleResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True
