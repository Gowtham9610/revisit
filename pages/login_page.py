from playwright.sync_api import Page,expect

class Login_Page:
    def __init__(self,page:Page):
        self.page = page

    def navigation(self):
        self.page.goto("https://the-internet.herokuapp.com/login")
    