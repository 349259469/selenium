import time

from selenium.webdriver.common.by import By
from loginpage import Loginpagesh
from driverinitutil import DriverInit

class Homepagesh(DriverInit):
    id = "login_username"
    password = "login_password"
    nextstep = "nextBtn"
    no = "401"
    psw = "1"

    def __init__(self,url):
        super().__init__(url)

    def init_driver(self):
        # element = super().driver.find_element(By.ID,self.id)
        # element.clear()
        # element.send_keys(self.no)
        # find_element = super().driver.find_element(By.ID, self.password)
        # find_element.clear()
        # find_element.send_keys(self.psw)
        # super().driver.find_element(By.ID,self.nextstep).click()
        # time.sleep(4)
        print('1111111')
