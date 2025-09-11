from selenium import webdriver
from selenium.webdriver.common.by import By
import time


site = 'https://www.saucedemo.com'
driver = webdriver.Firefox()
driver.maximize_window()
user = "standard_user"
pw = "secret_sauce"
driver.get(site)
username_field = driver.find_element(By.ID,value="user-name")
password_field = driver.find_element(By.ID,value="password")

username_field.send_keys(user)
password_field.send_keys(pw)
login_button = driver.find_element(By.ID,value="login-button")
assert not login_button.get_attribute("disabled")

login_button.click()


success_element = driver.find_element(By.CSS_SELECTOR, value=".title")
assert success_element.text == "Products"

time.sleep(3)
driver.quit()