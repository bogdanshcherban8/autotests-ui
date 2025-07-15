
import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

users = {'user.name@gmail.com': 'password', 'User.name@gmail.com': '  ', '  ': 'password'}
@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('user_form', users.keys(),
                         ids=lambda user_form: f'{user_form}: {users[user_form]}')
def test_wrong_email_or_password_authorization(login_page: LoginPage, user_form: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(user_form, user_form)
    login_page.click_login_button()
    login_page.check_wrong_email_or_password_alert()


