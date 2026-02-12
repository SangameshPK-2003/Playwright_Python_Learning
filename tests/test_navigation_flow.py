from pages.checkbox_page import CheckboxPage


def test_navigation_checkbox_to_dropdown(page):
    """
    Verify navigation from Checkboxes page to Dropdown page works correctly.
    """

    checkbox_page = CheckboxPage(page)

    # Load first page
    checkbox_page.load()

    # Navigate to dropdown page
    dropdown_page = checkbox_page.go_to_dropdown_page()

    # Verify dropdown page loaded by checking title
    assert dropdown_page.get_selected_text() is not None

