from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure

from components.elements.icon import Icon
from components.elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier:str):
        super().__init__(page)
        self.icon = Icon(page, f'{identifier}-empty-view-icon', "Icon")
        self.title = Text(page, f'{identifier}-empty-view-title-text', "Title")
        self.description = Text(page, f'{identifier}-empty-view-description-text', "Description")
    @allure.step('Check visible empty view "{title}"')
    def check_visible(self, title: str, description: str):
        expect(self.icon.get_locator()).to_be_visible()
        expect(self.title.get_locator()).to_be_visible()
        expect(self.title.get_locator()).to_have_text(title)
        expect(self.description.get_locator()).to_be_visible()
        expect(self.description.get_locator()).to_have_text(description)
