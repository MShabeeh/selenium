from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()
link = 'https://the-internet.herokuapp.com/dropdown'
driver.get(link)
driver.maximize_window()
variable = driver.find_element(By.ID,value='dropdown')
# print(variable)
select = Select(variable)
select.select_by_index(1)
select.select_by_value('2')
