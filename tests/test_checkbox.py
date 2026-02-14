from pages.checkbox_page import CheckboxPage


def test_first_checkbox_behavior(page):
    """
    Verify checkbox state changes correctly after user action.
    """

    checkbox_page = CheckboxPage(page)

    # Load page
    checkbox_page.load()

    # Initial state should be unchecked
    assert not checkbox_page.is_first_checkbox_checked()

    # Perform user action
    checkbox_page.check_first_checkbox()

    # Final state should be checked
    assert checkbox_page.is_first_checkbox_checked()
