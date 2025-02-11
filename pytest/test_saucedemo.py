from playwright.sync_api import Page

def test_inventory_site(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Perform login
    page.fill("#user-name", "standard_user")  # Username field
    page.fill("#password", "secret_sauce")    # Password field
    page.click("#login-button")               # Click login button

    # Ensure successful login
    assert "inventory.html" in page.url
