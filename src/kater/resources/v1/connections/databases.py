# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.connections import database_update_params, database_update_schema_params
from ....types.v1.connections.database_update_response import DatabaseUpdateResponse
from ....types.v1.connections.database_update_schema_response import DatabaseUpdateSchemaResponse

__all__ = ["DatabasesResource", "AsyncDatabasesResource"]


class DatabasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return DatabasesResourceWithStreamingResponse(self)

    def update(
        self,
        database_id: str,
        *,
        connection_id: str,
        auto_merge: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatabaseUpdateResponse:
        """Update a database's metadata.

        Updates label and/or description fields directly.

        If a name change is requested,
        a GitHub PR is created to update view YAML files. The name change is applied to
        the DB when the PR merges (or immediately if auto_merge is true or no views are
        affected).

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: DatabaseNotFoundError: If database doesn't exist (404)

        Args:
          auto_merge: If true and a name change requires a PR, auto-merge it

          description: Database description

          label: Human-readable display label

          name: Database name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return self._patch(
            f"/api/v1/connections/{connection_id}/databases/{database_id}",
            body=maybe_transform(
                {
                    "auto_merge": auto_merge,
                    "description": description,
                    "label": label,
                    "name": name,
                },
                database_update_params.DatabaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatabaseUpdateResponse,
        )

    def delete_schema(
        self,
        schema_id: str,
        *,
        connection_id: str,
        database_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a schema from a connection.

        Soft-deletes the schema record, setting deleted_at and deleted_by fields. The
        connection_id and database_id path parameters provide context for the resource
        hierarchy, though the schema_id alone uniquely identifies the record.

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: SchemaNotFoundError: If schema doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/connections/{connection_id}/databases/{database_id}/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_schema(
        self,
        schema_id: str,
        *,
        connection_id: str,
        database_id: str,
        auto_merge: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatabaseUpdateSchemaResponse:
        """Update a schema's metadata.

        Updates label and/or description fields directly.

        If a name change is requested,
        a GitHub PR is created to update view YAML files. The name change is applied to
        the DB when the PR merges (or immediately if auto_merge is true or no views are
        affected).

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: SchemaNotFoundError: If schema doesn't exist (404)

        Args:
          auto_merge: If true and a name change requires a PR, auto-merge it

          description: Schema description

          label: Human-readable display label

          name: Schema name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._patch(
            f"/api/v1/connections/{connection_id}/databases/{database_id}/schemas/{schema_id}",
            body=maybe_transform(
                {
                    "auto_merge": auto_merge,
                    "description": description,
                    "label": label,
                    "name": name,
                },
                database_update_schema_params.DatabaseUpdateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatabaseUpdateSchemaResponse,
        )


class AsyncDatabasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncDatabasesResourceWithStreamingResponse(self)

    async def update(
        self,
        database_id: str,
        *,
        connection_id: str,
        auto_merge: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatabaseUpdateResponse:
        """Update a database's metadata.

        Updates label and/or description fields directly.

        If a name change is requested,
        a GitHub PR is created to update view YAML files. The name change is applied to
        the DB when the PR merges (or immediately if auto_merge is true or no views are
        affected).

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: DatabaseNotFoundError: If database doesn't exist (404)

        Args:
          auto_merge: If true and a name change requires a PR, auto-merge it

          description: Database description

          label: Human-readable display label

          name: Database name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        return await self._patch(
            f"/api/v1/connections/{connection_id}/databases/{database_id}",
            body=await async_maybe_transform(
                {
                    "auto_merge": auto_merge,
                    "description": description,
                    "label": label,
                    "name": name,
                },
                database_update_params.DatabaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatabaseUpdateResponse,
        )

    async def delete_schema(
        self,
        schema_id: str,
        *,
        connection_id: str,
        database_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a schema from a connection.

        Soft-deletes the schema record, setting deleted_at and deleted_by fields. The
        connection_id and database_id path parameters provide context for the resource
        hierarchy, though the schema_id alone uniquely identifies the record.

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: SchemaNotFoundError: If schema doesn't exist (404)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/connections/{connection_id}/databases/{database_id}/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_schema(
        self,
        schema_id: str,
        *,
        connection_id: str,
        database_id: str,
        auto_merge: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatabaseUpdateSchemaResponse:
        """Update a schema's metadata.

        Updates label and/or description fields directly.

        If a name change is requested,
        a GitHub PR is created to update view YAML files. The name change is applied to
        the DB when the PR merges (or immediately if auto_merge is true or no views are
        affected).

        RLS: Filtered to current client (DualClientRLSDB).

        Raises: SchemaNotFoundError: If schema doesn't exist (404)

        Args:
          auto_merge: If true and a name change requires a PR, auto-merge it

          description: Schema description

          label: Human-readable display label

          name: Schema name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not database_id:
            raise ValueError(f"Expected a non-empty value for `database_id` but received {database_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._patch(
            f"/api/v1/connections/{connection_id}/databases/{database_id}/schemas/{schema_id}",
            body=await async_maybe_transform(
                {
                    "auto_merge": auto_merge,
                    "description": description,
                    "label": label,
                    "name": name,
                },
                database_update_schema_params.DatabaseUpdateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatabaseUpdateSchemaResponse,
        )


class DatabasesResourceWithRawResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

        self.update = to_raw_response_wrapper(
            databases.update,
        )
        self.delete_schema = to_raw_response_wrapper(
            databases.delete_schema,
        )
        self.update_schema = to_raw_response_wrapper(
            databases.update_schema,
        )


class AsyncDatabasesResourceWithRawResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

        self.update = async_to_raw_response_wrapper(
            databases.update,
        )
        self.delete_schema = async_to_raw_response_wrapper(
            databases.delete_schema,
        )
        self.update_schema = async_to_raw_response_wrapper(
            databases.update_schema,
        )


class DatabasesResourceWithStreamingResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

        self.update = to_streamed_response_wrapper(
            databases.update,
        )
        self.delete_schema = to_streamed_response_wrapper(
            databases.delete_schema,
        )
        self.update_schema = to_streamed_response_wrapper(
            databases.update_schema,
        )


class AsyncDatabasesResourceWithStreamingResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

        self.update = async_to_streamed_response_wrapper(
            databases.update,
        )
        self.delete_schema = async_to_streamed_response_wrapper(
            databases.delete_schema,
        )
        self.update_schema = async_to_streamed_response_wrapper(
            databases.update_schema,
        )
