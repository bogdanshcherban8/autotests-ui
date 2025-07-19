from config import settings
from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    @allure.title('Checking dashboard')
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible(username=settings.test_user.username)
        dashboard_page_with_state.check_reg_dashboard_title()
        dashboard_page_with_state.check_reg_dashboard_students_chart()
        dashboard_page_with_state.check_reg_dashboard_courses_chart()
        dashboard_page_with_state.check_reg_dashboard_scores_chart()
        dashboard_page_with_state.check_reg_dashboard_activities_chart()
        dashboard_page_with_state.sidebar.check_visible()