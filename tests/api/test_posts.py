import pytest


@pytest.mark.api
def test_get_posts(posts_api):
    response = posts_api.get_posts()

    assert response.status_code == 200

    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0
    assert "id" in posts[0]
    assert "title" in posts[0]


@pytest.mark.api
def test_get_single_post(posts_api):
    response = posts_api.get_post(1)

    assert response.status_code == 200

    post = response.json()

    assert post["id"] == 1
    assert post["userId"] == 1
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)


@pytest.mark.api
def test_create_post(posts_api):
    payload = {
        "title": "QA automation",
        "body": "API test with pytest",
        "userId": 1,
    }

    response = posts_api.create_post(payload)

    assert response.status_code == 201

    created_post = response.json()

    assert created_post["title"] == payload["title"]
    assert created_post["body"] == payload["body"]
    assert created_post["userId"] == payload["userId"]
    assert "id" in created_post