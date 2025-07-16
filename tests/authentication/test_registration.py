import pytest

from pages.authentication.registration_page import RegistrationPage

users = {'email': 'alienwieser@gmail.com', 'username': 'bogdan', 'password': 'kaban'}
@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    @pytest.mark.parametrize('user_form', [users])
    def test_successful_registration(self, registration_page: RegistrationPage, user_form: dict):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        registration_page.click_reg_link()
        registration_page.registration_form_component.fill(user_form['email'], user_form['username'], user_form['password'])
        registration_page.click_reg_button()

