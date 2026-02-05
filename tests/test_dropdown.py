from utils.browser_setup import launch_browser

def test_dropdown_selection():
    """
    Test Case:
    Verify user can select Option 1 from dropdown
    """

    # Setup browser
    playwright, browser, context, page = launch_browser()

    # Test steps
    page.goto("https://the-internet.herokuapp.com/dropdown")

    dropdown = page.locator("#dropdown")
    dropdown.select_option(label="Option 1")

    selected_text = dropdown.locator("option:checked").inner_text()

    # Assertion (real test behavior)
    assert selected_text == "Option 1", "Dropdown selection failed"

    # Cleanup
    browser.close()
    playwright.stop()


# Call test manually (temporary)
# test_dropdown_selection()
