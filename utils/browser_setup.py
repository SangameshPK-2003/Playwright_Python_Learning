from playwright.sync_api import sync_playwright

def launch_browser():
    """
    Launches browser and returns:
    - playwright instance
    - browser
    - context
    - page

    Centralizing browser setup avoids repetition.
    """

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    return playwright, browser, context, page
