def test_dropdown_selection(page):
    """
    Test Case:
    Verify user can select Option 1 from dropdown
    """

    # Navigate to dropdown page
    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Locate dropdown and select option
    dropdown = page.locator("#dropdown")
    dropdown.select_option(label="Option 1")

    # Get selected text
    selected_text = dropdown.locator("option:checked").inner_text()

    # Assertion
    assert selected_text == "Option 1", "Dropdown selection failed"
    
def test_page_title(page):
    """
    Verify the page title is correct.
    Demonstrates multiple tests using same fixture.
    """

    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Assertion on page title
    assert "The Internet" in page.title()
