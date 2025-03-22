from pages.base_page import BasePage, By

class CartPage(BasePage):
    URL = "http://selenium1py.pythonanywhere.com/basket/"

    CART_CONTENT = (By.ID, "content_inner")

    CART_TITLE = (By.CSS_SELECTOR, "div.basket-title")
    CART_ITEMS = (By.CSS_SELECTOR, "div.basket-items")


    def cart_content(self):
        cart_content = self.browser.find_element(*self.CART_CONTENT)
        return cart_content.find_element(By.TAG_NAME, "p")

    def get_cart_items(self):
        return self.browser.find_elements(*self.CART_ITEMS)

    def there_is_no_items_in_the_cart(self):
        return [] == self.get_cart_items()