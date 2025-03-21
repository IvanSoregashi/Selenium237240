from selenium.webdriver.common.by import By

def test1(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element(By.XPATH, "//button[@type='submit']").is_displayed()
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_enabled()

