# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.connections import ViewListResponse, ViewRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kater) -> None:
        view = client.v1.connections.views.retrieve(
            file_name="file_name",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kater) -> None:
        response = client.v1.connections.views.with_raw_response.retrieve(
            file_name="file_name",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kater) -> None:
        with client.v1.connections.views.with_streaming_response.retrieve(
            file_name="file_name",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewRetrieveResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.views.with_raw_response.retrieve(
                file_name="file_name",
                connection_id="",
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.v1.connections.views.with_raw_response.retrieve(
                file_name="file_name",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                sync_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_name` but received ''"):
            client.v1.connections.views.with_raw_response.retrieve(
                file_name="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Kater) -> None:
        view = client.v1.connections.views.list(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kater) -> None:
        response = client.v1.connections.views.with_raw_response.list(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kater) -> None:
        with client.v1.connections.views.with_streaming_response.list(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewListResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.views.with_raw_response.list(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.v1.connections.views.with_raw_response.list(
                sync_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncViews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKater) -> None:
        view = await async_client.v1.connections.views.retrieve(
            file_name="file_name",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.views.with_raw_response.retrieve(
            file_name="file_name",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.views.with_streaming_response.retrieve(
            file_name="file_name",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewRetrieveResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.views.with_raw_response.retrieve(
                file_name="file_name",
                connection_id="",
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.v1.connections.views.with_raw_response.retrieve(
                file_name="file_name",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                sync_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_name` but received ''"):
            await async_client.v1.connections.views.with_raw_response.retrieve(
                file_name="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKater) -> None:
        view = await async_client.v1.connections.views.list(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.views.with_raw_response.list(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.views.with_streaming_response.list(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewListResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.views.with_raw_response.list(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                connection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.v1.connections.views.with_raw_response.list(
                sync_id="",
                connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
