from pages.checkbox_page import CheckboxPage


def test_first_checkbox(page):
    """
    Verify first checkbox can be checked.
    """

    checkbox_page = CheckboxPage(page)

    checkbox_page.load()
    checkbox_page.check_first_checkbox()

    assert checkbox_page.is_first_checkbox_checked()
