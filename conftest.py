import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose a browser language: ru, en, ...")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    request.addfinalizer(browser.quit)
    yield browser
