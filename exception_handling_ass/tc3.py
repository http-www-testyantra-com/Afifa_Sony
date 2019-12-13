import time

from selenium import webdriver
from selenium.webdriver import ActionChains



def intercepted():
    driver = webdriver.Chrome(executable_path='C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe')
    try:

        driver.get("https://www.flipkart.com")
        driver.maximize_window()
        driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//a[text()='VIEW ALL'])[1]").click()
    except Exception:
        print('click intercepted')

intercepted()

