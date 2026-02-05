from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to Add/Remove Elements page
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Locate all existing "Delete" buttons
    delete_buttons = page.get_by_text("Delete")

    # Count how many Delete buttons are present BEFORE clicking
    initial_count = delete_buttons.count()
    print(f"Delete buttons before click: {initial_count}")
    page.wait_for_timeout(5000)

    # Click "Add Element"
    page.get_by_text("Add Element").click()

    # Count Delete buttons AFTER clicking
    new_count = delete_buttons.count()
    print(f"Delete buttons after click: {new_count}")

    # Assertion: number of Delete buttons should increase by 1
    if new_count == initial_count + 1:
        print("PASS: Delete button count increased by 1")
    else:
        print("FAIL: Delete button count did not increase correctly")

    page.wait_for_timeout(5000)
    browser.close()
