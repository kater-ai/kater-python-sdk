# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1 import (
    CompilerRenderResponse,
    CompilerCompileResponse,
    CompilerExecuteResponse,
    CompilerResolveResponse,
    CompilerValidateResponse,
    CompilerCompileDashboardResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompiler:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compile(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile(
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
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compile_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile(
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
                ]
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
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_compile(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.compile(
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
        compiler = response.parse()
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_compile(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.compile(
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

            compiler = response.parse()
            assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compile_dashboard(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compile_dashboard_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
            source="source",
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
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_compile_dashboard(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_compile_dashboard(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute(self, client: Kater) -> None:
        compiler = client.v1.compiler.execute(
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
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.execute(
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
                ]
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
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.execute(
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
        compiler = response.parse()
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.execute(
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

            compiler = response.parse()
            assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_render(self, client: Kater) -> None:
        compiler = client.v1.compiler.render(
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
        assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_render_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.render(
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
                ]
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
        assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_render(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.render(
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
        compiler = response.parse()
        assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_render(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.render(
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

            compiler = response.parse()
            assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve(self, client: Kater) -> None:
        compiler = client.v1.compiler.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
            source="source",
            auto_fix=True,
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
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resolve(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resolve(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: Kater) -> None:
        compiler = client.v1.compiler.validate()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.validate(
            source="source",
            auto_fix=True,
            connection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompiler:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compile(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile(
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
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compile_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile(
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
                ]
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
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_compile(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.compile(
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
        compiler = await response.parse()
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_compile(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.compile(
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

            compiler = await response.parse()
            assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compile_dashboard(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compile_dashboard_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
            source="source",
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
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_compile_dashboard(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_compile_dashboard(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            tenant_key="tenant_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.execute(
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
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.execute(
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
                ]
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
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.execute(
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
        compiler = await response.parse()
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.execute(
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

            compiler = await response.parse()
            assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_render(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.render(
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
        assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_render_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.render(
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
                ]
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
        assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_render(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.render(
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
        compiler = await response.parse()
        assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_render(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.render(
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

            compiler = await response.parse()
            assert_matches_type(CompilerRenderResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
            source="source",
            auto_fix=True,
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
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.resolve(
            connection_id="connection_id",
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
            query_kater_id="query_kater_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.validate()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.validate(
            source="source",
            auto_fix=True,
            connection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True
