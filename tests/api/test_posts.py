import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)

    assert response.status_code == 200

    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0
    assert "id" in posts[0]
    assert "title" in posts[0]


@pytest.mark.api
def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    post = response.json()

    assert post["id"] == 1
    assert post["userId"] == 1
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)


@pytest.mark.api
def test_create_post():
    payload = {
        "title": "QA automation",
        "body": "API test with pytest",
        "userId": 1,
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 201

    created_post = response.json()

    assert created_post["title"] == payload["title"]
    assert created_post["body"] == payload["body"]
    assert created_post["userId"] == payload["userId"]
    assert "id" in created_post