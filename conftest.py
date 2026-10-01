import logging
import os

import pytest
from selenium import webdriver

from clients.posts_api import PostsApi


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


def create_browser(browser_name):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        if os.getenv("CI") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(options=options)

    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()

        if os.getenv("CI") == "true":
            options.add_argument("-headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        return webdriver.Firefox(options=options)

    if browser_name == "edge":
        options = webdriver.EdgeOptions()

        if os.getenv("CI") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        return webdriver.Edge(options=options)

    raise ValueError(f"Unsupported browser: {browser_name}")


@pytest.fixture
def driver():
    browser_name = os.getenv("BROWSER", "chrome")
    browser = create_browser(browser_name)

    yield browser

    browser.quit()

@pytest.fixture
def posts_api():
    api = PostsApi()

    yield api

    api.close()