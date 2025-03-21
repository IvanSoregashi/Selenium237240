from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    URL = ""

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.URL)

    def is_element_present(self, locator):
        try:
            return bool(self.browser.find_elements(*locator))
        except NoSuchElementException as e:
            print(e)
            return False