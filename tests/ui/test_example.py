import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_example_title(driver):
    driver.get("https://example.com")

    assert driver.title == "Example Domain"


def test_example_page_content(driver):
    driver.get("https://example.com")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    body_text = driver.find_element(By.TAG_NAME, "body").text

    assert "This domain is for use in documentation examples" in body_text
    assert "This is not a service" in body_text


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