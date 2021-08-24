import page
from base.base import Base


class PageLogin(Base):
    def page_input_username(self, value):
        self.base_input(page.page_username, value)

    def page_input_passwrof(self, value):
        self.base_input(page.page_password, value)

    def page_click_login_btn(self):
        self.base_click(page.page_login_btn)

    def page_click_user_information(self):
        self.base_click(page.page_user_information)

    def page_click_logout_btn(self):
        self.base_click(page.page_logout_btn)

    def page_input_qqqd_search_box(self, value):
        self.base_input(page.page_qqqd_search_box, value)

    def page_click_qqqd_search_btn(self):
        self.base_click(page.page_qqqd_search_btn)

