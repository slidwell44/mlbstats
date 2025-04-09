import logging
import typing as t
import requests

from pydantic import ValidationError

from config import ENDPOINTS, EndpointConfig
from schemas.responses import GenericResponse


logger = logging.getLogger(__name__)


class GetterService:
    def __init__(self, endpoints=None):
        if endpoints is None:
            endpoints = ENDPOINTS

        self.endpoints = endpoints

    def _endpoint_validator(self, endpoint: str) -> EndpointConfig:
        if endpoint not in self.endpoints:
            raise ValueError(f"Invalid endpoint: {endpoint}")

        try:
            value: EndpointConfig = self.endpoints.get(endpoint)
            return value
        except Exception as e:
            raise ValueError(f"Endpoint configuration error for '{endpoint}': {e}")

    def _get(
        self, endpoint: str, params: dict, *, request_kwargs: dict[str, t.Any] = None
    ) -> dict:
        if request_kwargs is None:
            request_kwargs = {}

        ep_config: EndpointConfig = self._endpoint_validator(endpoint)

        url = ep_config.url
        path_params = {}
        query_params = {}

        # Separate path and query parameters
        for key, value in params.items():
            if key in ep_config.path_params:
                spec = ep_config.path_params[key]
                if spec.type == "bool":
                    # Convert a boolean string to the correct URL representation.
                    value_str = (
                        spec.True_str
                        if str(value).lower() == "true"
                        else spec.False_str
                    )
                    path_params[key] = value_str or ""
                else:
                    path_params[key] = str(value)
            elif key in ep_config.query_params:
                query_params[key] = str(value)
            else:
                logger.debug(f"Ignoring parameter {key} not defined in endpoint.")

        # Replace path parameters in the URL
        for key, value in path_params.items():
            replacement = value
            if ep_config.path_params[key].leading_slash and not value.startswith("/"):
                replacement = "/" + replacement
            if ep_config.path_params[key].trailing_slash and not value.endswith("/"):
                replacement += "/"
            url = url.replace("{" + key + "}", replacement)

        # Check if any required path parameter is missing and use default if available.
        while "{" in url and "}" in url:
            # For missing optional parameters remove the placeholder.
            start = url.find("{")
            end = url.find("}") + 1
            url = url[:start] + url[end:]

        # Append the query string
        if query_params:
            query_str = "&".join([f"{k}={v}" for k, v in query_params.items()])
            url += "?" + query_str

        logger.debug(f"Constructed URL: {url}")

        # Make the HTTP request
        response = requests.get(url, **request_kwargs)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        data = response.json()

        # Validate response with a generic response model (replace with endpoint-specific models as needed)
        try:
            parsed_response = GenericResponse.model_validate(data)
        except ValidationError as e:
            raise ValueError(f"Response validation error: {e}")

        return parsed_response.model_dump()
