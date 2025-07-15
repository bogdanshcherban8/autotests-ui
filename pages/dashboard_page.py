from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

        self.dashboard_students_chart = page.get_by_test_id('students-bar-chart')
        self.dashboard_students_title = page.get_by_test_id('students-widget-title-text')

        self.dashboard_courses_chart = page.get_by_test_id('courses-pie-chart')
        self.dashboard_courses_title = page.get_by_test_id('courses-widget-title-text')

        self.dashboard_activities_chart = page.get_by_test_id('activities-line-chart')
        self.dashboard_activities_title = page.get_by_test_id('activities-widget-title-text')

        self.dashboard_scores_chart = page.get_by_test_id('scores-scatter-chart')
        self.dashboard_scores_title = page.get_by_test_id('scores-widget-title-text')
    def check_reg_dashboard_title(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')

    def check_reg_dashboard_students_chart(self):
        expect(self.dashboard_students_title).to_be_visible()
        expect(self.dashboard_students_title).to_have_text('Students')
        expect(self.dashboard_students_chart).to_be_visible()

    def check_reg_dashboard_courses_chart(self):
        expect(self.dashboard_courses_title).to_be_visible()
        expect(self.dashboard_courses_title).to_have_text('Courses')
        expect(self.dashboard_courses_chart).to_be_visible()

    def check_reg_dashboard_activities_chart(self):
        expect(self.dashboard_activities_title).to_be_visible()
        expect(self.dashboard_activities_title).to_have_text('Activities')
        expect(self.dashboard_activities_chart).to_be_visible()

    def check_reg_dashboard_scores_chart(self):
        expect(self.dashboard_scores_title).to_be_visible()
        expect(self.dashboard_scores_title).to_have_text('Scores')
        expect(self.dashboard_scores_chart).to_be_visible()