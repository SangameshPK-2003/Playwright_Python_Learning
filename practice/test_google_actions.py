from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch visible Chromium browser
    browser = p.chromium.launch(headless=False)

    # Create a fresh browser context (new user session)
    context = browser.new_context(viewport=None)

    # Open a new tab
    page = context.new_page()

    # Navigate to Google
    page.goto("https://www.google.com")

    # Wait until DOM is loaded (HTML ready)
    page.wait_for_load_state("domcontentloaded")

    # ---- IMPORTANT PART STARTS HERE ----

    # Google search box has name="q"
    # We explicitly wait for it to be VISIBLE
    search_box = page.locator("input[name='q']").first

    # Wait until the search box is visible and ready
    search_box.wait_for(state="visible", timeout=30000)

    # Fill text into the search box
    search_box.fill("Playwright Python automation")

    # Press Enter to search
    page.keyboard.press("Enter")

    # Wait so we can visually confirm results
    page.wait_for_timeout(5000)

    # Print page title to verify navigation
    print("Page title is:", page.title())

    # Close browser
    browser.close()
