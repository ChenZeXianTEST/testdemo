from selenium.webdriver.common.by import By

"""

    移动执法web端
    登录页面
    
"""
# 用户名
page_username = By.ID, "autosuggest__input"
# 密码
page_password = By.ID, "psd"
# 登录按钮
page_login_btn = By.CSS_SELECTOR, '[class="btn btn-success btn-block"]'
# 用户头像
page_user_information = By.CSS_SELECTOR, '[class="name"]'
# 退出按钮
page_logout_btn = By.XPATH, '/html/body/div[1]/div/div/div[1]/ul/div[2]/div[3]/div/div[2]/ul/li[3]'
# 一企一档搜索框
page_qqqd_search_box = By.CSS_SELECTOR, '[class="ivu-input ivu-input-large"]'
# 一企一档搜索按钮
page_qqqd_search_btn = By.CSS_SELECTOR, '[class="ivu-input-group-append ivu-input-search"]'

"""
    固废系统注册页面
"""
# 立即注册按钮
page_open_signup_page_btn = By.CSS_SELECTOR, '[class="register_btn"]'
# 用户名
page_signup_username = By.CSS_SELECTOR, '[placeholder="请输入手机号"]'
# 昵称
page_signup_name = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[1]/div[2]/div/input'
# 密码
page_signup_password = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[1]/div[3]/div/input'
# 确认密码
page_signup_password_again = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[1]/div[4]/div/input'
# 机构名称
page_signup_institutions_name = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[2]/div[1]/div/input'
# 统一社会信用代码
page_signup_uniform_social_credit_code = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[2]/div[2]/div/input'
# 法定代表人
page_signup_legal_representative_name = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[2]/div[3]/div/input'
# 法人联系电话
page_signup_legal_representative_phone = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[2]/div[4]/div/input'
# 法人固定电话
page_signup_Legal_representative_fixed_line_telephone = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[3]/div[1]/div/input'
# 企业类型
page_signup_enterprise_type = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/span'
# 企业类型数据_股份有限公司
page_signup_enterprise_type_value = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/ul[2]/li[3]'
# 电子邮箱
page_signup_enterprise_emile = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[3]/div[3]/div/input'
# 邮政编码
page_signup_enterprise_postal_code = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[3]/div[4]/div/input'
# 成立时间
page_signup_enterprise_birth_date = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[4]/div[1]/div/div[1]/div/input'
# 投产时间
page_signup_enterprise_production_time = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div/input'
# 营业期限
page_signup_enterprise_over_time = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[4]/div[3]/div[1]/div[1]/div/span'
page_signup_enterprise_over_time_value = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[4]/div[3]/div[1]/div[2]/ul[2]/li[1]'
# 注册资金(万元)
page_signup_enterprise_money = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[4]/div[4]/div/input'
# 所属行业
page_signup_enterprise_industry_involved = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[5]/div[1]/div/div[1]/div/span'
# 所属行业数据_化工
page_signup_enterprise_industry_involved_value = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[5]/div[1]/div/div[2]/ul[2]/li[3]'
# 企业业务类型
page_signup_is_rating_agencies = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[5]/div[2]/div/div[1]/div/span'
# 企业业务类型数据_评价机构
page_signup_is_rating_agencies_value = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[5]/div[2]/div/div[2]/ul[2]/li[2]'
# 是否推荐机构
page_signup_is_agencies_top = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[5]/div[3]/div/div[1]/div/span'
# 是否推荐机构_是
page_signup_is_agencies_top_value = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[5]/div[3]/div/div[2]/ul[2]/li[1]'
# 详细地址
page_signup_enterprise_address = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[5]/div[4]/div/input'
# 中心经度
page_signup_enterprise_longitude = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[6]/div[1]/div/input'
# 中心纬度
page_signup_enterprise_latitude = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[6]/div[2]/div/input'
# 获取经纬度
page_signup_get_latitude_and_longitude_btn = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[6]/div[3]/button/span'
# 确定经纬度按钮
page_signup_save_latitude_and_longitude_btn = By.XPATH, '/html/body/div[10]/div[2]/div/div/div[3]/button[2]'
# 企业头像
page_signup_enterprise_picture = By.XPATH, '//*[@id="register"]/main/div[1]/div[2]/div/div[7]/div/div/div/input'
# 机构执业资质
page_signup_enterprise_qualification = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[1]/div/div/div/input'
# 收费标准
page_signup_enterprise_price = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[2]/div/div/div/input'
# 执业范围
page_signup_enterprise_turf = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[3]/div[1]/div/input'
# 服务行政区域
page_signup_city = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[1]/input'
# 服务行政区区域_广东
page_signup_city_guangdong = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/span/ul/li'
page_signup_city_zhanjiang = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/span/span/ul/li[8]'
page_signup_city_xiashan = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div/span/span/span/ul/li[2]'
# 服务质量等级
page_signup_level = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[3]/div[3]/div/div[1]/div/span'
page_signup_level_value = By.XPATH, '//*[@id="register"]/main/div[2]/div[1]/div[2]/div/div[3]/div[3]/div/div[2]/ul[2]/li[5]'
# 添加成员
page_signup_add_staff_btn = By.XPATH, '//*[@id="register"]/main/div[2]/div[2]/div[2]/button'
# 姓名
page_signup_staff_name = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[1]/div/input'
# 性别
page_signup_staff_sex = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[2]/div/div[1]'
page_signup_staff_sex_man = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[2]/div/div[2]/ul[2]/li[1]'
# 出生年月日
page_signup_staff_birth_date = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/input'
# 学历
page_signup_staff_educational_background = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[4]/div/div[1]'
page_signup_staff_educational_background_value = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[4]/div/div[2]/ul[2]/li[4]'
# 执业资格
page_signup_staff_qualification = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[5]/div/div/div/input'
# 职称
page_signup_staff_title = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[6]/div/div[1]'
page_signup_staff_title_value = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[6]/div/div[2]/ul[2]/li[1]'
# 职务
page_signup_staff_position = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[7]/div/input'
# 职责
page_signup_staff_duty = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[8]/div/textarea'
# 信用情况
page_signup_staff_credit = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[9]/div/input'
# 执业经历
page_signup_staff_experience = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/div[10]/div/textarea'
# 新增成员保存按钮
page_signup_add_staff_save_btn = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[3]/div/button[2]'
# 新增成员取消按钮
page_signup_add_staff_cancel_btn = By.XPATH, '/html/body/div[6]/div[2]/div/div/div[3]/div/button[1]'
# 注册提交按钮
page_signup_submit_btn = By.XPATH, '/html/body/div[9]/div[2]/div/div/div[1]/div/div/button'
