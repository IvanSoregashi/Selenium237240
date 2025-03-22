from .base_page import BasePage, NotABasketMixin, By
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage, NotABasketMixin):
    URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED_ALERT = (By.CSS_SELECTOR, "div.alertinner")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")

    def add_product_to_cart(self):
        button = self.browser.find_element(*self.ADD_TO_CART_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_added_alert_is_there(self):
        return self.is_element_present(self.PRODUCT_ADDED_ALERT)

    def get_basket_total_price(self):
        element = self.browser.find_element(*self.CART_TOTAL_PRICE)
        text = element.text.strip()
        price = text.rstrip("\nView basket").lstrip("Basket total: ")
        return price

    def get_items_price(self):
        element = self.browser.find_element(*self.PRODUCT_PRICE)
        return element.text.strip()

    def get_product_name(self):
        element = self.browser.find_element(*self.PRODUCT_NAME)
        text = element.text.strip()
        return text

    def get_product_name_from_alert(self):
        element = self.browser.find_element(*self.PRODUCT_ADDED_ALERT)
        text = element.text.strip()
        return text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.PRODUCT_ADDED_ALERT), \
            "Success message is presented, but should not be"

