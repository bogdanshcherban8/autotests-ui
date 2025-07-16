from components.authentication.registration_form_component import RegistrationFormComponent
from components.elements.button import Button
from components.elements.input import Input
from components.elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page
class RegistrationPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(page)
        self.reg_link = Link(page, 'login-page-registration-link', "Registration")
        self.reg_button = Button(page,'registration-page-registration-button', "Registration button")
        self.reg_logout = Button(page,'logout-drawer-list-item-button', "Registration logout")
        self.reg_empty_email = Input(page, "registration-form-email-input", "Email")
        self.reg_empty_username = Input(page, "registration-form-username-input", "Username")
        self.reg_empty_password = Input(page, "registration-form-password-input", "Password")
    def click_reg_link(self):
        self.reg_link.click()
    def click_reg_button(self):
        self.reg_button.click()
    def click_reg_logout(self):
        self.reg_logout.click()
    def check_form(self):
        self.reg_empty_email.check_visible()
        self.reg_empty_username.check_visible()
        self.reg_empty_password.check_visible()