from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://cosmocode.io/automation-practice-webtable/')
driver.execute_script("window.scrollTo(0,700)")
table = driver.find_element(By.ID,value='countries')
rows = table.find_elements(By.TAG_NAME,value='tr')
row_l = len(rows)
print(f'rows = {rows}')
print(f'rows_l = {row_l}')

s_v = 'Australia'
f = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME,value = 'td')
    for cell in cells:
        print(f'cell = {cell}')
        if s_v in cell.text:
            print(f'found={s_v}')
            f = True
            break
    if f:
        break
if not f:
    print(f'ele not found{s_v}')
