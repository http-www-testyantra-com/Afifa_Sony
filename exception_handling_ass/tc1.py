from selenium import webdriver
from selenium.webdriver import ActionChains



def mouse_hover():
    driver = webdriver.Chrome(executable_path='C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe')
    act = ActionChains(driver)
    try:

        driver.get("https://www.flipkart.com")
        driver.maximize_window()
        driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        tv = driver.find_element_by_xpath("//span[text()='TVs & Appliances']")
        act.move_to_element(tv).perform()
        driver.find_element_by_xpath("//a[@title='Oven Toaster Grills (OTG)']").click()


    except Exception as e:
        print(e)
        print('element not interactable ')
        mouse_hover()
        # driver.find_element_by_xpath("//a[@title='Oven Toaster Grills (OTG)']").click()



    finally:
        print('execution succesfull')

mouse_hover()

