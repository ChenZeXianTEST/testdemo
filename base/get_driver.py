from selenium import webdriver


def get_ydzf_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.0.212:9090/login.html")
    return driver


def get_gf_gl_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.0.212:8016/")
    return driver

def get_gf_jg_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.0.212:8017/login.html")
    return driver