from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from components.elements.button import Button
from components.elements.text import Text


class CreateCourseToolbarViewComponent (BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_course_title = Text(page,'create-course-toolbar-title-text', "Title")
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', "Create Course")

    def check_visible(self, is_create_course_disabled: bool = True):
        self.create_course_title.check_visible()
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()
        else:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()