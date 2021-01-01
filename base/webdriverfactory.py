"""
@package base

WebDriver Factory class                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
            driver.set_window_size(1440,900)
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver