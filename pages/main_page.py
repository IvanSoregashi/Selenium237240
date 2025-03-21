import time

from .base_page import BasePage, By
from .login_page import LoginPage

class MainPage(BasePage):
    URL = "http://selenium1py.pythonanywhere.com/"

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FALSE_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link_invalid")

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK)
        login_link.click()
        return LoginPage(self.browser)

    def should_be_login_link(self):
        return self.is_element_present(*self.FALSE_LOGIN_LINK)