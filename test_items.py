from selenium.webdriver.common.by import By

def test_presence_of_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button.is_displayed()
    assert button.is_enabled()
    #print(button.text)
    #print(button.get_attribute("data-loading-text"))

