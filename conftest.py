import os

import logging
import os

import pytest
from selenium import webdriver

from clients.posts_api import PostsApi


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()


@pytest.fixture
def posts_api():
    api = PostsApi()

    yield api

    api.close()