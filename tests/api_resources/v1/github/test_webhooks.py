# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.github import WebhookReceiveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_receive(self, client: Kater) -> None:
        webhook = client.v1.github.webhooks.receive(
            x_github_delivery="X-GitHub-Delivery",
            x_github_event="X-GitHub-Event",
            x_hub_signature_256="X-Hub-Signature-256",
        )
        assert_matches_type(WebhookReceiveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_receive(self, client: Kater) -> None:
        response = client.v1.github.webhooks.with_raw_response.receive(
            x_github_delivery="X-GitHub-Delivery",
            x_github_event="X-GitHub-Event",
            x_hub_signature_256="X-Hub-Signature-256",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookReceiveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_receive(self, client: Kater) -> None:
        with client.v1.github.webhooks.with_streaming_response.receive(
            x_github_delivery="X-GitHub-Delivery",
            x_github_event="X-GitHub-Event",
            x_hub_signature_256="X-Hub-Signature-256",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookReceiveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_receive(self, async_client: AsyncKater) -> None:
        webhook = await async_client.v1.github.webhooks.receive(
            x_github_delivery="X-GitHub-Delivery",
            x_github_event="X-GitHub-Event",
            x_hub_signature_256="X-Hub-Signature-256",
        )
        assert_matches_type(WebhookReceiveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_receive(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.github.webhooks.with_raw_response.receive(
            x_github_delivery="X-GitHub-Delivery",
            x_github_event="X-GitHub-Event",
            x_hub_signature_256="X-Hub-Signature-256",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookReceiveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_receive(self, async_client: AsyncKater) -> None:
        async with async_client.v1.github.webhooks.with_streaming_response.receive(
            x_github_delivery="X-GitHub-Delivery",
            x_github_event="X-GitHub-Event",
            x_hub_signature_256="X-Hub-Signature-256",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookReceiveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
