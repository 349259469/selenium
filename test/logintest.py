import pytest

from homepage import Homepagesh

class TestLogin:
    def test_login(self):
        a = Homepagesh(url="http://webhis.karrytech.com")
        #a.init_driver()#.ff()
