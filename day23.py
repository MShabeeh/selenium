import time
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By

csv_file = 'testdata.csv'

test_data = []
with open(csv_file,'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)
print(test_data)
for data in test_data:
    us = data['username']
    pw = data['password']
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(5)
    driver.find_element(By.ID,value='user-name').send_keys(us)
    driver.find_element(By.ID,value='password').send_keys(pw)
    driver.find_element(By.ID,value='login-button').click()
    time.sleep(5)
    driver.find_element(By.XPATH,value="//button[normalize-space()='Open Menu']").click()
    driver.find_element(By.XPATH,value="//a[@id='logout_sidebar_link']").click()
    time.sleep(5)
    driver.quit()