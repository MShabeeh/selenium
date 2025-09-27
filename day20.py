from selenium import webdriver
import time
url = "https://admin:admn@the-internet.herokuapp.com/basic_auth"
username = 'admin'
password = 'admin'

driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)