import pytest


@pytest.mark.smoke
def test_example_title(driver):
    driver.get("https://example.com")
    assert driver.title == "Example Domain"


def test_example_page_heading(driver):
    driver.get("https://example.com")
    assert driver.find_element("tag name", "h1").text == "Example Domain"