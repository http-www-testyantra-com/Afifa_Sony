from selenium import webdriver

def invoke_browser(func):
    def inner(url):
        driver=webdriver.Chrome(executable_path="C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe")
        driver.get(url)
        driver.maximize_window()
        func(driver)
        driver.close()
    return inner

# @invoke_browser
# def test_gmail_email_tf(driver):
#     driver.find_element_by_xpath("//input[@type='email']").send_keys("tysstesting@gmail.com")
#
# test_gmail_email_tf("https://www.gmail.com")
#
# def test_gmail_pwd(driver):
#     driver.find_element_by_xpath("testing20$",Keys.ENTER)
#
# def click_check_box(driver):
#     driver=webdriver.Chrome()
#     driver.find_element_by_xpath("//span[@role='checkbox']").click()
#
# def inbox_count(driver):
#     msgs=driver.find_element_by_xpath("//div[@class='bsU']").text
#     # for i in ():
#     #     i.text
# def search_mail(driver):
#     driver.find_element_by_xpath("//input[@name='q']").send_keys("Saloni Pattnaik ",Keys.ENTER)
#     driver.find_element_by_xpath("(//span[text()='Saloni Pattnaik'])[2]").click()
#
# def log_out(driver):
#     driver.find_element_by_xpath("//a[text()='Sign out']").click()





