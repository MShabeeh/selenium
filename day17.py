from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/drag_and_drop"
driver.get(url)
driver.maximize_window()
a = driver.find_element(By.ID,value="column-a")
b = driver.find_element(By.ID,value="column-b")
action = ActionChains(driver)
action.drag_and_drop(b,a).perform()
time.sleep(3)