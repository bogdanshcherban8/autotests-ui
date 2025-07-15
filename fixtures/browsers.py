import pytest
from playwright.sync_api import Playwright, Page, expect


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


from playwright.sync_api import Playwright, expect
import pytest
import time


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    page.get_by_test_id("login-page-registration-link").click()

    unique_email = f"test_{int(time.time())}@example.com"

    page.get_by_test_id("registration-form-email-input").locator("input").fill(unique_email)
    page.get_by_test_id("registration-form-username-input").locator("input").fill("TestUser")
    page.get_by_test_id("registration-form-password-input").locator("input").fill("TestPassword123")

    register_button = page.get_by_test_id("registration-page-registration-button")
    expect(register_button).to_be_visible()
    expect(register_button).to_be_enabled()

    register_button.click()

    page.wait_for_url("**/dashboard", timeout=10000)

    context.storage_state(path="new-browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="new-browser-state.json")
    yield context.new_page()
