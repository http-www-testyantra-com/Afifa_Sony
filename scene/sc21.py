import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def rings():
    driver=webdriver.Chrome(executable_path="C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe")
    driver.get("https://www.bluestone.com/")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@type='text']").send_keys("rings",Keys.ENTER)
    act=ActionChains(driver)
    time.sleep(2)
    price=driver.find_element_by_xpath("//span[.='Price']")
    act.move_to_element(price).perform()
    time.sleep(2)
    print('the count is :')
    print(driver.find_element_by_xpath("(//span[@class='items-count'])[1]").text)


rings()