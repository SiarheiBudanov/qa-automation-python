import logging

import requests
from jsonschema import Draft202012Validator

from config.settings import BASE_URL

logger = logging.getLogger(__name__)


class PostsApi:
    BASE_URL = BASE_URL

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/json"}
        )

    def _request(self, method, url, **kwargs):
        logger.info("HTTP request: %s %s", method, url)

        response = self.session.request(
            method,
            url,
            **kwargs,
        )

        logger.info(
            "HTTP response: %s %s",
            response.status_code,
            response.url,
        )

        return response

    def get_posts(self):
        return self._request(
            "GET",
            f"{self.BASE_URL}/posts",
            timeout=10,
        )

    def get_post(self, post_id):
        return self._request(
            "GET",
            f"{self.BASE_URL}/posts/{post_id}",
            timeout=10,
        )

    def create_post(self, payload):
        return self._request(
            "POST",
            f"{self.BASE_URL}/posts",
            json=payload,
            timeout=10,
        )
    def validate_response_schema(self, response, schema):
        payload = response.json()

        validator = Draft202012Validator(schema)
        errors = sorted(
            validator.iter_errors(payload),
            key=lambda error: list(error.path),
        )

        if errors:
            details = "\n".join(
                f"{list(error.path)}: {error.message}"
                for error in errors
            )

            raise AssertionError(
                f"JSON schema validation failed:\n{details}"
            )

        return True


    def close(self):
        self.session.close()
