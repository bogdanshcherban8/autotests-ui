import allure

class BasePage:
    def __init__(self, page):
        self.page = page
    def visit(self, url:str):
        with allure.step(f"Opening the url {url}"):
            self.page.goto(url, wait_until="networkidle")
    def reload(self):
        with allure.step(f"Reloading the page{self.page.url}"):
            self.page.reload(wait_until="networkidle")