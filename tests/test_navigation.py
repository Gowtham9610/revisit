from playwright.sync_api import Page,expect

def test_page_navigation(login_page,page:Page):
    login_page.navigation()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
