import os, sys
sys.path.append(os.getcwd())
from page.page_in import PageIn


class TestSignup:

    def setup_class(self):
        self.signup = PageIn().page_get_pagesignup()

    def teardown_class(self):
        pass
        # self.signup.driver.quit()

    def test_signup(self):
        qwe = '123'
        filepath = R"C:\Users\admin\Desktop\2.jpg"
        self.signup.page_click_open_signup_page()
        self.signup.page_input_username("13030150193")
        self.signup.page_input_name(qwe)
        self.signup.page_input_password('123qwe')
        self.signup.page_input_password_again('123qwe')
        self.signup.page_input_institutions_name(qwe)
        self.signup.page_input_uniform_social_credit_code("123123123123123123")
        self.signup.page_input_legal_representative_name("213")
        self.signup.page_input_legal_representative_phone(qwe)
        self.signup.page_input_legal_representative_fixed_line_telephone(qwe)
        self.signup.page_click_enterprise_type()
        self.signup.page_input_enterprise_emile("12@12.com")
        self.signup.page_input_enterprise_postal_code("510000")
        self.signup.page_input_enterprise_birth_date("2021-06-25")
        self.signup.page_input_enterprise_production_time("2021-06-24")
        self.signup.page_click_enterprise_over_time()
        self.signup.page_input_enterprise_money("5126")
        self.signup.page_click_enterprise_industry_involved()
        self.signup.page_click_is_rating_agencies()
        self.signup.page_click_is_agencies_top()
        self.signup.page_input_enterpise_address("天河区广东软件园")
        self.signup.page_click_get_latitude_and_longitude_btn(11, 22)
        # 拓展业务信息
        self.signup.page_input_enterprise_picture(filepath)
        # self.signup.page_input_enterprise_qualification(filepath)
        # self.signup.page_input_enterprise_price(filepath)
        self.signup.page_input_enterprise_turf("食品")
        self.signup.page_click_city()
        self.signup.page_click_enterpriser_level()
        # 添加人员
        self.signup.page_click_add_staff_btn()
        self.signup.page_input_staff_name("赵思易")
        self.signup.page_click_staff_sex()
        self.signup.page_input_staff_birth_date("2020-01-22")
        self.signup.page_click_educational_background()
        # self.signup.page_input_staff_qualification(filepath)
        self.signup.page_click_staff_title()
        self.signup.page_input_staff_position("评价")
        self.signup.page_input_staff_duty("评价人员")
        self.signup.page_input_staff_credit("在多家机构进行评测")
        self.signup.page_input_staff_experience()
        self.signup.page_click_add_staff_save_btn()
        # allure generate ./reports/allure_report_01 -o ./reports/html --clean
