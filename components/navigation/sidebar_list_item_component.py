from re import Pattern

from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.elements.button import Button
from components.elements.icon import Icon
from components.elements.text import Text
import allure

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', "Icon")
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text',"Title")
        self.button = Button(page, f'{identifier}-drawer-list-item-button', "Button")
    @allure.step('Check sidebar list with title "{title}"')
    def check_visible(self, title:str):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)