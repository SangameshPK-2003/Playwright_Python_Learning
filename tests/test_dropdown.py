from pages.dropdown_page import DropdownPage

def test_dropdown_selection(page):
    """
    Verify dropdown selection using Page Object Model.
    """

    dropdown_page = DropdownPage(page)

    dropdown_page.load()
    dropdown_page.select_option("Option 1")

    assert dropdown_page.is_option_selected("Option 1")


    
def test_page_title(page):
    """
    Verify the page title is correct.
    Demonstrates multiple tests using same fixture.
    """

    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Assertion on page title
    assert "The Internet" in page.title()
