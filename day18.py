from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/horizontal_slider"
driver.get(url)
driver.maximize_window()
time.sleep(5)
slider = driver.find_element(By.XPATH,value="//input[@type='range']")
action = ActionChains(driver)
action.click_and_hold(slider).move_by_offset(xoffset=50,yoffset=0).release().perform()
time.sleep(5)
driver.quit()