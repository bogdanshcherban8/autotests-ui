from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from components.elements.input import Input
import allure

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(page, 'login-form-email-input', "Email input")
        self.password_input = Input(page, 'login-form-password-input', 'Password input')
    @allure.step('Fill login form')
    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)
        self.password_input.fill(password)
        self.password_input.check_have_value(password)

