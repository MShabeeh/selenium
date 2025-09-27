from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/iframe')
iframe = driver.find_element(By.ID,value='mce_0_ifr')
t_e = driver.find_element(By.ID,value='tinymce')
t_e.clear()
t_e.send_keys('this is shabeeh Ahmad Raza')
time.sleep(5)
driver.switch_to.default_content()
s_l = driver.find_element(By.XPATH,value="//iframe[@id='mce_0_ifr']")
s_l.click()