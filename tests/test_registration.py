from playwright.sync_api import Page, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    reg_link = chromium_page.get_by_test_id('login-page-registration-link')
    reg_link.click()
    reg_email = chromium_page.get_by_test_id('registration-form-email-input').locator("input")
    reg_email.fill('alienwieser@gmail.com')
    reg_password = chromium_page.get_by_test_id('registration-form-password-input').locator("input")
    reg_password.fill('bogdan')
    reg_username = chromium_page.get_by_test_id('registration-form-username-input').locator("input")
    reg_username.fill('kaban')
    reg_button = chromium_page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    reg_check_dashboard = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(reg_check_dashboard).to_be_visible()
