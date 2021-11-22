from typing import Any

from httpx import Request
from httpx._auth import FunctionAuth

from yt_client import ApiClient


class AuthApiClient(ApiClient):
    def __init__(self, host: str = None, token: str = None, **kwargs: Any) -> None:
        def auth_func(request: Request):
            request.headers["authorization"] = token
            return request

        super().__init__(host, auth=FunctionAuth(auth_func), **kwargs)
