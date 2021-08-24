import page
from base.base import Base


class PageSignup(Base):
    def page_click_open_signup_page(self):
        self.base_click(page.page_open_signup_page_btn)

    def page_input_username(self, value):
        self.base_input(page.page_signup_username, value)

    def page_input_name(self, value):
        self.base_input(page.page_signup_name, value)

    def page_input_password(self, value):
        self.base_input(page.page_signup_password, value)

    def page_input_password_again(self, value):
        self.base_input(page.page_signup_password_again, value)

    def page_input_institutions_name(self, value):
        self.base_input(page.page_signup_institutions_name, value)

    def page_input_uniform_social_credit_code(self, value):
        self.base_input(page.page_signup_uniform_social_credit_code, value)

    def page_input_legal_representative_name(self, value):
        self.base_input(page.page_signup_legal_representative_name, value)

    def page_input_legal_representative_phone(self, value):
        self.base_input(page.page_signup_legal_representative_phone, value)

    def page_input_legal_representative_fixed_line_telephone(self, value):
        self.base_input(page.page_signup_Legal_representative_fixed_line_telephone, value)

    def page_click_enterprise_type(self):
        self.base_click(page.page_signup_enterprise_type)
        self.base_click(page.page_signup_enterprise_type_value)

    def page_input_enterprise_emile(self, value):
        self.base_input(page.page_signup_enterprise_emile, value)

    def page_input_enterprise_postal_code(self, value):
        self.base_input(page.page_signup_enterprise_postal_code, value)

    def page_input_enterprise_birth_date(self, value):
        self.base_input(page.page_signup_enterprise_birth_date, value)

    def page_input_enterprise_production_time(self, value):
        self.base_input(page.page_signup_enterprise_production_time, value)

    def page_click_enterprise_over_time(self):
        self.base_click(page.page_signup_enterprise_over_time)
        self.base_click(page.page_signup_enterprise_over_time_value)

    def page_input_enterprise_money(self, value):
        self.base_input(page.page_signup_enterprise_money, value)

    def page_click_enterprise_industry_involved(self):
        self.base_click(page.page_signup_enterprise_industry_involved)
        self.base_click(page.page_signup_enterprise_industry_involved_value)

    def page_click_is_rating_agencies(self):
        self.base_click(page.page_signup_is_rating_agencies)
        self.base_click(page.page_signup_is_rating_agencies_value)

    def page_click_is_agencies_top(self):
        self.base_click(page.page_signup_is_agencies_top)
        self.base_click(page.page_signup_is_agencies_top_value)

    def page_input_enterpise_address(self, value):
        self.base_input(page.page_signup_enterprise_address, value)

    def page_click_get_latitude_and_longitude_btn(self, x, y):
        self.base_click(page.page_signup_get_latitude_and_longitude_btn)
        self.base_action_chains_click(x, y)
        self.base_click(page.page_signup_save_latitude_and_longitude_btn)

    def page_input_enterprise_picture(self, filename):
        self.base_input(page.page_signup_enterprise_picture, filename)

    def page_input_enterprise_qualification(self, filename):
        self.base_input(page.page_signup_enterprise_qualification, filename)

    def page_input_enterprise_price(self, value):
        self.base_input(page.page_signup_enterprise_price, value)

    def page_input_enterprise_turf(self, value):
        self.base_input(page.page_signup_enterprise_turf, value)

    def page_click_city(self):
        self.base_click(page.page_signup_city)
        self.base_click(page.page_signup_city_guangdong)
        self.base_click(page.page_signup_city_zhanjiang)
        self.base_click(page.page_signup_city_xiashan)

    def page_click_enterpriser_level(self):
        self.base_click(page.page_signup_level)
        self.base_click(page.page_signup_level_value)

    def page_click_add_staff_btn(self):
        self.base_click(page.page_signup_add_staff_btn)

    def page_input_staff_name(self, value):
        self.base_input(page.page_signup_staff_name, value)

    def page_click_staff_sex(self):
        self.base_click(page.page_signup_staff_sex)
        self.base_click(page.page_signup_staff_sex_man)

    def page_input_staff_birth_date(self, value):
        self.base_input(page.page_signup_staff_birth_date, value)

    def page_click_educational_background(self):
        self.base_click(page.page_signup_staff_educational_background)
        self.base_click(page.page_signup_staff_educational_background_value)

    def page_input_staff_qualification(self, value):
        self.base_input(page.page_signup_staff_qualification, value)

    def page_click_staff_title(self):
        self.base_click(page.page_signup_staff_title)
        self.base_click(page.page_signup_staff_title_value)

    def page_input_staff_position(self, value):
        self.base_input(page.page_signup_staff_position, value)

    def page_input_staff_duty(self, value):
        self.base_input(page.page_signup_staff_duty, value)

    def page_input_staff_credit(self, value):
        self.base_input(page.page_signup_staff_credit, value)

    def page_input_staff_experience(self, value):
        self.base_input(page.page_signup_staff_experience, value)

    def page_click_add_staff_save_btn(self):
        self.base_click(page.page_signup_add_staff_save_btn)