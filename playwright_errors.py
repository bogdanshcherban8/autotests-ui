from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    #unknown = page.locator('#unkown')
    #expect(unknown).to_be_visible()
    login_button = page.get_by_test_id('login-page-login-button')
    login_button.fill('unknown')
    page.wait_for_timeout(5000)