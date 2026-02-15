class BaseTest:
    """
    Base class for all test classes.
    Can contain shared utilities, common assertions,
    and reusable setup logic in future.
    """

    def get_page(self, page):
        """
        Provides Playwright page instance to child tests.
        """
        return page
