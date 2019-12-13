from selenium import webdriver
from selenium.webdriver import ActionChains



def click():
    driver = webdriver.Chrome(executable_path='C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe')
    try:
        driver.find_element_by_xpath("//h2[text()='Deals of the Day']").click()
    except Exception as e:
        print('element not clickable ')

click()