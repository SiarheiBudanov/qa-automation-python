import pytest


@pytest.mark.api
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"title": ""},
        {"body": ""},
        {"userId": "invalid"},
        {"title": None, "body": None, "userId": None},
    ],
)
def test_create_post_invalid_payload(posts_api, payload):
    response = posts_api.create_post(payload)

    assert response.status_code in (201, 400, 422)