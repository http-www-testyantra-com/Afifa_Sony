import time

from selenium import webdriver
from selenium.webdriver import ActionChains




def allert():
    driver = webdriver.Chrome(executable_path='C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe')
    try:

        driver.get("https://www.flipkart.com")
        driver.maximize_window()
        driver.switch_to.alert()
        driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
    except Exception:
        print('no such alert ')

allert()