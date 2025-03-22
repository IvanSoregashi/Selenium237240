import pytest

from pages.product_page import ProductPage

#@pytest.fixture(scope="function", params=[0,
#                                          1,
#                                          2,
#                                          3,
#                                          4,
#                                          5,
#                                          6,
#                                          pytest.param(7, marks=pytest.mark.xfail),
#                                          8,
#                                          9])
#def product_page(browser, request):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{request.param}"
#    return ProductPage(browser, link)

@pytest.fixture
def product_page(browser):
    return ProductPage(browser)

def test_guest_can_add_product_to_basket(product_page):
    product_page.open()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    assert product_page.product_added_alert_is_there()
    item_name = product_page.get_product_name()
    message = product_page.get_product_name_from_alert()
    assert f"{item_name} has been added to your basket." == message, "name not in message"
    items_price = product_page.get_items_price()
    carts_amount = product_page.get_basket_total_price()
    assert items_price == carts_amount, "price of product differs from cart's amount"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(product_page):
    product_page.open()
    product_page.add_product_to_cart()
    assert product_page.is_not_element_present(product_page.PRODUCT_ADDED_ALERT)

def test_guest_cant_see_success_message(product_page):
    product_page.open()
    assert product_page.is_not_element_present(product_page.PRODUCT_ADDED_ALERT)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(product_page):
    product_page.open()
    product_page.add_product_to_cart()
    assert product_page.is_disappeared(product_page.PRODUCT_ADDED_ALERT)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    assert page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    from pages.login_page import LoginPage
    page.go_to_login_page()
    return LoginPage(page.browser)