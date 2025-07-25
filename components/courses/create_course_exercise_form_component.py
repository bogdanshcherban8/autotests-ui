from playwright.sync_api import expect, Page

from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.input import Input
from components.elements.text import Text
import allure

class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.delete_button = Button(
            page, "create-course-exercise-{index}-box-toolbar-delete-exercise-button", 'Delete Exercise'
        )
        self.subtitle = Text(
            page, "create-course-exercise-{index}-box-toolbar-subtitle-text", "Exercise subtitle"
        )
        self.title_input = Input(
            page, "create-course-exercise-form-title-{index}-input", "Exercise title input"
        )
        self.description_input = Input(
            page, "create-course-exercise-form-description-{index}-input", 'Exercise description input'
        )
    def click_delete_button(self, index: int):
        self.delete_button.click(index=index)
    @allure.step("Check visible course exercise form at index '{index}'")
    def check_visible(self, index: int, title: str, description: str):
        self.subtitle.check_visible(index=index)
        self.subtitle.check_have_text(f"#{index + 1} Exercise", index=index)
        self.title_input.check_visible(index=index)
        self.title_input.check_have_value(title, index=index)
        self.description_input.check_visible(index=index)
        self.description_input.check_have_value(description, index=index)

    @allure.step("Fill create course exercise form with '{index}'")
    def fill_create_exercise_form(self, index: int, title: str, description: str):
        self.title_input.fill(title, index=index)
        self.title_input.check_have_value(title, index=index)
        self.description_input.fill(description, index=index)
        self.description_input.check_have_value(description, index=index)
