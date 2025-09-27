from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/nested_frames')
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frameset-middle")
con = driver.find_element(By.ID,value=100).text

print(con)