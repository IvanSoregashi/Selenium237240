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

def test_guest_cant_see_product_in_basket_opened_from_main_page(main_page):
    main_page.open()
    main_page.to_the_cart_page()
    from pages.cart_page import CartPage
    cart_page = CartPage(main_page.browser)
    assert cart_page.cart_content().text == "Your basket is empty. Continue shopping"
    assert cart_page.get_cart_items() == []

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, main_page):
        main_page.open()
        login_page = main_page.go_to_login_page()
        assert login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, main_page):
        main_page.open()
        assert main_page.should_be_login_link(), "Login link is not presented"
