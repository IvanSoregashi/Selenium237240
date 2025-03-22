from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    URL = ""

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FALSE_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link_invalid")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    def __init__(self, browser: WebDriver, link=None):
        self.browser = browser
        self.URL = link or self.URL
        #self.browser.implicitly_wait(5)

    def go_to_login_page(self):
        from pages.login_page import LoginPage
        login_link = self.browser.find_element(*self.LOGIN_LINK)
        login_link.click()
        return LoginPage(self.browser)

    def should_be_login_link(self):
        return self.is_element_present(self.LOGIN_LINK)


    def open(self):
        self.browser.get(self.URL)

    def is_element_present(self, locator):
        try:
            return bool(self.browser.find_elements(*locator))
        except NoSuchElementException as e:
            print(e)
            return False

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        return self.is_element_present(self.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"


class NotABasketMixin:
    CART_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a.btn.btn-default")

    def to_the_cart_page(self):
        self.browser.find_element(*self.CART_BUTTON).click()
