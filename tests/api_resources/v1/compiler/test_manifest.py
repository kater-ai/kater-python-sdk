# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.compiler import ManifestRegenerateAndCreatePrResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManifest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_regenerate_and_create_pr(self, client: Kater) -> None:
        manifest = client.v1.compiler.manifest.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_regenerate_and_create_pr_with_all_params(self, client: Kater) -> None:
        manifest = client.v1.compiler.manifest.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            include_dependency_graph=True,
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_regenerate_and_create_pr(self, client: Kater) -> None:
        response = client.v1.compiler.manifest.with_raw_response.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifest = response.parse()
        assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_regenerate_and_create_pr(self, client: Kater) -> None:
        with client.v1.compiler.manifest.with_streaming_response.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifest = response.parse()
            assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncManifest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_regenerate_and_create_pr(self, async_client: AsyncKater) -> None:
        manifest = await async_client.v1.compiler.manifest.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_regenerate_and_create_pr_with_all_params(self, async_client: AsyncKater) -> None:
        manifest = await async_client.v1.compiler.manifest.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            include_dependency_graph=True,
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_regenerate_and_create_pr(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.manifest.with_raw_response.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifest = await response.parse()
        assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_regenerate_and_create_pr(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.manifest.with_streaming_response.regenerate_and_create_pr(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifest = await response.parse()
            assert_matches_type(ManifestRegenerateAndCreatePrResponse, manifest, path=["response"])

        assert cast(Any, response.is_closed) is True
