from selenium import webdriver
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
browser.quit()