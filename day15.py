from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, "datepicker2").click()
c_d = datetime.now()
print(c_d)
n_d = c_d + timedelta(days=1)
print(n_d)

n_d = str(n_d.day)
c_m = datetime.now().month
n_m = (c_m%12)+1
c_y = c_d.year
n_m_y = f"{n_m}/{c_y}"
print(n_m_y)
time.sleep(5)
m_drop = driver.find_element(By.CSS_SELECTOR,value="select[title='Change the month']")
select = Select(m_drop)
select.select_by_value(str(n_m_y))
y_drop = driver.find_element(By.CSS_SELECTOR,value="select[title='Change the year")
select = Select(y_drop)
select.select_by_visible_text("2024")
driver.find_element(By.LINK_TEXT,n_d).click()
time.sleep(5)