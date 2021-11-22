import inspect

from pydantic import BaseModel

from yt_client import models
from yt_client.api_client import ApiClient, AsyncApis, SyncApis  # noqa F401
from yt_client.auth_api_client import AuthApiClient
from yt_client.exceptions import ResponseValidationError, UnexpectedResponse

for model in inspect.getmembers(models, inspect.isclass):
    if model[1].__module__ == "yt_client.models":
        model_class = model[1]
        if issubclass(model_class, BaseModel):
            model_class.update_forward_refs()
