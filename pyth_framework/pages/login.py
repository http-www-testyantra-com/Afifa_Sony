from pyth_framework.base.common_methods import *
from pyth_framework.base.locators import *
class Login_Page(SeleniumDriver):
    _email_field = "email"
    _password_field = "password"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def enterEmail(self, email):
        self.getElement().sendKeys(email,self._email_field)


    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)



    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)






