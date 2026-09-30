from pathlib import Path

import pytest
from selenium import webdriver


SCREENSHOTS_DIR = Path("reports") / "screenshots"


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")

    if driver is None:
        return

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    safe_name = (
        report.nodeid
        .replace("::", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .replace("[", "_")
        .replace("]", "_")
    )

    screenshot_path = SCREENSHOTS_DIR / f"{safe_name}.png"
    driver.save_screenshot(str(screenshot_path))
    print(f"\nScreenshot saved: {screenshot_path}")