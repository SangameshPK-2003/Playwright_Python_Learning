# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     # Launch browser
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     # Open dropdown page
#     page.goto("https://the-internet.herokuapp.com/dropdown")

#     # Locate dropdown
#     dropdown = page.locator("#dropdown")

#     # Select option using visible text (business-friendly)
#     dropdown.select_option(label="Option 1")

#     # Read the selected visible text
#     selected_text = dropdown.locator("option:checked").inner_text()

#     # REAL ASSERTION
#     # If this condition is false, the test FAILS immediately
#     assert selected_text == "Option 2", "Dropdown selection failed"

#     # Close browser (this line won't run if assertion fails)
#     browser.close()
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    assert False  # force failure

    # browser.close()  # not reached
