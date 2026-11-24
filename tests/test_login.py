import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.json_reader import read_json

def test_valid_login(page: Page):

    login_page = LoginPage(page)
    valid_user = login_data["valid_login"]

    login_page.navigate()

    login_page.login(
        valid_user["username"],
        valid_user["password"]
    )

    expect(page.get_by_text("Products", exact=True)).to_be_visible()

login_data = read_json("login_data.json")
@pytest.mark.login
@pytest.mark.parametrize(
    "test_data",
    login_data["invalid_login"]
)
def test_invalid_login(page: Page, test_data):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    expect(login_page.error_message).to_contain_text(
        test_data["expected_error"]
    )