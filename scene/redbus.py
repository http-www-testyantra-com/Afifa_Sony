
# from datetime import date, datetime, timedelta
import time

from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\afifa\\PycharmProjects\\SonyTr\\chromedriver.exe")
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//a[text()=' FLIGHTS ']").click()
driver.switch_to_window(driver.window_handles[1])
time.sleep(2)
driver.find_element_by_xpath("//label[text()='Round Trip']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='From']").send_keys("bost")
time.sleep(2)
driver.find_element_by_xpath("//div[text()='Boston (BOS)']").click()
driver.find_element_by_xpath("//input[@name='To']").send_keys("bang")
time.sleep(2)
driver.find_element_by_xpath("//div[text()='Bengaluru (BLR)']").click()


# future_date=date.today()+timedelta(20)
# print(future_date)

# print(future_date.strftime('%b/%d/%Y'))
# future_month=future_date.strftime('%b')
# print(future_month)
# print(future_date.strftime('%Y'))
# fdate=future_date.strftime('%d')
# print(fdate)
time.sleep(2)
driver.find_element_by_xpath("//input[@placeholder='Departure Date']").click()
time.sleep(2)

#/div[@class='date-table-right']/descendant::tr[@class='active']/descendant::span[text()='January']/../../../../../..//table[@class='date-table']/descendant::span[@class='act'][6]

while(True):
    # next = driver.find_element_by_xpath("//tr[@class='active']")
    next=driver.find_element_by_xpath("(//span[text()='January'])[1]")
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//div[@class='date-table-right']/descendant::tr[@class='active']/descendant::span[text()='January']/../../../../../..//table[@class='date-table']/descendant::span[@class='act'][6]").click()
        break
    except Exception as e:
        # print(e)
        next.click()
driver.find_element_by_xpath("//input[@placeholder='Return Date']").click()
time.sleep(2)
while(True):
    n2=driver.find_element_by_xpath("(//span[text()='May'])[3]")
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//div[@class='date-table-right']/descendant::tr[@class='active']/descendant::span[text()='(//span[text()='February'])[2]']/../../../../../..//table[@class='date-table']/descendant::span[@class='act'][5]").click()
        break
    except Exception as e:
        n2.click()
driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()




#(//span[@class='act'])[6]