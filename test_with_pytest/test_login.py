import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestSample():

    @pytest.fixture(scope='class')  # For all the functions inside this class
    def test_setup(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()

        yield
        driver.close()
        driver.quit()

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # noqa
        driver.find_element(by=By.NAME, value='username').send_keys('Admin' + Keys.ESCAPE)  # noqa
        driver.find_element(by=By.NAME, value='password').send_keys('admin123' + Keys.ESCAPE)  # noqa
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert driver.title == 'OrangeHRM'

    def test_logout(self, test_setup):
        driver.find_element(by=By.CLASS_NAME, value="bi-caret-down-fill").click()  # noqa
        driver.find_element(by=By.LINK_TEXT, value='Logout').click()
