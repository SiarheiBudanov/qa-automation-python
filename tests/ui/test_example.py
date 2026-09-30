import pytest

from pages.example_page import ExamplePage


@pytest.mark.ui
def test_example_title(driver):
    page = ExamplePage(driver)
    page.open()

    assert page.title() == "Example Domain"


@pytest.mark.ui
def test_example_page_content(driver):
    page = ExamplePage(driver)
    page.open()

    body_text = page.body_text()

    assert "This domain is for use in documentation examples" in body_text
    assert "This is not a service" in body_text


@pytest.mark.ui
@pytest.mark.parametrize(
    "url, expected_title",
    [
        ("https://example.com", "Example Domain"),
        ("https://example.org", "Example Domain"),
    ],
)
def test_example_pages_title(driver, url, expected_title):
    driver.get(url)

    assert driver.title == expected_title