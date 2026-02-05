from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    # Navigate to checkbox demo page
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Locate all checkboxes on the page
    checkboxes = page.locator("input[type='checkbox']")
    page.wait_for_timeout(3000)

    # Check first checkbox if not already checked
    if not checkboxes.nth(0).is_checked():
        page.wait_for_timeout(3000)
        checkboxes.nth(0).check()
        page.wait_for_timeout(3000)
        print("First checkbox checked")
    else:
        print("First checkbox was already checked")

    # Uncheck second checkbox if it is checked
    if checkboxes.nth(1).is_checked():
        page.wait_for_timeout(3000)
        checkboxes.nth(1).uncheck()
        page.wait_for_timeout(3000)
        print("Second checkbox unchecked")
    else:
        print("Second checkbox was already unchecked")

    page.wait_for_timeout(5000)

    browser.close()
