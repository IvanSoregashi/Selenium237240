from .base_page import BasePage, By

class LoginPage(BasePage):
    URL = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    def should_be_login_page(self):
        return (
                self.should_be_login_url()
                and self.should_be_login_form()
                and self.should_be_register_form()
        )

    def should_be_login_url(self):
        return self.browser.current_url == self.URL

    def should_be_login_form(self):
        return self.is_element_present(self.LOGIN_FORM)

    def should_be_register_form(self):
        return self.is_element_present(self.REGISTER_FORM)
