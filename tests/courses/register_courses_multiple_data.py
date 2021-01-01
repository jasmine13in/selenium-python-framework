import selenium
from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners","191","1220", "10"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num = ccNum, exp = ccExp, cvv = ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.mark(result, "enrollment verification failed due to wrong card no")
        self.webScroll(direction="up")
        self.driver.find_element_by_link_text("ALL COURSES").click()

