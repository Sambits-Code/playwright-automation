from playwright.sync_api import sync_playwright

def open_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto("https://www.cibc.com/en/personal-banking.html")
        page.keyboard.press("F11")
        page.wait_for_timeout(5000)
        #page.locator("textarea[name='q']").fill("Talent500 CIBC")
        #page.keyboard.press("Enter")
        #page.wait_for_timeout(10000)
        print("Page title:", page.title())
        browser.close()

if __name__ == "__main__":
    open_google()