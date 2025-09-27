from selenium import webdriver
import requests 
from selenium.webdriver.common.by import By
driver= webdriver.Firefox()
url = 'https://openjsf.com/'
driver.get(url)
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,value = 'a')
print(len(all_links))

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f'broken link:{href}(status code: {response.status_code})')
driver.close()