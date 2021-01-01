from selenium.webdriver.common.by import By
import base

import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    _practice = "HOME"
    _user_settings_icon = "//img[contains(@class, 'zl-navbar')]"

    def navigateToAllCourses(self):
        self.elementClick(locator = self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator = self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator = self._practice, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator  = self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)


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

    '''def getLoginLink(self):
        return self.driver.find_element_by_xpath(self._login_link)

    def getEmailField(self):
        return self.driver.find_element_by_id(self._email_field)

    def getPasswordField(self):
        return self.driver.find_element_by_id(self._password_field)

    def getLoginButton(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath(self._login_button)'''

