import pytest

from Browser import Browser
from Browser import SupportedBrowsers


class TestLogin():
    USER = 'Admin'
    PWD = 'admin123'

    @pytest.fixture(scope='class')  # For all the functions inside this class
    def test_setup(self):
        global browser
        browser = Browser()
        browser.new_browser(SupportedBrowsers.chromium, headless=True)

        yield
        browser.close_browser("ALL")

    def test_login(self, test_setup):
        browser.new_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # noqa
        browser.wait_for_load_state()
        browser.fill_text('input[name="username"]', self.USER)
        browser.fill_text('input[name="password"]', self.PWD)
        browser.click("button.orangehrm-login-button")
        assert browser.get_title() == 'OrangeHRM'

    def test_logout(self, test_setup):
        browser.wait_for_load_state()
        browser.click('i.oxd-userdropdown-icon')
        browser.click('a:text("Logout")')
        browser.wait_for_load_state()
        assert browser.get_url() == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'  # noqa
