# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import v1, readyz, healthz
    from .resources.v1.v1 import V1Resource, AsyncV1Resource
    from .resources.readyz import ReadyzResource, AsyncReadyzResource
    from .resources.healthz import HealthzResource, AsyncHealthzResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Kater", "AsyncKater", "Client", "AsyncClient"]


class Kater(SyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Kater client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `KATER_API_KEY`
        - `bearer_token` from `KATER_AUTH_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("KATER_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("KATER_AUTH_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("KATER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def v1(self) -> V1Resource:
        from .resources.v1 import V1Resource

        return V1Resource(self)

    @cached_property
    def healthz(self) -> HealthzResource:
        from .resources.healthz import HealthzResource

        return HealthzResource(self)

    @cached_property
    def readyz(self) -> ReadyzResource:
        from .resources.readyz import ReadyzResource

        return ReadyzResource(self)

    @cached_property
    def with_raw_response(self) -> KaterWithRawResponse:
        return KaterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KaterWithStreamedResponse:
        return KaterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKater(AsyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncKater client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `KATER_API_KEY`
        - `bearer_token` from `KATER_AUTH_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("KATER_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("KATER_AUTH_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("KATER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def v1(self) -> AsyncV1Resource:
        from .resources.v1 import AsyncV1Resource

        return AsyncV1Resource(self)

    @cached_property
    def healthz(self) -> AsyncHealthzResource:
        from .resources.healthz import AsyncHealthzResource

        return AsyncHealthzResource(self)

    @cached_property
    def readyz(self) -> AsyncReadyzResource:
        from .resources.readyz import AsyncReadyzResource

        return AsyncReadyzResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncKaterWithRawResponse:
        return AsyncKaterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKaterWithStreamedResponse:
        return AsyncKaterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KaterWithRawResponse:
    _client: Kater

    def __init__(self, client: Kater) -> None:
        self._client = client

    @cached_property
    def v1(self) -> v1.V1ResourceWithRawResponse:
        from .resources.v1 import V1ResourceWithRawResponse

        return V1ResourceWithRawResponse(self._client.v1)

    @cached_property
    def healthz(self) -> healthz.HealthzResourceWithRawResponse:
        from .resources.healthz import HealthzResourceWithRawResponse

        return HealthzResourceWithRawResponse(self._client.healthz)

    @cached_property
    def readyz(self) -> readyz.ReadyzResourceWithRawResponse:
        from .resources.readyz import ReadyzResourceWithRawResponse

        return ReadyzResourceWithRawResponse(self._client.readyz)


class AsyncKaterWithRawResponse:
    _client: AsyncKater

    def __init__(self, client: AsyncKater) -> None:
        self._client = client

    @cached_property
    def v1(self) -> v1.AsyncV1ResourceWithRawResponse:
        from .resources.v1 import AsyncV1ResourceWithRawResponse

        return AsyncV1ResourceWithRawResponse(self._client.v1)

    @cached_property
    def healthz(self) -> healthz.AsyncHealthzResourceWithRawResponse:
        from .resources.healthz import AsyncHealthzResourceWithRawResponse

        return AsyncHealthzResourceWithRawResponse(self._client.healthz)

    @cached_property
    def readyz(self) -> readyz.AsyncReadyzResourceWithRawResponse:
        from .resources.readyz import AsyncReadyzResourceWithRawResponse

        return AsyncReadyzResourceWithRawResponse(self._client.readyz)


class KaterWithStreamedResponse:
    _client: Kater

    def __init__(self, client: Kater) -> None:
        self._client = client

    @cached_property
    def v1(self) -> v1.V1ResourceWithStreamingResponse:
        from .resources.v1 import V1ResourceWithStreamingResponse

        return V1ResourceWithStreamingResponse(self._client.v1)

    @cached_property
    def healthz(self) -> healthz.HealthzResourceWithStreamingResponse:
        from .resources.healthz import HealthzResourceWithStreamingResponse

        return HealthzResourceWithStreamingResponse(self._client.healthz)

    @cached_property
    def readyz(self) -> readyz.ReadyzResourceWithStreamingResponse:
        from .resources.readyz import ReadyzResourceWithStreamingResponse

        return ReadyzResourceWithStreamingResponse(self._client.readyz)


class AsyncKaterWithStreamedResponse:
    _client: AsyncKater

    def __init__(self, client: AsyncKater) -> None:
        self._client = client

    @cached_property
    def v1(self) -> v1.AsyncV1ResourceWithStreamingResponse:
        from .resources.v1 import AsyncV1ResourceWithStreamingResponse

        return AsyncV1ResourceWithStreamingResponse(self._client.v1)

    @cached_property
    def healthz(self) -> healthz.AsyncHealthzResourceWithStreamingResponse:
        from .resources.healthz import AsyncHealthzResourceWithStreamingResponse

        return AsyncHealthzResourceWithStreamingResponse(self._client.healthz)

    @cached_property
    def readyz(self) -> readyz.AsyncReadyzResourceWithStreamingResponse:
        from .resources.readyz import AsyncReadyzResourceWithStreamingResponse

        return AsyncReadyzResourceWithStreamingResponse(self._client.readyz)


Client = Kater

AsyncClient = AsyncKater
