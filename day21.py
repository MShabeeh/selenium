import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
firefox = Options()
firefox.add_argument("--private")
driver = webdriver.Firefox(options=firefox)
url ="https://www.google.com/"
driver.get(url)
time.sleep(5)
