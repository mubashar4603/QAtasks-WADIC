import time
from pageObjects.SignupUser import SignupUser
from utilities.readProperties import ReadConfig
from utilities.randomData import randomGenerate
from utilities.getLink import getLink
from utilities.customLogger import LogGen

class Test_000_Signup:
    baseURL = ReadConfig.getAppURL()
    email = ReadConfig.getEmail()
    fname = ReadConfig.getFname()
    lname = ReadConfig.getLname()
    cname = ReadConfig.getCompany()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    def test_signup_student(self, setup):
        self.logger.info("************* Test_000_Login *********")
        self.logger.info("************* Verifying User signup ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.signup_user = SignupUser(self.driver)
        self.signup_user.clickCreateAccount()
        time.sleep(2)
        self.signup_user.setFname(self.fname)
        self.signup_user.setLname(self.lname)
        self.signup_user.setCompany(self.cname)
        time.sleep(1)
        self.signup_user.setPostal(randomGenerate.generate_random_postal())
        time.sleep(1)
        self.signup_user.setEmail(randomGenerate.add_random_numbers_to_email(self.email))
        time.sleep(1)
        self.signup_user.setPhone(randomGenerate.generate_random_phone_number())
        time.sleep(1)
        self.signup_user.setPassword(self.password)
        time.sleep(1)
        self.signup_user.checkBox()
        self.driver.execute_script('window.scrollBy(0,500);')
        time.sleep(3)
        self.signup_user.reCaptcha()
        time.sleep(2)
        self.signup_user.clickCreate()
        time.sleep(12)
        # req_otp = getLink.access_email(username = 'randomstagtest@gmail.com', password = 'wzwf rclz qaeh cmda')
        # # print("outtttttpottttt:", req_otp)
        # fetched_otp = str(req_otp)
        # # print("ouuuuuttttputtttt:", fetched_otp)
        # self.signup_student.putOTP(fetched_otp)
        # time.sleep(4)
        # self.signup_student.verifyOTP()
        # time.sleep(10)
        actual_title = self.driver.title
        if actual_title == "Account Login":
            assert True
            self.driver.close()
            self.logger.info("************* Student_signup test is passed*********")
        else:
            self.driver.save_screenshot("/home/anonymous/PycharmProjects/QAtask-WADIC/Screenshots" + "test_signup.png")
            self.driver.close()
            self.logger.error("************* Student_signup test is failed*********")
            assert False



