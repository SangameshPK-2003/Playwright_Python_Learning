from pages.dropdown_page import DropdownPage
class CheckboxPage:
    """
    Page Object for the Checkboxes page.
    Contains locators and reusable actions.
    """

    def __init__(self, page):
        self.page = page
        self.checkboxes = page.locator("input[type='checkbox']")

    def load(self):
        """Navigate to checkboxes page."""
        self.page.goto("https://the-internet.herokuapp.com/checkboxes", timeout=60000)

    def check_first_checkbox(self):
        """Ensure first checkbox is checked."""
        if not self.checkboxes.nth(0).is_checked():
            self.checkboxes.nth(0).check()

    def is_first_checkbox_checked(self):
        """Return True if first checkbox is checked."""
        return self.checkboxes.nth(0).is_checked()
    
    def go_to_dropdown_page(self):
        """
        Navigate from Checkboxes page to Dropdown page.
        Returns a new DropdownPage object.
        """
        self.page.goto("https://the-internet.herokuapp.com/dropdown", timeout=60000)
        return DropdownPage(self.page)
    



