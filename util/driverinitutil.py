import pathlib

from selenium import webdriver
class DriverInit:
    def __init__(self):
        options = webdriver.ChromeOptions().add_argument("--user-data-dir=" + str(pathlib.Path.home()) + r"\AppData\Local\Google\Chrome\seleniumTest")
        driver = webdriver.Chrome(options)
