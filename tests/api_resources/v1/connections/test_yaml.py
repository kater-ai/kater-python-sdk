# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.connections import YamlCommitYamlResponse, YamlRetrieveYamlResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestYaml:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_commit_yaml(self, client: Kater) -> None:
        yaml = client.v1.connections.yaml.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
        )
        assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_commit_yaml_with_all_params(self, client: Kater) -> None:
        yaml = client.v1.connections.yaml.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
            auto_merge=True,
        )
        assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_commit_yaml(self, client: Kater) -> None:
        response = client.v1.connections.yaml.with_raw_response.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        yaml = response.parse()
        assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_commit_yaml(self, client: Kater) -> None:
        with client.v1.connections.yaml.with_streaming_response.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            yaml = response.parse()
            assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_commit_yaml(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.yaml.with_raw_response.commit_yaml(
                connection_id="",
                yaml_content="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_yaml(self, client: Kater) -> None:
        yaml = client.v1.connections.yaml.retrieve_yaml(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(YamlRetrieveYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_yaml(self, client: Kater) -> None:
        response = client.v1.connections.yaml.with_raw_response.retrieve_yaml(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        yaml = response.parse()
        assert_matches_type(YamlRetrieveYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_yaml(self, client: Kater) -> None:
        with client.v1.connections.yaml.with_streaming_response.retrieve_yaml(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            yaml = response.parse()
            assert_matches_type(YamlRetrieveYamlResponse, yaml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_yaml(self, client: Kater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.yaml.with_raw_response.retrieve_yaml(
                "",
            )


class TestAsyncYaml:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_commit_yaml(self, async_client: AsyncKater) -> None:
        yaml = await async_client.v1.connections.yaml.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
        )
        assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_commit_yaml_with_all_params(self, async_client: AsyncKater) -> None:
        yaml = await async_client.v1.connections.yaml.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
            auto_merge=True,
        )
        assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_commit_yaml(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.yaml.with_raw_response.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        yaml = await response.parse()
        assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_commit_yaml(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.yaml.with_streaming_response.commit_yaml(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            yaml_content="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            yaml = await response.parse()
            assert_matches_type(YamlCommitYamlResponse, yaml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_commit_yaml(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.yaml.with_raw_response.commit_yaml(
                connection_id="",
                yaml_content="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_yaml(self, async_client: AsyncKater) -> None:
        yaml = await async_client.v1.connections.yaml.retrieve_yaml(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(YamlRetrieveYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_yaml(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.yaml.with_raw_response.retrieve_yaml(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        yaml = await response.parse()
        assert_matches_type(YamlRetrieveYamlResponse, yaml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_yaml(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.yaml.with_streaming_response.retrieve_yaml(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            yaml = await response.parse()
            assert_matches_type(YamlRetrieveYamlResponse, yaml, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_yaml(self, async_client: AsyncKater) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.yaml.with_raw_response.retrieve_yaml(
                "",
            )
