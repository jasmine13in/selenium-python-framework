from selenium.webdriver.common.by import By
import base

import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


####Locators defined here###
    __search_box = "//input[@id='search']"
    __search_button = "//div//form[@id = 'search']//div[@class = 'input-group']//button[1]"
    _course = "//h4[contains(text(),'{0}')]"
    _all_courses = "//div[contains(@class = 'all-courses')]"
    _enroll_button = "//div//button[contains(text(), 'Enroll in Course')]"
    _cc_num = "//div[@id='card-number']//input"
    _cc_exp = "//div[@id = 'card-expiry']//input"
    _cc_cvv = "//div[@id = 'card-cvc']//input"
    _submit_enroll = "//div//form[@id='checkout-form']//div[@class = 'col-xs-12']//button[1]"
    _enroll_error_message = "//span[contains(text(),'Your card number is invalid.')]"

##Element Interactions###

    def enterCourseName(self, name):
        time.sleep(2)
        self.sendKeys(name,locator=self.__search_box, locatorType="xpath")
        self.elementClick(locator = self.__search_button, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator = self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator = self._enroll_button, locatorType="xpath")

    def enterCardNum(self,num):
        self.sendKeys(num, locator = self._cc_num, locatorType="xpath")

    def enterCardExp(self, exp):
            self.sendKeys(exp, locator = self._cc_exp, locatorType="xpath")

    def enterCardCVV(self,cvv):
        self.sendKeys(cvv, locator = self._cc_cvv, locatorType="xpath")

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self,num, exp, cvv):
        time.sleep(2)
        self.enterCardNum(num)
        #time.sleep(2)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num = "", exp = "", cvv = ""):
        self.clickOnEnrollButton()
        time.sleep(2)
        self.webScroll(direction="down")
        #time.sleep(4)
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element = messageElement)

