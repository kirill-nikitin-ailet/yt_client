from asyncio import get_event_loop
from functools import lru_cache
from typing import Any, Awaitable, Callable, Dict, Generic, Type, TypeVar, overload

from httpx import AsyncClient, Request, Response
from pydantic import ValidationError

from yt_client.api.default_api import AsyncDefaultApi, SyncDefaultApi
from yt_client.exceptions import ResponseHandlingException, ResponseValidationError, UnexpectedResponse

ClientT = TypeVar("ClientT", bound="ApiClient")


class AsyncApis(Generic[ClientT]):
    def __init__(self, client: ClientT):
        self.client = client

        self.default_api = AsyncDefaultApi(self.client)


class SyncApis(Generic[ClientT]):
    def __init__(self, client: ClientT):
        self.client = client

        self.default_api = SyncDefaultApi(self.client)


T = TypeVar("T")
Send = Callable[[Request], Awaitable[Response]]
MiddlewareT = Callable[[Request, Send], Awaitable[Response]]


class ApiClient:
    def __init__(self, host: str = None, **kwargs: Any) -> None:
        self.host = host
        self.middleware: MiddlewareT = BaseMiddleware()
        self._async_client = AsyncClient(**kwargs)

    async def close(self):
        await self._async_client.aclose()

    @overload
    async def request(
        self, *, type_: Type[T], method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> T:
        ...

    @overload  # noqa F811
    async def request(
        self, *, type_: None, method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> None:
        ...

    async def request(  # noqa F811
        self, *, type_: Any, method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> Any:
        if path_params is None:
            path_params = {}
        url = (self.host or "") + url.format(**path_params)
        request = Request(method, url, **kwargs)
        return await self.send(request, type_)

    @overload
    def request_sync(self, *, type_: Type[T], **kwargs: Any) -> T:
        ...

    @overload  # noqa F811
    def request_sync(self, *, type_: None, **kwargs: Any) -> None:
        ...

    def request_sync(self, *, type_: Any, **kwargs: Any) -> Any:  # noqa F811
        """
        This method is not used by the generated apis, but is included for convenience
        """
        return get_event_loop().run_until_complete(self.request(type_=type_, **kwargs))

    async def send(self, request: Request, type_: Type[T]) -> T:
        response = await self.middleware(request, self.send_inner)
        if 200 <= response.status_code <= 299:
            if type_ is None:
                return response
            try:
                return parse_as_type(response.json(), type_)
            except ValidationError as e:
                raise ResponseValidationError.for_exception(e, response)
        raise UnexpectedResponse.for_response(response)

    async def send_inner(self, request: Request) -> Response:
        try:
            response = await self._async_client.send(request)
        except Exception as e:
            raise ResponseHandlingException(e)
        return response

    def add_middleware(self, middleware: MiddlewareT) -> None:
        current_middleware = self.middleware

        async def new_middleware(request: Request, call_next: Send) -> Response:
            async def inner_send(request: Request) -> Response:
                return await current_middleware(request, call_next)

            return await middleware(request, inner_send)

        self.middleware = new_middleware


class BaseMiddleware:
    async def __call__(self, request: Request, call_next: Send) -> Response:
        return await call_next(request)


@lru_cache(maxsize=None)
def _get_parsing_type(type_: Any, source: str) -> Any:
    from pydantic.main import create_model

    type_name = getattr(type_, "__name__", str(type_))
    return create_model(f"ParsingModel[{type_name}] (for {source})", obj=(type_, ...))


def parse_as_type(obj: Any, type_: Type[T]) -> T:
    model_type = _get_parsing_type(type_, source=parse_as_type.__name__)
    return model_type(obj=obj).obj
