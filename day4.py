from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
viewports = [(1024,768),(786,1024),(270,370)]
browser.get('http://www.google.com/')
try:

    for x in viewports:
        browser.set_window_size(width=x[0],height=x[1])
        time.sleep(2)
finally:
    browser.close()
# browser.maximize_window()
# title = browser.title
# print(title)