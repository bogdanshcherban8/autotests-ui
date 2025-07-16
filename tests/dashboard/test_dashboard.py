from pages.dashboard.dashboard_page import DashboardPage
import pytest
@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page_with_state.navbar.check_visible('TestUser')
        dashboard_page_with_state.check_reg_dashboard_title()
        dashboard_page_with_state.check_reg_dashboard_students_chart()
        dashboard_page_with_state.check_reg_dashboard_courses_chart()
        dashboard_page_with_state.check_reg_dashboard_scores_chart()
        dashboard_page_with_state.check_reg_dashboard_activities_chart()
        dashboard_page_with_state.sidebar.check_visible()