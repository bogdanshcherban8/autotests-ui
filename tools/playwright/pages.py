import allure
import re
from playwright.sync_api import Page, Playwright
from config import settings, Browser
from tools.playwright.mock import mock_status_resources


def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def initialize_playwright_pages(playwright: Playwright, taste_name: str, browser_type: Browser, storage_state: str = None) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(storage_state=storage_state, record_video_dir=settings.videos_dir,
                                  base_url=settings.get_base_url())
    context.tracing.start(screenshots=False, snapshots=True, sources=True)
    page = context.new_page()
    mock_status_resources(page)
    yield page
    filename = sanitize_filename(taste_name)

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{filename}.zip'))
    browser.close()
    allure.attach.file(settings.tracing_dir.joinpath(f'{filename}.zip'), name='tracing', extension="zip")
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
