import pytest
from config import settings
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from pages.authentication.registration_page import RegistrationPage
import allure

from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    @allure.title('Another successful registration')
    def test_successful_registration(self, registration_page: RegistrationPage):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.registration_form_component.fill(email=settings.test_user.email,
                                                           username=settings.test_user.username,
                                                           password=settings.test_user.password)
        registration_page.click_reg_button()
