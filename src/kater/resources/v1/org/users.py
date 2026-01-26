# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import ClientUserRole
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.org import user_create_params, user_update_params
from ....types.v1.client_user import ClientUser
from ....types.v1.client_user_role import ClientUserRole
from ....types.v1.org.user_list_response import UserListResponse
from ....types.v1.org.user_delete_response import UserDeleteResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        password: str,
        first_name: Optional[str] | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        role: ClientUserRole | Omit = omit,
        username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientUser:
        """
        Create a new user in the current organization.

        Creates the user in PropelAuth and adds them to this organization. The user will
        receive an email to confirm their email address.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          role: Role of a user within a client organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/org/users",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": role,
                    "username": username,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientUser,
        )

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientUser:
        """
        Get a specific user in the current organization.

        RLS: Filtered to current client, can see any user (ClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/api/v1/org/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientUser,
        )

    def update(
        self,
        user_id: str,
        *,
        email: Optional[str] | Omit = omit,
        first_name: Optional[str] | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        password: Optional[str] | Omit = omit,
        picture_url: Optional[str] | Omit = omit,
        role: Optional[ClientUserRole] | Omit = omit,
        username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientUser:
        """
        Update a user in the current organization.

        Different PropelAuth methods are called depending on what's being updated:

        - Email changes require re-confirmation
        - Password changes take effect immediately
        - Profile fields (name, username, picture) are updated together
        - Role changes affect organization permissions

        RLS: Filtered to current client, can update any user (ClientRLSDB).

        Args:
          role: Role of a user within a client organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/api/v1/org/users/{user_id}",
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "password": password,
                    "picture_url": picture_url,
                    "role": role,
                    "username": username,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientUser,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        List all users in the current organization.

        RLS: Filtered to current client, sees all users (ClientRLSDB).
        """
        return self._get(
            "/api/v1/org/users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Soft delete a user from the current organization.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            f"/api/v1/org/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kater-ai/kater-python-sdk#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        password: str,
        first_name: Optional[str] | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        role: ClientUserRole | Omit = omit,
        username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientUser:
        """
        Create a new user in the current organization.

        Creates the user in PropelAuth and adds them to this organization. The user will
        receive an email to confirm their email address.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          role: Role of a user within a client organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/org/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": role,
                    "username": username,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientUser,
        )

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientUser:
        """
        Get a specific user in the current organization.

        RLS: Filtered to current client, can see any user (ClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/api/v1/org/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientUser,
        )

    async def update(
        self,
        user_id: str,
        *,
        email: Optional[str] | Omit = omit,
        first_name: Optional[str] | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        password: Optional[str] | Omit = omit,
        picture_url: Optional[str] | Omit = omit,
        role: Optional[ClientUserRole] | Omit = omit,
        username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientUser:
        """
        Update a user in the current organization.

        Different PropelAuth methods are called depending on what's being updated:

        - Email changes require re-confirmation
        - Password changes take effect immediately
        - Profile fields (name, username, picture) are updated together
        - Role changes affect organization permissions

        RLS: Filtered to current client, can update any user (ClientRLSDB).

        Args:
          role: Role of a user within a client organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/api/v1/org/users/{user_id}",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "password": password,
                    "picture_url": picture_url,
                    "role": role,
                    "username": username,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientUser,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        List all users in the current organization.

        RLS: Filtered to current client, sees all users (ClientRLSDB).
        """
        return await self._get(
            "/api/v1/org/users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Soft delete a user from the current organization.

        RLS: Filtered to current client (ClientRLSDB).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            f"/api/v1/org/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
