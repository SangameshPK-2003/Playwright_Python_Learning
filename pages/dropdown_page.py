class DropdownPage:
    """
    Page Object representing the Dropdown page.
    Contains locators and page actions.
    """

    def __init__(self, page):
        # Store Playwright page instance
        self.page = page

        # Define locator once
        self.dropdown = page.locator("#dropdown")

    def load(self):
        """Navigate to dropdown page with higher timeout for slow network."""
        self.page.goto(
        "https://the-internet.herokuapp.com/dropdown",
        timeout=60000  # wait up to 60 seconds instead of 30
    )
    


    def select_option(self, option_text):
        """
        Select an option from dropdown after ensuring it is visible.
        """

        # Wait until dropdown is visible (prevents flaky timing failures)
        self.page.wait_for_selector("#dropdown", state="visible")

        # Perform selection
        self.page.select_option("#dropdown", label=option_text)

    def get_selected_text(self):
        """Return selected option text."""
        return self.dropdown.locator("option:checked").inner_text()
    
    def is_option_selected(self, expected_text):
        """
        Reusable verification helper.
        Returns True if expected option is selected, else False.
        """
        actual_text = self.get_selected_text()
        return actual_text == expected_text

