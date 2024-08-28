import time
from pageObjects.LoginUser import LoginUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("*************Verifying login test*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginUser(self.driver)
        self.lp.navigateLogin()
        time.sleep(2)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(6)
        actual_title = self.driver.title
        if actual_title == "Roof Scope":
            assert True
            self.logger.info("*************Login test is passed*********")
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/anonymous/PycharmProjects/QAtask-WADIC/Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("*************Login test is failed*********")
            assert False
