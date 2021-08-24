from base.get_driver import *
from page.page_login import PageLogin
from page.page_signup import PageSignup
driver = get_gf_jg_driver()


class PageIn():
    def page_get_pagelogin(self):
        return PageLogin(driver)

    def page_get_pagesignup(self):
        return PageSignup(driver)
