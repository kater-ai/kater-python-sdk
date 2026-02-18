# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kater import Kater, AsyncKater
from tests.utils import assert_matches_type
from kater.types.v1 import (
    CompilerCompileResponse,
    CompilerExecuteResponse,
    CompilerResolveResponse,
    CompilerValidateResponse,
    CompilerEnumerateResponse,
    CompilerCompileDashboardResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompiler:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compile(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compile_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
                "ai_context": "ai_context",
                "calculations": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "chart_hints": [
                    {
                        "config": {
                            "color_by": "ref(created_date)",
                            "comparison": "previous_period",
                            "size": "ref(created_date)",
                            "stack_by": "ref(created_date)",
                            "target_value": "target_value",
                            "x_axis": "ref(created_date)",
                            "y_axis": "ref(created_date)",
                        },
                        "recommend": "line",
                        "when": {"foo": "string"},
                    }
                ],
                "custom_properties": {"foo": "bar"},
                "description": "description",
                "dimensions": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "disallowed_widget_types": ["axis_metric_by_dimension"],
                "filters": [
                    {
                        "field": "ref(dim_customer.sale_price)",
                        "name": "x",
                        "operator": "equals",
                        "sql_value": "SUM(ref(sale_price))",
                        "static_values": ["string"],
                    }
                ],
                "inheritance_chain": ["string"],
                "label": "label",
                "limit": 1,
                "measures": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "order_by": {
                    "asc": ["string"],
                    "desc": ["string"],
                },
                "required_access_grants": ["string"],
                "resolved_chart": {
                    "config": {
                        "color_by": "ref(created_date)",
                        "comparison": "previous_period",
                        "size": "ref(created_date)",
                        "stack_by": "ref(created_date)",
                        "target_value": "target_value",
                        "x_axis": "ref(created_date)",
                        "y_axis": "ref(created_date)",
                    },
                    "recommend": "line",
                },
                "resolved_variables": [
                    {
                        "bound_value": "string",
                        "default": "string",
                        "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "name": "x",
                        "type": "STRING",
                        "allowed_values": {
                            "static": [
                                {
                                    "value": "string",
                                    "label": "label",
                                }
                            ]
                        },
                        "constraints": {
                            "max": 0,
                            "max_length": 1,
                            "min": 0,
                            "step": 0,
                        },
                        "description": "description",
                        "is_default": True,
                        "is_runtime": True,
                        "label": "label",
                    }
                ],
                "select_from": [
                    {
                        "cte_alias": "cte_alias",
                        "output_columns": [
                            {
                                "column_alias": "column_alias",
                                "field_name": "field_name",
                                "source_type": "dimension",
                            }
                        ],
                        "ref": "ref(dim_customer.sale_price)",
                        "variables": {"foo": "string"},
                    }
                ],
            },
            source="source",
            tenant_key="tenant_key",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compile(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compile(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compile_dashboard(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compile_dashboard_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            source="source",
            filters={"foo": "string"},
            tenant_key="tenant_key",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compile_dashboard(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compile_dashboard(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enumerate(self, client: Kater) -> None:
        compiler = client.v1.compiler.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enumerate_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            query_refs=["string"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_enumerate(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_enumerate(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute(self, client: Kater) -> None:
        compiler = client.v1.compiler.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
                "ai_context": "ai_context",
                "calculations": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "chart_hints": [
                    {
                        "config": {
                            "color_by": "ref(created_date)",
                            "comparison": "previous_period",
                            "size": "ref(created_date)",
                            "stack_by": "ref(created_date)",
                            "target_value": "target_value",
                            "x_axis": "ref(created_date)",
                            "y_axis": "ref(created_date)",
                        },
                        "recommend": "line",
                        "when": {"foo": "string"},
                    }
                ],
                "custom_properties": {"foo": "bar"},
                "description": "description",
                "dimensions": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "disallowed_widget_types": ["axis_metric_by_dimension"],
                "filters": [
                    {
                        "field": "ref(dim_customer.sale_price)",
                        "name": "x",
                        "operator": "equals",
                        "sql_value": "SUM(ref(sale_price))",
                        "static_values": ["string"],
                    }
                ],
                "inheritance_chain": ["string"],
                "label": "label",
                "limit": 1,
                "measures": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "order_by": {
                    "asc": ["string"],
                    "desc": ["string"],
                },
                "required_access_grants": ["string"],
                "resolved_chart": {
                    "config": {
                        "color_by": "ref(created_date)",
                        "comparison": "previous_period",
                        "size": "ref(created_date)",
                        "stack_by": "ref(created_date)",
                        "target_value": "target_value",
                        "x_axis": "ref(created_date)",
                        "y_axis": "ref(created_date)",
                    },
                    "recommend": "line",
                },
                "resolved_variables": [
                    {
                        "bound_value": "string",
                        "default": "string",
                        "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "name": "x",
                        "type": "STRING",
                        "allowed_values": {
                            "static": [
                                {
                                    "value": "string",
                                    "label": "label",
                                }
                            ]
                        },
                        "constraints": {
                            "max": 0,
                            "max_length": 1,
                            "min": 0,
                            "step": 0,
                        },
                        "description": "description",
                        "is_default": True,
                        "is_runtime": True,
                        "label": "label",
                    }
                ],
                "select_from": [
                    {
                        "cte_alias": "cte_alias",
                        "output_columns": [
                            {
                                "column_alias": "column_alias",
                                "field_name": "field_name",
                                "source_type": "dimension",
                            }
                        ],
                        "ref": "ref(dim_customer.sale_price)",
                        "variables": {"foo": "string"},
                    }
                ],
            },
            source="source",
            tenant_key="tenant_key",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve(self, client: Kater) -> None:
        compiler = client.v1.compiler.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
            source="source",
            auto_fix=True,
            combination="combination",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resolve(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resolve(self, client: Kater) -> None:
        with client.v1.compiler.with_streaming_response.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = response.parse()
            assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate(self, client: Kater) -> None:
        compiler = client.v1.compiler.validate()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: Kater) -> None:
        compiler = client.v1.compiler.validate(
            source="source",
            auto_fix=True,
            connection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: Kater) -> None:
        response = client.v1.compiler.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = response.parse()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compile(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compile_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
                "ai_context": "ai_context",
                "calculations": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "chart_hints": [
                    {
                        "config": {
                            "color_by": "ref(created_date)",
                            "comparison": "previous_period",
                            "size": "ref(created_date)",
                            "stack_by": "ref(created_date)",
                            "target_value": "target_value",
                            "x_axis": "ref(created_date)",
                            "y_axis": "ref(created_date)",
                        },
                        "recommend": "line",
                        "when": {"foo": "string"},
                    }
                ],
                "custom_properties": {"foo": "bar"},
                "description": "description",
                "dimensions": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "disallowed_widget_types": ["axis_metric_by_dimension"],
                "filters": [
                    {
                        "field": "ref(dim_customer.sale_price)",
                        "name": "x",
                        "operator": "equals",
                        "sql_value": "SUM(ref(sale_price))",
                        "static_values": ["string"],
                    }
                ],
                "inheritance_chain": ["string"],
                "label": "label",
                "limit": 1,
                "measures": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "order_by": {
                    "asc": ["string"],
                    "desc": ["string"],
                },
                "required_access_grants": ["string"],
                "resolved_chart": {
                    "config": {
                        "color_by": "ref(created_date)",
                        "comparison": "previous_period",
                        "size": "ref(created_date)",
                        "stack_by": "ref(created_date)",
                        "target_value": "target_value",
                        "x_axis": "ref(created_date)",
                        "y_axis": "ref(created_date)",
                    },
                    "recommend": "line",
                },
                "resolved_variables": [
                    {
                        "bound_value": "string",
                        "default": "string",
                        "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "name": "x",
                        "type": "STRING",
                        "allowed_values": {
                            "static": [
                                {
                                    "value": "string",
                                    "label": "label",
                                }
                            ]
                        },
                        "constraints": {
                            "max": 0,
                            "max_length": 1,
                            "min": 0,
                            "step": 0,
                        },
                        "description": "description",
                        "is_default": True,
                        "is_runtime": True,
                        "label": "label",
                    }
                ],
                "select_from": [
                    {
                        "cte_alias": "cte_alias",
                        "output_columns": [
                            {
                                "column_alias": "column_alias",
                                "field_name": "field_name",
                                "source_type": "dimension",
                            }
                        ],
                        "ref": "ref(dim_customer.sale_price)",
                        "variables": {"foo": "string"},
                    }
                ],
            },
            source="source",
            tenant_key="tenant_key",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compile(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compile(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.compile(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerCompileResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compile_dashboard(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compile_dashboard_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
            source="source",
            filters={"foo": "string"},
            tenant_key="tenant_key",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compile_dashboard(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compile_dashboard(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.compile_dashboard(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_path="dashboard_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerCompileDashboardResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enumerate(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enumerate_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="source",
            query_refs=["string"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_enumerate(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_enumerate(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.enumerate(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerEnumerateResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
                "ai_context": "ai_context",
                "calculations": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "chart_hints": [
                    {
                        "config": {
                            "color_by": "ref(created_date)",
                            "comparison": "previous_period",
                            "size": "ref(created_date)",
                            "stack_by": "ref(created_date)",
                            "target_value": "target_value",
                            "x_axis": "ref(created_date)",
                            "y_axis": "ref(created_date)",
                        },
                        "recommend": "line",
                        "when": {"foo": "string"},
                    }
                ],
                "custom_properties": {"foo": "bar"},
                "description": "description",
                "dimensions": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "disallowed_widget_types": ["axis_metric_by_dimension"],
                "filters": [
                    {
                        "field": "ref(dim_customer.sale_price)",
                        "name": "x",
                        "operator": "equals",
                        "sql_value": "SUM(ref(sale_price))",
                        "static_values": ["string"],
                    }
                ],
                "inheritance_chain": ["string"],
                "label": "label",
                "limit": 1,
                "measures": [
                    {
                        "ref": "ref",
                        "label": "label",
                    }
                ],
                "order_by": {
                    "asc": ["string"],
                    "desc": ["string"],
                },
                "required_access_grants": ["string"],
                "resolved_chart": {
                    "config": {
                        "color_by": "ref(created_date)",
                        "comparison": "previous_period",
                        "size": "ref(created_date)",
                        "stack_by": "ref(created_date)",
                        "target_value": "target_value",
                        "x_axis": "ref(created_date)",
                        "y_axis": "ref(created_date)",
                    },
                    "recommend": "line",
                },
                "resolved_variables": [
                    {
                        "bound_value": "string",
                        "default": "string",
                        "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "name": "x",
                        "type": "STRING",
                        "allowed_values": {
                            "static": [
                                {
                                    "value": "string",
                                    "label": "label",
                                }
                            ]
                        },
                        "constraints": {
                            "max": 0,
                            "max_length": 1,
                            "min": 0,
                            "step": 0,
                        },
                        "description": "description",
                        "is_default": True,
                        "is_runtime": True,
                        "label": "label",
                    }
                ],
                "select_from": [
                    {
                        "cte_alias": "cte_alias",
                        "output_columns": [
                            {
                                "column_alias": "column_alias",
                                "field_name": "field_name",
                                "source_type": "dimension",
                            }
                        ],
                        "ref": "ref(dim_customer.sale_price)",
                        "variables": {"foo": "string"},
                    }
                ],
            },
            source="source",
            tenant_key="tenant_key",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.execute(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            resolved_query={
                "kater_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "x",
                "source_query": "ref(dim_customer.sale_price)",
                "topic": "ref(dim_customer.sale_price)",
                "widget_category": "axis",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerExecuteResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
            source="source",
            auto_fix=True,
            combination="combination",
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.resolve(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_ref="query_ref",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerResolveResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.validate()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKater) -> None:
        compiler = await async_client.v1.compiler.validate(
            source="source",
            auto_fix=True,
            connection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            x_kater_cli_id="X-Kater-CLI-ID",
        )
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKater) -> None:
        response = await async_client.v1.compiler.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compiler = await response.parse()
        assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKater) -> None:
        async with async_client.v1.compiler.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compiler = await response.parse()
            assert_matches_type(CompilerValidateResponse, compiler, path=["response"])

        assert cast(Any, response.is_closed) is True
