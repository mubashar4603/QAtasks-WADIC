import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class SignupUser:
    create_button_selector = 'a[href="https://qa-oc.roofscope.com/index.php?route=account/register"][class="nav-link nav-link-txt"]'
    textbox_fname_id = 'first-name'
    textbox_lname_id = 'last-name'
    textbox_company_id = 'input-custom-field1'
    textbox_postal_id = 'input-custom-field2'
    textbox_phone_id = 'input-telephone'
    textbox_email_id = 'login-email'
    textbox_password_id = 'login-password'
    textbox_Cpassword_name = 'confirm'
    checkbox_selector = 'flexCheckDefault'
    recaptcha_selector = 'div[class="rc-anchor rc-anchor-normal rc-anchor-light"]'
    create_button_seletor = 'button[name="button"]'


    def __init__(self, driver):
        self.driver = driver

    def clickCreateAccount(self):
        self.driver.find_element(By.CSS_SELECTOR, self.create_button_selector).click()

    def setFname(self, fname):
        self.driver.find_element(By.ID, self.textbox_fname_id).send_keys(fname)

    def setLname(self, lname):
        self.driver.find_element(By.ID, self.textbox_lname_id).send_keys(lname)

    def setCompany(self, cname):
        self.driver.find_element(By.ID, self.textbox_company_id).send_keys(cname)

    def setPostal(self, pcode):
        self.driver.find_element(By.ID, self.textbox_postal_id).send_keys(pcode)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setPhone(self, phone):
        self.driver.find_element(By.ID, self.textbox_phone_id).send_keys(phone)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        self.driver.find_element(By.NAME, self.textbox_Cpassword_name).send_keys(password)

    def checkBox(self):
        self.driver.find_element(By.ID, self.checkbox_selector).click()

    def reCaptcha(self):
        captcha_iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
        self.driver.switch_to.frame(captcha_iframe)
        checkbox = self.driver.find_element(By.ID, "recaptcha-anchor")
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.driver.switch_to.default_content()

    def clickCreate(self):
        self.driver.find_element(By.CSS_SELECTOR, self.create_button_seletor).click()







