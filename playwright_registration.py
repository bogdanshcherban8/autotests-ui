from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    reg_link = page.get_by_test_id('login-page-registration-link')
    reg_link.click()
    reg_email = page.get_by_test_id('registration-form-email-input').locator("input")
    reg_email.fill('alienwieser@gmail.com')
    reg_password = page.get_by_test_id('registration-form-password-input').locator("input")
    reg_password.fill('bogdan')
    reg_username = page.get_by_test_id('registration-form-username-input').locator("input")
    reg_username.fill('kaban')
    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()
    context.storage_state(path = 'browser-state.json')
    logout_button = page.get_by_test_id('logout-drawer-list-item-button')
    logout_button.click()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(5000)