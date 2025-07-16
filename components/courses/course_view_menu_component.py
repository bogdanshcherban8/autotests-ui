from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.elements.button import Button
class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.menu_button = Button(page, 'course-view-menu-button', 'Menu')
        self.menu_edit_button = Button(page, 'course-view-edit-menu-item', 'Edit')
        self.menu_delete_button = Button(page, 'course-view-delete-menu-item', 'Delete')
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)
        self.menu_edit_button.check_visible(nth=index)
        self.menu_edit_button.click(nth=index)

    def clock_delete(self, index: int):
        self.menu_button.click(nth=index)
        self.menu_delete_button.check_visible(nth=index)
        self.menu_delete_button.click(nth=index)