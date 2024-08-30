import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


class OrderBooking:
    login_selector = 'a[class="nav-link nav-link-txt"][href="https://qa-oc.roofscope.com/index.php?route=account/login"]'
    username_field_id = 'login-email'
    password_field_id = 'login-password'
    login_button_selector = 'button[type="submit"]'
    search_location_id = 'pac-input'
    search_address_selector = 'button[class="btn btn-red p-3 mx-auto search-address-btn-home-page  but_search"]'
    confirm_location_selector = 'button[class="btn btn btn-red border-radius-x confirm confirm-location-btn"]'

    card_number_id = 'input-cc-number'
    expiry_month_id = 'input-cc-expire-date'
    first_month_selector = 'option[value="01"]'






    def __init__(self, driver):
        self.driver = driver

    def navigateLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_selector).click()

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.username_field_id).clear()
        self.driver.find_element(By.ID, self.username_field_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_selector).click()

    def searchLocation(self):
        res = self.driver.find_element(By.ID, 'pac-input')
        cities = ['Denver, CO, USA', 'Lahore, VA, USA', 'Durango, CO, USA', 'Las Vegas, NV, USA', 'IKEA, East IKEA Way, Centennial, CO, USA']
        random_city = random.choice(cities)
        res.send_keys(random_city)
        time.sleep(3)
        res.send_keys(Keys.TAB)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='SEARCH ADDRESS']").click()

    # def searchAddress(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.search_address_selector).click()

    def confirmLocation(self):
        # self.driver.find_element(By.CSS_SELECTOR, self.confirm_location_selector).click()
        self.driver.execute_script('window.scrollBy(0,500);')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'.btn.btn.btn-red.next').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[@id='scope_types']//div[1]//button[1]").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '.btn.btn.btn-red.next').click()
        time.sleep(1)
        self.driver.find_element(By.ID, 'button-cart').click()
        time.sleep(1)
        self.driver.execute_script('window.scrollBy(0,500);')
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, 'button[href="https://qa-oc.roofscope.com/index.php?route=checkout/checkout"]').click()

    # def placeOrder(self):
    #     self.driver.find_element(By.ID, self.card_number_id).send_keys("4111111111111111")
    #     time.sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR, self.expiry_month_id).click()

    #

