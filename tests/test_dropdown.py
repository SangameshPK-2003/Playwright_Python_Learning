import pytest
from pages.dropdown_page import DropdownPage


@pytest.mark.parametrize("option_text", ["Option 1", "Option 2"])
def test_dropdown_selection(page, option_text):
    """
    Verify dropdown selection works for multiple options.
    """

    dropdown_page = DropdownPage(page)

    dropdown_page.load()
    dropdown_page.select_option(option_text)

    assert dropdown_page.is_option_selected(option_text)


    
def test_page_title(page):
    """
    Verify the page title is correct.
    Demonstrates multiple tests using same fixture.
    """

    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Assertion on page title
    assert "The Internet" in page.title()
