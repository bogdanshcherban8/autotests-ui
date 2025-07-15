from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.menu_edit_button = page.get_by_test_id('course-view-edit-menu-item')
        self.menu_delete_button = page.get_by_test_id('course-view-delete-menu-item')
    def click_edit(self, index: int):
        self.menu_button.nth(index).click()
        expect(self.menu_edit_button.nth(index)).to_be_visible()
        self.menu_edit_button.nth(index).click()

    def clock_delete(self, index: int):
        self.menu_button.nth(index).click()
        expect(self.menu_delete_button.nth(index)).to_be_clickable()
        self.menu_delete_button.nth(index).click()