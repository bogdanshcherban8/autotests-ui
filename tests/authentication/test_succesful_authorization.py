import pytest, re
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from pages.authentication.login_page import LoginPage
from playwright.sync_api import expect

users = {'email': 'alienwieser@gmail.com', 'username': 'TestUser', 'password': 'kaban'}
@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize('user_form', [users])
class TestSuccessfulReg:

    def test_successful_reg(self, registration_page: RegistrationPage, user_form: dict, login_page: LoginPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        registration_page.click_reg_link()
        registration_page.registration_form_component.fill(
            user_form['email'], user_form['username'], user_form['password']
        )
        registration_page.click_reg_button()

        # ожидание перехода
        expect(registration_page.page).to_have_url(re.compile(r".*/dashboard.*"), timeout=10000)

        dashboard_page = DashboardPage(registration_page.page)
        dashboard_page.navbar.check_visible(user_form['username'])
        dashboard_page.check_reg_dashboard_title()
        dashboard_page.check_reg_dashboard_students_chart()
        dashboard_page.check_reg_dashboard_courses_chart()
        dashboard_page.check_reg_dashboard_scores_chart()
        dashboard_page.check_reg_dashboard_activities_chart()
        dashboard_page.sidebar.check_visible()

        registration_page.click_reg_logout()

        login_page.login_form_component.fill_login_form(
            email=user_form['email'],
            password=user_form['password']
        )
        login_page.click_login_button()
