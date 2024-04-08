from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://trends.google.com/trends/?geo=US')
# element = driver.find_element(By.XPATH,'.//*[@id="input-254"]')
# driver.maximize_window()
# element.send_keys("glass")
# element.send_keys(Keys.ENTER)
# #click on cookie
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cookieBarButton.cookieBarConsentButton"))).click()
# #click on subregion
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(.)='Subregion']"))).click()
# #click on city
# elementbtn=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//md-option[@value='city']")))
# driver.execute_script("arguments[0].click();", elementbtn)

time.sleep(10)