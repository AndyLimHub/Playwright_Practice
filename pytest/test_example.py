import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.pause()
    page.get_by_text("This is just a demo of").click()
    expect(page.locator("body")).to_contain_text("real TodoMVC app.")
    expect(page.locator("body")).to_contain_text("This is just a demo of TodoMVC for testing, not the real TodoMVC app.")
    expect(page.get_by_role("contentinfo")).to_contain_text("TodoMVC")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("Task")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    expect(page.get_by_text("All Active Completed")).to_be_visible()
