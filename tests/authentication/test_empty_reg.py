import pytest, re
from pages.authentication.registration_page import RegistrationPage
import allure

from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
class TestEmptyReg:
    @allure.title('Successful registration')
    def test_successful_reg(self, registration_page: RegistrationPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.check_form()
