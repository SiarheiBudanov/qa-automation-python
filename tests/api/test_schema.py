import pytest

from schemas.post_schema import POST_SCHEMA


@pytest.mark.api
def test_single_post_matches_schema(posts_api):
    response = posts_api.get_post(1)

    assert response.status_code == 200

    assert posts_api.validate_response_schema(
        response,
        POST_SCHEMA,
    )