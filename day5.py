from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get('https://practice.expandtesting.com/checkboxes')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_element(By.XPATH,value="//input[@id='checkbox1']").click()
time.sleep(3)
