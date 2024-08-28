import time
from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginUser:
    login_selector = 'a[class="nav-link nav-link-txt"][href="https://qa-oc.roofscope.com/index.php?route=account/login"]'
    textbox_username_id = 'login-email'
    textbox_password_id = 'login-password'
    button_login_selector = 'button[class="btn btn-login  btn-lg"]'
    popup_logout_selector = 'li[class="dropdown desktop-menu nav-item"]'
    option_logout_selector = 'button[role="menuitem"][tabindex="0"]:nth-of-type(3)'
    def __init__(self, driver):
        self.driver = driver
    def navigateLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_selector).click()
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_selector).click()
    def clickLogout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.popup_logout_selector).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.option_logout_selector).click()
