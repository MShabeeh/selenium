from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

with open('testdata.json','r') as file:
    test_data = json.load(file)

for data in test_data['users']:
    driver = webdriver.Firefox()
    driver.get('https://www.saucedemo.com/v1/')
    us = data['username']
    pw = data['password']
    time.sleep(5)
    driver.find_element(By.ID,value='user-name').send_keys(us)
    driver.find_element(By.ID,value='password').send_keys(pw)
    driver.find_element(By.ID,value='login-button').click()
    time.sleep(5)
    driver.find_element(By.XPATH,value="//button[normalize-space()='Open Menu']").click()
    driver.find_element(By.XPATH,value="//a[@id='logout_sidebar_link']").click()
    time.sleep(5)
    driver.quit()