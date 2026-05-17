# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1.connections.sdk import (
    WidgetRenderResponse,
    WidgetRegenerateMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWidget:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_regenerate_metadata(self, client: Kater) -> None:
        widget = client.v1.connections.sdk.widget.regenerate_metadata(
            persist={"mode": "mode"},
            post_query_state={},
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
        )
        assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_regenerate_metadata_with_all_params(self, client: Kater) -> None:
        widget = client.v1.connections.sdk.widget.regenerate_metadata(
            persist={
                "mode": "mode",
                "scope": {
                    "chat_thread_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "widget_instance_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "scope_type": "scope_type",
            },
            post_query_state={
                "filters": [
                    {
                        "expression": "equals",
                        "field": {
                            "ref": "ref(dim_customer.sale_price)",
                            "modifiers": [
                                {
                                    "kind": "timeframe",
                                    "value": "x",
                                }
                            ],
                        },
                        "kind": "date",
                        "default_enabled": True,
                        "default_value": "string",
                        "values": {
                            "source": "result_distinct",
                            "limit": 1,
                            "searchable": True,
                            "sort": "asc",
                        },
                    }
                ],
                "sorts": [
                    {
                        "field": {
                            "ref": "ref(dim_customer.sale_price)",
                            "modifiers": [
                                {
                                    "kind": "timeframe",
                                    "value": "x",
                                }
                            ],
                        },
                        "default_direction": "asc",
                        "default_enabled": True,
                        "priority": 1,
                    }
                ],
            },
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
            source="source",
            post_query_state_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision=0,
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_regenerate_metadata(self, client: Kater) -> None:
        response = client.v1.connections.sdk.widget.with_raw_response.regenerate_metadata(
            persist={"mode": "mode"},
            post_query_state={},
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_regenerate_metadata(self, client: Kater) -> None:
        with client.v1.connections.sdk.widget.with_streaming_response.regenerate_metadata(
            persist={"mode": "mode"},
            post_query_state={},
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_render(self, client: Kater) -> None:
        widget = client.v1.connections.sdk.widget.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ]
            },
            filter_state=[{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            pinned_variant="pinned_variant",
            presentation={},
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
        )
        assert_matches_type(WidgetRenderResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_render_with_all_params(self, client: Kater) -> None:
        widget = client.v1.connections.sdk.widget.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [
                    {
                        "effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "enabled": True,
                        "value": {
                            "value": "string",
                            "mode": "scalar",
                        },
                    }
                ],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ],
                "selected_field_ids": ["string"],
                "timeframe_overrides": [
                    {
                        "active_timeframe": "active_timeframe",
                        "source_kater_id": "source_kater_id",
                    }
                ],
            },
            filter_state=[
                {
                    "effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enabled": True,
                    "value": {
                        "value": "string",
                        "mode": "scalar",
                    },
                }
            ],
            pinned_variant="pinned_variant",
            presentation={
                "chart": {"foo": "string"},
                "display": {"foo": "string"},
                "style": {"foo": "string"},
            },
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
            source="source",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(WidgetRenderResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_render(self, client: Kater) -> None:
        response = client.v1.connections.sdk.widget.with_raw_response.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ]
            },
            filter_state=[{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            pinned_variant="pinned_variant",
            presentation={},
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(WidgetRenderResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_render(self, client: Kater) -> None:
        with client.v1.connections.sdk.widget.with_streaming_response.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ]
            },
            filter_state=[{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            pinned_variant="pinned_variant",
            presentation={},
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(WidgetRenderResponse, widget, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWidget:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_regenerate_metadata(self, async_client: AsyncKater) -> None:
        widget = await async_client.v1.connections.sdk.widget.regenerate_metadata(
            persist={"mode": "mode"},
            post_query_state={},
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
        )
        assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_regenerate_metadata_with_all_params(self, async_client: AsyncKater) -> None:
        widget = await async_client.v1.connections.sdk.widget.regenerate_metadata(
            persist={
                "mode": "mode",
                "scope": {
                    "chat_thread_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "widget_instance_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "scope_type": "scope_type",
            },
            post_query_state={
                "filters": [
                    {
                        "expression": "equals",
                        "field": {
                            "ref": "ref(dim_customer.sale_price)",
                            "modifiers": [
                                {
                                    "kind": "timeframe",
                                    "value": "x",
                                }
                            ],
                        },
                        "kind": "date",
                        "default_enabled": True,
                        "default_value": "string",
                        "values": {
                            "source": "result_distinct",
                            "limit": 1,
                            "searchable": True,
                            "sort": "asc",
                        },
                    }
                ],
                "sorts": [
                    {
                        "field": {
                            "ref": "ref(dim_customer.sale_price)",
                            "modifiers": [
                                {
                                    "kind": "timeframe",
                                    "value": "x",
                                }
                            ],
                        },
                        "default_direction": "asc",
                        "default_enabled": True,
                        "priority": 1,
                    }
                ],
            },
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
            source="source",
            post_query_state_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision=0,
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_regenerate_metadata(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.sdk.widget.with_raw_response.regenerate_metadata(
            persist={"mode": "mode"},
            post_query_state={},
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_regenerate_metadata(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.sdk.widget.with_streaming_response.regenerate_metadata(
            persist={"mode": "mode"},
            post_query_state={},
            query_kater_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rendered_query_key_id="rendered_query_key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(WidgetRegenerateMetadataResponse, widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_render(self, async_client: AsyncKater) -> None:
        widget = await async_client.v1.connections.sdk.widget.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ]
            },
            filter_state=[{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            pinned_variant="pinned_variant",
            presentation={},
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
        )
        assert_matches_type(WidgetRenderResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_render_with_all_params(self, async_client: AsyncKater) -> None:
        widget = await async_client.v1.connections.sdk.widget.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [
                    {
                        "effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "enabled": True,
                        "value": {
                            "value": "string",
                            "mode": "scalar",
                        },
                    }
                ],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ],
                "selected_field_ids": ["string"],
                "timeframe_overrides": [
                    {
                        "active_timeframe": "active_timeframe",
                        "source_kater_id": "source_kater_id",
                    }
                ],
            },
            filter_state=[
                {
                    "effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enabled": True,
                    "value": {
                        "value": "string",
                        "mode": "scalar",
                    },
                }
            ],
            pinned_variant="pinned_variant",
            presentation={
                "chart": {"foo": "string"},
                "display": {"foo": "string"},
                "style": {"foo": "string"},
            },
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
            source="source",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(WidgetRenderResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_render(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.connections.sdk.widget.with_raw_response.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ]
            },
            filter_state=[{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            pinned_variant="pinned_variant",
            presentation={},
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(WidgetRenderResponse, widget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_render(self, async_client: AsyncKater) -> None:
        async with async_client.v1.connections.sdk.widget.with_streaming_response.render(
            connection_id="connection_id",
            dashboard={
                "dashboard_filter_state": [{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "dashboard_kater_id": "dashboard_kater_id",
                "slot_name": "slot_name",
                "widget_kater_id": "widget_kater_id",
            },
            field_selection={
                "selected_fields": [
                    {
                        "modifiers": [
                            {
                                "kind": "timeframe",
                                "value": "x",
                            }
                        ],
                        "source_kater_id": "x",
                    }
                ]
            },
            filter_state=[{"effective_kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            pinned_variant="pinned_variant",
            presentation={},
            query_kater_id="query_kater_id",
            result_window={
                "cursor": "cursor",
                "page_size": 0,
                "sort_by": "sort_by",
                "sort_order": "asc",
            },
            temporal={
                "as_of": "as_of",
                "timezone": "timezone",
            },
            variables=[
                {
                    "name": "name",
                    "query_kater_id": "query_kater_id",
                    "scope": "query",
                    "value": "string",
                    "variable_kater_id": "variable_kater_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(WidgetRenderResponse, widget, path=["response"])

        assert cast(Any, response.is_closed) is True
