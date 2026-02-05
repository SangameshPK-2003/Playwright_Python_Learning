from playwright.sync_api import sync_playwright


def select_dropdown_and_verify(page, dropdown_selector, option_label):
    dropdown = page.locator(dropdown_selector)
    dropdown.select_option(label=option_label)

    selected_value = dropdown.input_value()
    selected_text = dropdown.locator("option:checked").inner_text()

    if selected_text == option_label:
        print(f"PASS: '{option_label}' is selected (value = {selected_value})")
    else:
        print(f"FAIL: Expected '{option_label}', found '{selected_text}'")
        

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/dropdown")

    select_dropdown_and_verify(page, "#dropdown", "Option 1")
    browser.close()