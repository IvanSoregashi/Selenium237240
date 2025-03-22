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

    def register_new_user(self, email, password):
        reg_form = self.browser.find_element(*self.REGISTER_FORM)
        reg_form.find_element(By.ID, "id_registration-email").send_keys(email)
        reg_form.find_element(By.ID, "id_registration-password1").send_keys(password)
        reg_form.find_element(By.ID, "id_registration-password2").send_keys(password)
        reg_form.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary").click()

