from playwright.sync_api import Page, expect

from components.courses.CreateCourseToolbarViewComponent import CreateCourseToolbarViewComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_course_exercise = CreateCourseExerciseFormComponent(page)
        self.create_course_form_component = CreateCourseFormComponent(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)
        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.create_course_description_textarea = (
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def check_visible_exercises_title(self):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

    def check_visible_create_exercise_button(self):
        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(title='There is no exercises',
                                                description='Click on "Create exercise" button to create new exercise')

