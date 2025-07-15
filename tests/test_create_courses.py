import pytest

from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage
from pages.dashboard_page import DashboardPage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form("", "", "", "0", "0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    image_path = "./testdata/files/image.png"
    create_course_page.image_upload_widget.upload_preview_image(image_path)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    course_data = {
        "title": "Playwright",
        "estimated_time": "2 weeks",
        "description": "Playwright",
        "max_score": "100",
        "min_score": "10"
    }
    create_course_page.fill_create_course_form(**course_data)

    create_course_page.click_create_course_button()

    courses_list_page = CoursesListPage(create_course_page.page)

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title=course_data["title"],
        max_score=course_data["max_score"],
        min_score=course_data["min_score"],
        estimated_time=course_data["estimated_time"]
    )


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(dashboard_page_with_state: DashboardPage, courses_list_page: CoursesListPage):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.check_visible_empty_view()
    courses_list_page.toolbar_view.check_visible()
    dashboard_page_with_state.navbar.check_visible('TestUser')
    dashboard_page_with_state.sidebar.check_visible()
