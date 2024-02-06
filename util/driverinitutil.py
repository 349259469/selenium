import pathlib

from selenium import webdriver
class DriverInit:
    def __init__(self,url):
        driver = webdriver.Chrome(webdriver.ChromeOptions().add_argument(
        "--user-data-dir=" + str(pathlib.Path.home()) + r"\AppData\Local\Google\Chrome\seleniumTest"))
        driver.get(url)
        driver.maximize_window()
        self.driver.implicitly_wait(5)

    def __int__(self,driver):
        self.driver = driver

