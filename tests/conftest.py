import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    """
    PyTest Fixture:
    - Runs BEFORE each test
    - Provides a ready-to-use Playwright page
    - Automatically closes browser AFTER test
    """

    # Start Playwright
    playwright = sync_playwright().start()

    # Launch browser
    browser = playwright.chromium.launch(headless=False)

    # Create new context and page
    context = browser.new_context()
    page = context.new_page()

    # Provide page to the test
    yield page

    # --- Teardown (runs after test finishes) ---
    browser.close()
    playwright.stop()
