from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
action = ActionChains(driver)
hovar_element = driver.find_element(By.XPATH,value="//a[normalize-space()='SwitchTo']")
time.sleep(5)
action.move_to_element(hovar_element).perform()
driver.find_element(By.XPATH,value="//a[normalize-space()='Frames']").click()
time.sleep(5)