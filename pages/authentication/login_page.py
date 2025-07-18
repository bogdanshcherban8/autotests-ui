from components.authentication.login_form_component import LoginFormComponent
from components.elements.link import Link
from components.elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.elements.button import Button
import allure
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_form_component = LoginFormComponent(page)
        self.login_button = Button(page, 'login-page-login-button', "Login")
        self.reg_link = Link(page, 'login-page-registration-link', "Registration")
        self.wrong_email_or_password_alert = Text(page, 'login-page-wrong-email-or-password-alert', "Wrong email or password")

    def click_login_button(self):
        self.login_button.click()
    def click_registration_link(self):
        self.reg_link.click()
    @allure.step('Check wrong email or password alert')
    def check_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")