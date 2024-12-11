from playwright.sync_api import sync_playwright

def test_hans_zimmer():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Change to True for headless mode
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Navigate to Google
        page.goto("https://www.google.com")
        
        # Step 2: Search for "Hans Zimmer"
        page.fill("input[name='q']", "Hans Zimmer")
        page.press("input[name='q']", "Enter")
        
        # Wait for search results to load
        page.wait_for_selector("h3")  # Ensures search results are visible

        # Step 3: Click the first link
        page.click("h3")  # Clicks the first heading (assumes it is the first link)

        # Step 4: Extract text from the page
        page.wait_for_load_state("domcontentloaded")
        page_content = page.content()  # Gets the full HTML content of the page
        print(page_content)  # Print the extracted text

        # Close the browser
        browser.close()

# Run the test
test_hans_zimmer()
