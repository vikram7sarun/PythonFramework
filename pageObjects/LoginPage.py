from selenium.webdriver.common.by import By

class LoginPage:
    txtbox_username_id="txtUsername"
    txtbox_password_id="txtPassword"
    btn_login_xpath="//*[@id='btnLogin']"
    link_logout_linktxt="Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.txtbox_username_id).clear()
        self.driver.find_element(By.ID,self.txtbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.txtbox_password_id).clear()
        self.driver.find_element(By.ID,self.txtbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_linktxt).click()
