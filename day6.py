from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

dropdown_e = driver.find_element(By.ID,value='dropdown')
select = Select(dropdown_e)
option_count = len(select.options)
e_c = 5

if option_count ==e_c:
    print('sb shi h bhai')
else:
    print('TC failed')
# select.select_by_visible_text("Option 2")
# select.select_by_index(1)
# select.select_by_value('2')