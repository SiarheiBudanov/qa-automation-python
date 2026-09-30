from selenium.webdriver.common.by import By


class ExamplePage:
    URL = "https://example.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def title(self):
        return self.driver.title

    def body_text(self):
        return self.driver.find_element(By.TAG_NAME, "body").text