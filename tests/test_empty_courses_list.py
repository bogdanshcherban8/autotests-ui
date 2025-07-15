import pytest

from pages.courses_list_page import CoursesListPage
from pages.dashboard_page import DashboardPage
@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(dashboard_page_with_state: DashboardPage, courses_list_page: CoursesListPage):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.check_visible_empty_view()
    courses_list_page.check_visible_courses_title()
    dashboard_page_with_state.navbar.check_visible('TestUser')
    dashboard_page_with_state.sidebar.check_visible()