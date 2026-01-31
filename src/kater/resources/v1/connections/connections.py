# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from .databases import (
    DatabasesResource,
    AsyncDatabasesResource,
    DatabasesResourceWithRawResponse,
    AsyncDatabasesResourceWithRawResponse,
    DatabasesResourceWithStreamingResponse,
    AsyncDatabasesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ....types.v1 import (
    connection_list_params,
    connection_create_params,
    connection_update_params,
    connection_list_syncs_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.connection import Connection
from ....types.v1.database_config_param import DatabaseConfigParam
from ....types.v1.connection_list_response import ConnectionListResponse
from ....types.v1.connection_sync_response import ConnectionSyncResponse
from ....types.v1.connection_list_syncs_response import ConnectionListSyncsResponse
from ....types.v1.connection_approve_sync_response import ConnectionApproveSyncResponse
from ....types.v1.connection_retrieve_schema_response import ConnectionRetrieveSchemaResponse
from ....types.v1.connection_retrieve_credential_response import ConnectionRetrieveCredentialResponse
from ....types.v1.connection_retrieve_sync_status_response import ConnectionRetrieveSyncStatusResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    @cached_property
    def databases(self) -> DatabasesResource:
        return DatabasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return ConnectionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str,
        name: str,
        password: str,
        username: str,
        warehouse_type: Literal["postgresql"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          databases: Databases to include in the connection (at least one required)

          host: Database host

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          password: Database password

          username: Database username

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          port: Database port

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account: str,
        auth: connection_create_params.SnowflakeConnectionConfigAuth,
        databases: Iterable[DatabaseConfigParam],
        name: str,
        role: str,
        username: str,
        warehouse: str,
        warehouse_type: Literal["snowflake"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          account: Snowflake account identifier (e.g., 'xy12345.us-east-1')

          auth: Authentication configuration

          databases: Databases to include in the connection (at least one required)

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          role: Snowflake role

          username: Snowflake username

          warehouse: Compute warehouse name

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        access_token: str,
        databases: Iterable[DatabaseConfigParam],
        http_path: str,
        name: str,
        server_hostname: str,
        warehouse_type: Literal["databricks"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          access_token: Databricks personal access token

          databases: Databases to include in the connection (at least one required)

          http_path: SQL warehouse HTTP path (e.g., '/sql/1.0/warehouses/xxx')

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          server_hostname: Databricks server hostname (e.g., 'dbc-xxx.cloud.databricks.com')

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str,
        name: str,
        password: str,
        username: str,
        warehouse_type: Literal["clickhouse"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          databases: Databases to include in the connection (at least one required)

          host: ClickHouse host

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          password: ClickHouse password

          username: ClickHouse username

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          port: ClickHouse port

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str,
        name: str,
        password: str,
        username: str,
        warehouse_type: Literal["mssql"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          databases: Databases to include in the connection (at least one required)

          host: SQL Server host

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          password: SQL Server password

          username: SQL Server username

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          port: SQL Server port

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["databases", "host", "name", "password", "username", "warehouse_type"],
        ["account", "auth", "databases", "name", "role", "username", "warehouse", "warehouse_type"],
        ["access_token", "databases", "http_path", "name", "server_hostname", "warehouse_type"],
    )
    def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str | Omit = omit,
        name: str,
        password: str | Omit = omit,
        username: str | Omit = omit,
        warehouse_type: Literal["postgresql"]
        | Literal["snowflake"]
        | Literal["databricks"]
        | Literal["clickhouse"]
        | Literal["mssql"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        account: str | Omit = omit,
        auth: connection_create_params.SnowflakeConnectionConfigAuth | Omit = omit,
        role: str | Omit = omit,
        warehouse: str | Omit = omit,
        access_token: str | Omit = omit,
        http_path: str | Omit = omit,
        server_hostname: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        return self._post(
            "/api/v1/connections",
            body=maybe_transform(
                {
                    "databases": databases,
                    "host": host,
                    "name": name,
                    "password": password,
                    "username": username,
                    "warehouse_type": warehouse_type,
                    "description": description,
                    "label": label,
                    "port": port,
                    "query_timeout": query_timeout,
                    "query_timezone_conversion": query_timezone_conversion,
                    "account": account,
                    "auth": auth,
                    "role": role,
                    "warehouse": warehouse,
                    "access_token": access_token,
                    "http_path": http_path,
                    "server_hostname": server_hostname,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Get a single warehouse connection by ID.

        Returns connection from the database (source of truth) with full hierarchy. For
        YAML output compatible with repository files (using kater_id), use the GET
        /connections/{id}/schema endpoint instead.

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: NotFoundError: If connection doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/api/v1/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    def update(
        self,
        connection_id: str,
        *,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Update a warehouse connection's metadata.

        Updates name, label, and/or description fields.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ConnectionNotFoundError: If connection doesn't exist (404)

        Args:
          description: Connection description

          label: Human-readable display label

          name: Connection name (snake_case identifier)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._patch(
            f"/api/v1/connections/{connection_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "label": label,
                    "name": name,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    def list(
        self,
        *,
        status: Literal["approved", "pending", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """
        List warehouse connections for the client.

        Filter connections by approval status using the `status` query parameter:

        - `approved` (default): Only approved connections (is_pending_approval=false)
        - `pending`: Only connections awaiting PR approval (is_pending_approval=true)
        - `all`: All connections regardless of approval status

        Pending connections include their approval PR URLs when available. Returns empty
        list if GitHub is not configured.

        RLS: Filtered to current client (DualClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, connection_list_params.ConnectionListParams),
            ),
            cast_to=ConnectionListResponse,
        )

    def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a warehouse connection.

        Soft-deletes the connection record and cascades to all associated databases and
        schemas, setting deleted_at and deleted_by fields.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ConnectionNotFoundError: If connection doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def approve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Merge the PR for a pending connection to finalize it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/api/v1/connections/{connection_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    def approve_sync(
        self,
        sync_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionApproveSyncResponse:
        """
        Merge the PR for a completed schema sync.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._post(
            f"/api/v1/connections/{connection_id}/sync/{sync_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionApproveSyncResponse,
        )

    def list_syncs(
        self,
        connection_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListSyncsResponse:
        """
        List all schema sync records for a connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/api/v1/connections/{connection_id}/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    connection_list_syncs_params.ConnectionListSyncsParams,
                ),
            ),
            cast_to=ConnectionListSyncsResponse,
        )

    def retrieve_credential(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveCredentialResponse:
        """
        Get decrypted warehouse credentials for a connection.

        Returns the decrypted credentials for a connection. This is sensitive data and
        should only be used when actually needed for warehouse operations.

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: NotFoundError: If connection doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return cast(
            ConnectionRetrieveCredentialResponse,
            self._get(
                f"/api/v1/connections/{connection_id}/credential",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ConnectionRetrieveCredentialResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_schema(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveSchemaResponse:
        """
        Get connection as a ConnectionSchema object.

        Returns the connection in the YAML-compatible schema format with full
        database/schema hierarchy.

        RLS: Automatically filtered by client_id from auth context.

        Raises: ConnectionNotFoundError: If connection not found or deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/api/v1/connections/{connection_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveSchemaResponse,
        )

    def retrieve_sync_status(
        self,
        sync_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveSyncStatusResponse:
        """
        Get the current status of a schema sync workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._get(
            f"/api/v1/connections/{connection_id}/sync/{sync_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveSyncStatusResponse,
        )

    def stream_sync_progress(
        self,
        sync_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Server-Sent Events stream for real-time sync progress updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._get(
            f"/api/v1/connections/{connection_id}/sync/{sync_id}/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def sync(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionSyncResponse:
        """Start a schema sync workflow.

        Returns 202 Accepted with sync_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/api/v1/connections/{connection_id}/sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionSyncResponse,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    @cached_property
    def databases(self) -> AsyncDatabasesResource:
        return AsyncDatabasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncConnectionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str,
        name: str,
        password: str,
        username: str,
        warehouse_type: Literal["postgresql"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          databases: Databases to include in the connection (at least one required)

          host: Database host

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          password: Database password

          username: Database username

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          port: Database port

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account: str,
        auth: connection_create_params.SnowflakeConnectionConfigAuth,
        databases: Iterable[DatabaseConfigParam],
        name: str,
        role: str,
        username: str,
        warehouse: str,
        warehouse_type: Literal["snowflake"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          account: Snowflake account identifier (e.g., 'xy12345.us-east-1')

          auth: Authentication configuration

          databases: Databases to include in the connection (at least one required)

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          role: Snowflake role

          username: Snowflake username

          warehouse: Compute warehouse name

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        access_token: str,
        databases: Iterable[DatabaseConfigParam],
        http_path: str,
        name: str,
        server_hostname: str,
        warehouse_type: Literal["databricks"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          access_token: Databricks personal access token

          databases: Databases to include in the connection (at least one required)

          http_path: SQL warehouse HTTP path (e.g., '/sql/1.0/warehouses/xxx')

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          server_hostname: Databricks server hostname (e.g., 'dbc-xxx.cloud.databricks.com')

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str,
        name: str,
        password: str,
        username: str,
        warehouse_type: Literal["clickhouse"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          databases: Databases to include in the connection (at least one required)

          host: ClickHouse host

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          password: ClickHouse password

          username: ClickHouse username

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          port: ClickHouse port

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str,
        name: str,
        password: str,
        username: str,
        warehouse_type: Literal["mssql"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Create a new warehouse connection with PR approval flow.

        Args:
          databases: Databases to include in the connection (at least one required)

          host: SQL Server host

          name: Name of the connection (snake_case: lowercase letters, numbers, underscores)

          password: SQL Server password

          username: SQL Server username

          warehouse_type: Warehouse type

          description: Description of the connection

          label: Human-readable label for the connection (defaults to name if not set)

          port: SQL Server port

          query_timeout: Query timeout in seconds (1-3600)

          query_timezone_conversion: Timezone conversion mode: 'do_not_convert' or 'convert_to_utc'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["databases", "host", "name", "password", "username", "warehouse_type"],
        ["account", "auth", "databases", "name", "role", "username", "warehouse", "warehouse_type"],
        ["access_token", "databases", "http_path", "name", "server_hostname", "warehouse_type"],
    )
    async def create(
        self,
        *,
        databases: Iterable[DatabaseConfigParam],
        host: str | Omit = omit,
        name: str,
        password: str | Omit = omit,
        username: str | Omit = omit,
        warehouse_type: Literal["postgresql"]
        | Literal["snowflake"]
        | Literal["databricks"]
        | Literal["clickhouse"]
        | Literal["mssql"],
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        port: int | Omit = omit,
        query_timeout: Optional[int] | Omit = omit,
        query_timezone_conversion: Optional[str] | Omit = omit,
        account: str | Omit = omit,
        auth: connection_create_params.SnowflakeConnectionConfigAuth | Omit = omit,
        role: str | Omit = omit,
        warehouse: str | Omit = omit,
        access_token: str | Omit = omit,
        http_path: str | Omit = omit,
        server_hostname: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        return await self._post(
            "/api/v1/connections",
            body=await async_maybe_transform(
                {
                    "databases": databases,
                    "host": host,
                    "name": name,
                    "password": password,
                    "username": username,
                    "warehouse_type": warehouse_type,
                    "description": description,
                    "label": label,
                    "port": port,
                    "query_timeout": query_timeout,
                    "query_timezone_conversion": query_timezone_conversion,
                    "account": account,
                    "auth": auth,
                    "role": role,
                    "warehouse": warehouse,
                    "access_token": access_token,
                    "http_path": http_path,
                    "server_hostname": server_hostname,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    async def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Get a single warehouse connection by ID.

        Returns connection from the database (source of truth) with full hierarchy. For
        YAML output compatible with repository files (using kater_id), use the GET
        /connections/{id}/schema endpoint instead.

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: NotFoundError: If connection doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/api/v1/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    async def update(
        self,
        connection_id: str,
        *,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Update a warehouse connection's metadata.

        Updates name, label, and/or description fields.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ConnectionNotFoundError: If connection doesn't exist (404)

        Args:
          description: Connection description

          label: Human-readable display label

          name: Connection name (snake_case identifier)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._patch(
            f"/api/v1/connections/{connection_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "label": label,
                    "name": name,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    async def list(
        self,
        *,
        status: Literal["approved", "pending", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """
        List warehouse connections for the client.

        Filter connections by approval status using the `status` query parameter:

        - `approved` (default): Only approved connections (is_pending_approval=false)
        - `pending`: Only connections awaiting PR approval (is_pending_approval=true)
        - `all`: All connections regardless of approval status

        Pending connections include their approval PR URLs when available. Returns empty
        list if GitHub is not configured.

        RLS: Filtered to current client (DualClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, connection_list_params.ConnectionListParams),
            ),
            cast_to=ConnectionListResponse,
        )

    async def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a warehouse connection.

        Soft-deletes the connection record and cascades to all associated databases and
        schemas, setting deleted_at and deleted_by fields.

        RLS: Filtered to current client (ClientRLSDB).

        Raises: ConnectionNotFoundError: If connection doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def approve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connection:
        """
        Merge the PR for a pending connection to finalize it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/api/v1/connections/{connection_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )

    async def approve_sync(
        self,
        sync_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionApproveSyncResponse:
        """
        Merge the PR for a completed schema sync.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._post(
            f"/api/v1/connections/{connection_id}/sync/{sync_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionApproveSyncResponse,
        )

    async def list_syncs(
        self,
        connection_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListSyncsResponse:
        """
        List all schema sync records for a connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/api/v1/connections/{connection_id}/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    connection_list_syncs_params.ConnectionListSyncsParams,
                ),
            ),
            cast_to=ConnectionListSyncsResponse,
        )

    async def retrieve_credential(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveCredentialResponse:
        """
        Get decrypted warehouse credentials for a connection.

        Returns the decrypted credentials for a connection. This is sensitive data and
        should only be used when actually needed for warehouse operations.

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: NotFoundError: If connection doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return cast(
            ConnectionRetrieveCredentialResponse,
            await self._get(
                f"/api/v1/connections/{connection_id}/credential",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ConnectionRetrieveCredentialResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_schema(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveSchemaResponse:
        """
        Get connection as a ConnectionSchema object.

        Returns the connection in the YAML-compatible schema format with full
        database/schema hierarchy.

        RLS: Automatically filtered by client_id from auth context.

        Raises: ConnectionNotFoundError: If connection not found or deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/api/v1/connections/{connection_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveSchemaResponse,
        )

    async def retrieve_sync_status(
        self,
        sync_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveSyncStatusResponse:
        """
        Get the current status of a schema sync workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._get(
            f"/api/v1/connections/{connection_id}/sync/{sync_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveSyncStatusResponse,
        )

    async def stream_sync_progress(
        self,
        sync_id: str,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Server-Sent Events stream for real-time sync progress updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._get(
            f"/api/v1/connections/{connection_id}/sync/{sync_id}/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def sync(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionSyncResponse:
        """Start a schema sync workflow.

        Returns 202 Accepted with sync_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/api/v1/connections/{connection_id}/sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionSyncResponse,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connections.update,
        )
        self.list = to_raw_response_wrapper(
            connections.list,
        )
        self.delete = to_raw_response_wrapper(
            connections.delete,
        )
        self.approve = to_raw_response_wrapper(
            connections.approve,
        )
        self.approve_sync = to_raw_response_wrapper(
            connections.approve_sync,
        )
        self.list_syncs = to_raw_response_wrapper(
            connections.list_syncs,
        )
        self.retrieve_credential = to_raw_response_wrapper(
            connections.retrieve_credential,
        )
        self.retrieve_schema = to_raw_response_wrapper(
            connections.retrieve_schema,
        )
        self.retrieve_sync_status = to_raw_response_wrapper(
            connections.retrieve_sync_status,
        )
        self.stream_sync_progress = to_raw_response_wrapper(
            connections.stream_sync_progress,
        )
        self.sync = to_raw_response_wrapper(
            connections.sync,
        )

    @cached_property
    def databases(self) -> DatabasesResourceWithRawResponse:
        return DatabasesResourceWithRawResponse(self._connections.databases)


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connections.delete,
        )
        self.approve = async_to_raw_response_wrapper(
            connections.approve,
        )
        self.approve_sync = async_to_raw_response_wrapper(
            connections.approve_sync,
        )
        self.list_syncs = async_to_raw_response_wrapper(
            connections.list_syncs,
        )
        self.retrieve_credential = async_to_raw_response_wrapper(
            connections.retrieve_credential,
        )
        self.retrieve_schema = async_to_raw_response_wrapper(
            connections.retrieve_schema,
        )
        self.retrieve_sync_status = async_to_raw_response_wrapper(
            connections.retrieve_sync_status,
        )
        self.stream_sync_progress = async_to_raw_response_wrapper(
            connections.stream_sync_progress,
        )
        self.sync = async_to_raw_response_wrapper(
            connections.sync,
        )

    @cached_property
    def databases(self) -> AsyncDatabasesResourceWithRawResponse:
        return AsyncDatabasesResourceWithRawResponse(self._connections.databases)


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connections.update,
        )
        self.list = to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            connections.delete,
        )
        self.approve = to_streamed_response_wrapper(
            connections.approve,
        )
        self.approve_sync = to_streamed_response_wrapper(
            connections.approve_sync,
        )
        self.list_syncs = to_streamed_response_wrapper(
            connections.list_syncs,
        )
        self.retrieve_credential = to_streamed_response_wrapper(
            connections.retrieve_credential,
        )
        self.retrieve_schema = to_streamed_response_wrapper(
            connections.retrieve_schema,
        )
        self.retrieve_sync_status = to_streamed_response_wrapper(
            connections.retrieve_sync_status,
        )
        self.stream_sync_progress = to_streamed_response_wrapper(
            connections.stream_sync_progress,
        )
        self.sync = to_streamed_response_wrapper(
            connections.sync,
        )

    @cached_property
    def databases(self) -> DatabasesResourceWithStreamingResponse:
        return DatabasesResourceWithStreamingResponse(self._connections.databases)


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connections.delete,
        )
        self.approve = async_to_streamed_response_wrapper(
            connections.approve,
        )
        self.approve_sync = async_to_streamed_response_wrapper(
            connections.approve_sync,
        )
        self.list_syncs = async_to_streamed_response_wrapper(
            connections.list_syncs,
        )
        self.retrieve_credential = async_to_streamed_response_wrapper(
            connections.retrieve_credential,
        )
        self.retrieve_schema = async_to_streamed_response_wrapper(
            connections.retrieve_schema,
        )
        self.retrieve_sync_status = async_to_streamed_response_wrapper(
            connections.retrieve_sync_status,
        )
        self.stream_sync_progress = async_to_streamed_response_wrapper(
            connections.stream_sync_progress,
        )
        self.sync = async_to_streamed_response_wrapper(
            connections.sync,
        )

    @cached_property
    def databases(self) -> AsyncDatabasesResourceWithStreamingResponse:
        return AsyncDatabasesResourceWithStreamingResponse(self._connections.databases)
