import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    new_user_reg = page.get_by_test_id('login-page-registration-link')
    new_user_reg.click()
    new_user_email = page.get_by_test_id('registration-form-email-input').locator('input')
    new_user_email.fill('test_email@gmail.com')
    new_user_name = page.get_by_test_id('registration-form-username-input').locator('input')
    new_user_name.fill('test_username')
    new_user_password = page.get_by_test_id('registration-form-password-input').locator('input')
    new_user_password.fill('PASSWORD')
    new_user_log = page.get_by_test_id('registration-page-login-link')
    new_user_log.click()
    context.storage_state(path='new-browser-state.json')
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="new-browser-state.json")
    yield context.new_page()
    browser.close()