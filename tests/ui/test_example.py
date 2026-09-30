import pytest

from pages.example_page import ExamplePage


@pytest.mark.ui
def test_example_title(driver):
    page = ExamplePage(driver).open()

    assert page.title == "Example Domain"


@pytest.mark.ui
def test_example_page_content(driver):
    page = ExamplePage(driver).open()

    assert page.has_expected_content()


@pytest.mark.ui
def test_example_page_is_loaded(driver):
    page = ExamplePage(driver).open()

    assert page.is_loaded()


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