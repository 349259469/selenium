import pytest

from homepage import Homepagesh

class TestLogin:
    def test_login(self):
        a = Homepagesh()
        driver = a.init_driver()
        driver.ff()
