import os, sys

sys.path.append(os.getcwd())
from time import sleep
from page.page_in import PageIn
import pytest


class TestLogin():
    def setup_class(self):
        self.login = PageIn().page_get_pagelogin()


    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("username, password", [("admin", "1"), ("yiduiB", "a123456"), ("dadui1A", "a123456"), ("erduiA", "a123456"), ("erduiB", "a123456"), ("lingdao1", "a123456"), ("lingdao2", "a123456"), ("test1", "a123456")])
    def test_login(self, username, password):
        self.login.page_input_username(username)
        self.login.page_input_passwrof(password)
        self.login.page_click_login_btn()
        self.login.page_click_user_information()
        self.login.page_click_logout_btn()
