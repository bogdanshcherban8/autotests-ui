from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
from playwright.sync_api import Page
import re
import allure

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')
    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.logout_list_item.check_visible("Logout")
        self.courses_list_item.check_visible("Courses")
        self.dashboard_list_item.check_visible("Dashboard")

    @allure.step('Click logout sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step('Click course sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step('Click dashboard sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))
