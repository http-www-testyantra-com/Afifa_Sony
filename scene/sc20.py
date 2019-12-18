import time

from selenium import webdriver
from selenium.webdriver import ActionChains


def gold():
    driver=webdriver.Chrome(executable_path="C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe")
    driver.get("https://www.bluestone.com/")
    driver.maximize_window()
    act=ActionChains(driver)
    g_coin=driver.find_element_by_xpath("//a[@title='Coins']")
    time.sleep(2)
    act.move_to_element(g_coin).perform()
    driver.find_element_by_xpath("(//span[.='10 gram'])[1]").click()
    print(driver.find_element_by_xpath("//img[@class='img-responsive']").is_displayed())

gold()