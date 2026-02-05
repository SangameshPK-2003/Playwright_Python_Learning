from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch browser visibly
    browser = p.chromium.launch(headless=False)

    # Create a normal browser context (no viewport config)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to dropdown demo page
    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Locate the dropdown
    dropdown = page.locator("#dropdown")

    # Select option by visible text
    dropdown.select_option(label="Option 1")

    # 🔑 CORRECT assertion for dropdowns
    # Read the currently selected value
    selected_value = dropdown.input_value()

    # Verify expected value
    if selected_value == "1":
        print("PASS: Option 1 is selected")
    else:
        print("FAIL: Option 1 is NOT selected")

    # Pause for observation
    page.wait_for_timeout(3000)

    browser.close()
