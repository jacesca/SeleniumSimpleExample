import unittest
import HtmlTestRunner  # A Test Runner in python, for Human Readable HTML Reports  # noqa

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import shutil
import os


REPORT_PATH = "test_with_unittest/Reports"


class LoginLogoutTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        shutil.rmtree(REPORT_PATH)
        os.mkdir(REPORT_PATH)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_login_valid(self):
        # Load the page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # noqa
        # Write the username
        self.driver.find_element(by=By.NAME, value='username').send_keys('Admin' + Keys.ESCAPE)  # noqa
        # Write the pwd
        self.driver.find_element(by=By.NAME, value='password').send_keys('admin123' + Keys.ESCAPE)  # noqa
        # Click on Login Button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_logout_allowed(self):
        # Click on the user welcome name
        self.driver.find_element(by=By.CLASS_NAME, value="bi-caret-down-fill").click()  # noqa
        # Click on logout
        self.driver.find_element(by=By.LINK_TEXT, value='Logout').click()
        # driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()  # noqa


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=REPORT_PATH))  # noqa
