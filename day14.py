from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(url)
driver.maximize_window()
Alertb = driver.find_element(By.XPATH,value="//button[normalize-space()='Click for JS Prompt']")
alert = Alertb.click()
al = driver.switch_to.alert
alert_text= al.text
print(alert_text)
al.send_keys("Myself Shabeeh Ahmad Raza")
time.sleep(5)
al.accept()