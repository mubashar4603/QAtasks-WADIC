import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
        # maximize the windows
driver.maximize_window()
        # navigate to url
driver.get("https://qa-oc.roofscope.com/index.php?route=account/login")
# time.sleep(2)
# captcha_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
# driver.switch_to.frame(captcha_iframe)
# checkbox = driver.find_element(By.ID, "recaptcha-anchor")
# driver.execute_script("arguments[0].click();", checkbox)
# driver.switch_to.default_content()
driver.find_element(By.ID,'login-email').send_keys("metutorstest+1@gmail.com")
driver.find_element(By.ID,'login-password').send_keys("Test@123")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# driver.find_element(By.ID, 'pac-input').send_keys("Colorado, USA")


res = driver.find_element(By.ID, 'pac-input')
res.send_keys("Pueblo, CO, USA" + Keys.TAB)
time.sleep(2)

# res.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'button[class="btn btn btn-red border-radius-x confirm confirm-location-btn"]').click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'button[class="btn btn-red p-3 mx-auto search-address-btn-home-page  but_search"]').click()

time.sleep(10)
