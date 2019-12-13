from selenium import webdriver
from pyth_framework.pages.login import *
def invoke_browser(func):
    def inner(url):
        driver=webdriver.Chrome("C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe")
        driver.get(url)
        driver.maximize_window()
        func(driver)
        driver.close()
    return inner



@invoke_browser
def test_login(self):
    lp=Login_Page()
    lp.login("email","tysstesting@gmail.com")


test_login("https://www.gmail.com")