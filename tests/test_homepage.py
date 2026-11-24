import  pytest
from playwright.sync_api import Page, expect


def test_homepage_load(page : Page):

    page.goto("/")

    expect(page).to_have_title("Swag Labs")

    expect(page.get_by_placeholder("Username")).to_be_visible()

    expect(page.get_by_placeholder("Password")).to_be_visible()

    expect(page.get_by_role("button", name = "Login")).to_be_visible()