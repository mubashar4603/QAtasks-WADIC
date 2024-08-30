from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://mdpocket.com/reference-guides/medical-student-reference-guides/MDpocket-Medical-Student-eBook")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, 'bookCustomizerChaptersData').click()
time.sleep(4)
driver.find_element(By.ID,'showCustomizedBookFullPreview').click()
time.sleep(4)
driver.find_element(By.ID,'chapter-categoryid-1').click()

time.sleep(5)
drag_point = driver.find_element(By.ID,'chapterRow-43')
drop_area = driver.find_element(By.ID,'sortable2')
time.sleep(3)
action = ActionChains(driver)
action.drag_and_drop(drag_point, drop_area).perform()
time.sleep(5)
driver.execute_script('window.scrollBy(0,300);')
# driver.find_element(By.ID, 'chapterRow-43').click()
time.sleep(5)