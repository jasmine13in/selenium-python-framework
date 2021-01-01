from traceback import print_stack
from base.selenium_driver import SeleniumDriver
from utilities.util import Util

class BasePage(SeleniumDriver):
    def __init__(self, driver):
        super(BasePage,self).__init__(driver)
        self.driver = driver
        self.util = Util

    def verifyPageTitle(self,titletoVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titletoVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False