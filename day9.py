from selenium import webdriver
import requests 
from selenium.webdriver.common.by import By
url = 'https://the-internet.herokuapp.com/broken_images'
driver = webdriver.Firefox()
driver.get(url)
img = driver.find_elements(By.TAG_NAME,value="img")
brok_img = []

for i in img:
    src = i.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            brok_img.append(src)
            print(f"BIF{brok_img[-1]}")

driver.quit()