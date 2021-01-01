import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csvdata import RegisterCoursesCSVDataTests

#Get all tests from test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

smokeTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity = 2).run(smokeTest)
