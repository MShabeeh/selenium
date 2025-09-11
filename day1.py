from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()

browser.get('http://selenium.dev/')
browser.maximize_window()
title = browser.title
print(title)
time.sleep(2)
try:
    assert 'Selenium12' in title
except Exception as e:
    print(e)
browser.find_element(By.U)
browser.quit()