from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
url = "https://demo.automationtesting.in/Resizable.html"
driver.get(url)
driver.maximize_window()
resizable_element = driver.find_element(By.XPATH,value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_size = driver.find_element(By.XPATH,value="//div[@id='resizable']")
size = initial_size.size
print(size)
action = ActionChains(driver)
action.click_and_hold(resizable_element).move_by_offset(xoffset=100,yoffset=100).release().perform()
print(initial_size.size)