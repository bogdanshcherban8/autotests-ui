import pytest, re
from pages.authentication.registration_page import RegistrationPage

@pytest.mark.regression
@pytest.mark.registration
class TestEmptyReg:
    def test_successful_reg(self, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        registration_page.click_reg_link()
        registration_page.check_form()
