import pytest
import requests


@pytest.mark.api
def test_httpbin_get():
    response = requests.get(
        "https://httpbin.org/get",
        params={"test": "pytest"},
        timeout=10,
    )

    response.raise_for_status()

    assert response.status_code == 200
    assert response.json()["args"]["test"] == "pytest"


@pytest.mark.api
def test_httpbin_headers():
    response = requests.get(
        "https://httpbin.org/headers",
        timeout=10,
    )

    response.raise_for_status()

    assert response.status_code == 200
    assert "headers" in response.json()