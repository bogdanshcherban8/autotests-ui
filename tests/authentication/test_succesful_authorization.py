import pytest, re

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from pages.authentication.login_page import LoginPage
from playwright.sync_api import expect
import allure
from allure_commons.types import Severity

from tools.routes import AppRoute

@pytest.mark.regression
@pytest.mark.registration
@allure.severity(Severity.BLOCKER)
class TestSuccessfulReg:
    @allure.title('Successful registration with dashboard and login check')
    def test_successful_reg(self, registration_page: RegistrationPage, login_page: LoginPage):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.registration_form_component.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_reg_button()

        expect(registration_page.page).to_have_url(re.compile(r".*/dashboard.*"), timeout=10000)

        dashboard_page = DashboardPage(registration_page.page)
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.check_reg_dashboard_title()
        dashboard_page.check_reg_dashboard_students_chart()
        dashboard_page.check_reg_dashboard_courses_chart()
        dashboard_page.check_reg_dashboard_scores_chart()
        dashboard_page.check_reg_dashboard_activities_chart()
        dashboard_page.sidebar.check_visible()

        registration_page.click_reg_logout()

        login_page.login_form_component.fill_login_form(
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        login_page.click_login_button()
