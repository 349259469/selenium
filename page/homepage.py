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

    def init_driver(self):
        super.__init__()
        driver.implicitly_wait(10)
        driver.get("http://webhis.karrytech.com")
        driver.maximize_window()
        element = driver.find_element(By.ID,self.id)
        element.clear()
        element.send_keys(self.no)
        find_element = driver.find_element(By.ID, self.password)
        find_element.clear()
        find_element.send_keys(self.psw)
        driver.find_element(By.ID,self.nextstep).click()
        time.sleep(4)
        return Loginpagesh