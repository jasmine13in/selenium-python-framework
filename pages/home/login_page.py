from selenium.webdriver.common.by import By
import base

import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[contains(text(),'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def EnterEmail(self, email):
        self.sendKeys(email, locator = self._email_field)

    def EnterPassword(self, password):
        self.sendKeys(password, locator = self._password_field)

    def ClickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")


    def Login(self, email = "", password = ""):
        time.sleep(2)
        self.clickLoginLink()
        time.sleep(2)
        self.EnterEmail(email)
        self.EnterPassword(password)
        time.sleep(2)
        self.ClickLoginButton()

    def verifyLoginSuccessful(self):
        time.sleep(1)
        result = self.isElementPresent("//img[contains(@class, 'zl-navbar')]",byType = "xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid')]", byType="xpath")
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("Google")

    def logout(self):
        self.nav.navigateToUserSettings()
        LogoutElement = self.waitForElement(locator="//a[contains(text(),'Logout')]", locatorType="xpath", pollFrequency=1)
        self.elementClick(element=LogoutElement)



    '''def getLoginLink(self):
        return self.driver.find_element_by_xpath(self._login_link)

    def getEmailField(self):
        return self.driver.find_element_by_id(self._email_field)

    def getPasswordField(self):
        return self.driver.find_element_by_id(self._password_field)

    def getLoginButton(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath(self._login_button)'''

