import time

from .base_page import BasePage, NotABasketMixin, By
from .login_page import LoginPage

class MainPage(BasePage, NotABasketMixin):
    URL = "http://selenium1py.pythonanywhere.com/"

