import time

import pytest

from pages.main_page import MainPage, By

@pytest.fixture
def main_page(browser):
    return MainPage(browser)

def test_guest_can_go_to_login_page(main_page):
    main_page.open()
    login_page = main_page.go_to_login_page()
    assert login_page.should_be_login_page()

@pytest.mark.xfail
def test_login_link(main_page):
    assert main_page.should_be_login_link(), "Login link is not presented"

