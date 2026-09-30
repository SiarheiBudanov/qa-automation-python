import os


ENVIRONMENT = os.getenv("TEST_ENV", "dev")

BASE_URLS = {
    "dev": "https://jsonplaceholder.typicode.com",
    "stage": "https://jsonplaceholder.typicode.com",
}


BASE_URL = BASE_URLS[ENVIRONMENT]