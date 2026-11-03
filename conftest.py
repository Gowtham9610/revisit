import pytest
from playwright.sync_api import Page
from pages.login_page import Login_Page

@pytest.fixture
def login_page(page:Page):
    return Login_Page(page)

