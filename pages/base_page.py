from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    URL = ""

    def __init__(self, browser: WebDriver, link=None):
        self.browser = browser
        self.URL = link or self.URL
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.URL)

    def is_element_present(self, locator):
        try:
            return bool(self.browser.find_elements(*locator))
        except NoSuchElementException as e:
            print(e)
            return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False
