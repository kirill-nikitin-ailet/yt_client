import json
from typing import Any, Dict, Optional

from httpx import Headers, Response

MAX_CONTENT = 200


class ApiException(Exception):
    """Base class"""


class UnexpectedResponse(ApiException):
    """
    Raised when response is not successful (status code not 2xx)

    Encapsulates response status code, content and headers
    """

    def __init__(self, status_code: Optional[int], reason_phrase: str, content: bytes, headers: Headers) -> None:
        self.status_code = status_code
        self.reason_phrase = reason_phrase
        self.content = content
        self.headers = headers

    @staticmethod
    def for_response(response: Response) -> "UnexpectedResponse":
        return UnexpectedResponse(
            status_code=response.status_code,
            reason_phrase=response.reason_phrase,
            content=response.content,
            headers=response.headers,
        )

    def __str__(self) -> str:
        status_code_str = f"{self.status_code}" if self.status_code is not None else ""
        if self.reason_phrase == "" and self.status_code is not None:
            reason_phrase_str = "(Unrecognized Status Code)"
        else:
            reason_phrase_str = f"({self.reason_phrase})"
        status_str = f"{status_code_str} {reason_phrase_str}".strip()
        short_content = self.content if len(self.content) <= MAX_CONTENT else self.content[: MAX_CONTENT - 3] + b" ..."
        raw_content_str = f"Raw response content:\n{short_content!r}"
        return f"Unexpected Response: {status_str}\n{raw_content_str}"

    def structured(self) -> Dict[str, Any]:
        return json.loads(self.content)


class ResponseValidationError(ApiException):
    """
    Raised when validation of the content of the response fails.

    Encapsulates source exception and  response status code, content and headers
    """

    def __init__(self, source: Exception, status_code: Optional[int], content: str, headers: dict = None) -> None:
        self.source = source
        self.status_code = status_code
        self.content = content
        self.headers = headers

    @staticmethod
    def for_exception(source: Exception, response: Response) -> "ResponseValidationError":
        return ResponseValidationError(source, response.status_code, response.content, response.headers)


class ResponseHandlingException(ApiException):
    """
    Raised when the request fails or the response breaks

    Encapsulates source exception
    """

    def __init__(self, source: Exception) -> None:
        self.source = source
