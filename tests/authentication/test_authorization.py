import allure
import pytest
from allure_commons.types import Severity
from tools.allure.features import AllureFeature
from tools.allure.tags import AllureTags
from pages.authentication.login_page import LoginPage
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.routes import AppRoute

users = {'user.name@gmail.com': 'password', 'User.name@gmail.com': '  ', '  ': 'password'}
@pytest.mark.regression
@pytest.mark.authorization
@allure.severity(Severity.CRITICAL)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.tag(AllureTags.AUTHORIZATION, AllureTags.REGRESSIONS)
@pytest.mark.parametrize('user_form', users.keys(),
                         ids=lambda user_form: f'{user_form}: {users[user_form]}')
class TestAuthorization:
    @allure.title('User login with wrong email or password')
    def test_wrong_email_or_password_authorization(self,login_page: LoginPage, user_form: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form_component.fill_login_form(user_form, user_form)
        login_page.click_login_button()
        login_page.check_wrong_email_or_password_alert()