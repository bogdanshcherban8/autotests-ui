from playwright.sync_api import Playwright, Page
import pytest
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from config import settings
import re

from tools.playwright.pages import initialize_playwright_pages
from tools.routes import AppRoute


def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', name)

@pytest.fixture(params=settings.browsers)
def page(playwright: Playwright, request: SubRequest) -> Page:
    yield from initialize_playwright_pages(playwright, taste_name=request.node.name, browser_type=request.param)


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form_component.fill(email=settings.test_user.email, username=settings.test_user.username,
                                                       password=settings.test_user.password)
    registration_page.click_reg_button()
    context.storage_state(path=settings.browser_state_file)
    browser.close()

@pytest.fixture(params=settings.browsers)
def page_with_state(initialize_browser_state, playwright: Playwright, request: SubRequest) -> Page:
    yield from initialize_playwright_pages(playwright, taste_name=request.node.name,
                                           storage_state=settings.browser_state_file, browser_type=request.param)