from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Click Add Element
    page.get_by_text("Add Element").click()

    # Locate Delete button
    delete_button = page.get_by_text("Delete")

    # Assert visibility
    assert delete_button.is_visible(), "Delete button should be visible after clicking Add Element"

    browser.close()
