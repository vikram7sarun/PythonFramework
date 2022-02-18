import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL  = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        self.logger.info("******************Test_001_Login****************")
        self.logger.info("******************Verify Home Page Title****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        # if act_title == "'OrangeHRM'":
        #     assert True
        #     self.driver.close()
        #     self.logger.info("******************Home Page Title is Passed****************")
        # else:
        #     self.driver.save_screenshot(".\\screenshots\\"+"test_homePage_Title.png")
        #     self.driver.close()
        #     self.logger.error("******************Home Page Title is Failed****************")
        #     assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("******************Verify Dashboard Page Title****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        # if act_title == "'OrangeHRM'":
        #     assert True
        #     self.logger.info("******************Dahboard Page Title is Passed****************")
        # else:
        #     assert False
        #     self.logger.error("******************Dahboard Page Title is Failed****************")
