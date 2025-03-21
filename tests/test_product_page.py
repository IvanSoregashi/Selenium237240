import pytest

from pages.product_page import ProductPage

@pytest.fixture(scope="function", params=[0,
                                          1,
                                          2,
                                          3,
                                          4,
                                          5,
                                          6,
                                          pytest.param(7, marks=pytest.mark.xfail),
                                          8,
                                          9])
def product_page(browser, request):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{request.param}"
    return ProductPage(browser, link)

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
