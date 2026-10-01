from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ExamplePage:
    URL = "https://example.com"
    BODY = (By.TAG_NAME, "body")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

        self.wait.until(
            EC.presence_of_element_located(self.BODY)
        )

        return self

    @property
    def title(self):
        return self.driver.title

    @property
    def body_text(self):
        return self.driver.find_element(*self.BODY).text

    @property
    def current_url(self):
        return self.driver.current_url

    def is_loaded(self):
        return self.current_url.startswith(self.URL)

    def has_expected_content(self):
        return (
            "This domain is for use in documentation examples"
            in self.body_text
        )