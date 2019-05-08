from Basepage import *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    '''首页登录页面'''
    url='/'

    #定位器
    denglu_loc=(By.CSS_SELECTOR,'a.login.fr')
    username_loc = (By.ID,'username')
    password_loc = (By.ID,'password')
    submit_loc = (By.CSS_SELECTOR, 'a.loginbtn')

    #打开登录窗口
    def type_denglu(self):
        self.find_element(*self.denglu_loc).click()

    #用户名输入框元素
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    #密码输入框元素
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)
    # 登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()
    # 登录按钮元素
def test_user_login(driver,username,password):
        '''测试登录'''
        login_page=LoginPage(driver)
        login_page.open()
        login_page.type_denglu()
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.type_submit()




