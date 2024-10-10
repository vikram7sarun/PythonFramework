from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_xpath="//input[@id='email']"
    textbox_password_xpath="//input[@id='password']"
    btn_login_xpath="//*[@type='submit']"
    link_logout_linktxt="Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_linktxt).click()
