import time
from selenium import webdriver
from exc_custom.custom_exception import *

class BrowserException(Exception):
    def custom(self):
        driver = webdriver.Chrome()

        driver.get("https://www.flipkart.com")
        driver.maximize_window()
        driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//a[text()='VIEW ALL'])[1]").click()

# raise BrowserException('session not created exception')
raise NameException('session not created')


