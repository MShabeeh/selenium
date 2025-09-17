from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.maximize_window()
url = 'https://www.selenium.dev/'
driver.get(url)
driver.switch_to.new_window()
driver.get('https://playwright.dev/')
time.sleep(3)
number_of_tabs = len(driver.window_handles)
print(number_of_tabs)

tabs_value = driver.window_handles
print(tabs_value)
curr_tab = driver.current_window_handle
print(curr_tab)
driver.find_element(By.CSS_SELECTOR,value=".getStarted_Sjon").click()
first_tab = driver.window_handles[0]
if curr_tab!= first_tab:
    driver.switch_to.window(first_tab)
driver.find_element(By.XPATH,value="//span[normalize-space()='Downloads']").click()