from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch the browser in visible mode
    browser = p.chromium.launch(headless=False)

    # Create a browser context with a LARGE viewport
    # This simulates a maximized window reliably
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )

    # Open a new page (tab)
    page = context.new_page()

    # Navigate to demo site
    page.goto("https://the-internet.herokuapp.com/inputs")

    # Locate input field
    input_box = page.locator("input")

    # Enter text
    input_box.fill("1818181818")

    # Wait so you can see it clearly
    page.wait_for_timeout(5000)

    print("Viewport set to 1920x1080 (Playwright-style maximize)")
    print("This is the DAY 2 OF LEARNING PLAYWRIGHT")
    print("VIRAT KOHLI IS THE KNG OF THE CRICKET")

    # Close browser
    browser.close()
