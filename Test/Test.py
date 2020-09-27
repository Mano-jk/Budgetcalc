from selenium import webdriver
#driver.implicitly_wait(10)
from selenium.webdriver.chrome.options import Options

option=Options()
option.add_argument("--headless")   
option.add_argument('--no-sandbox')
option.add_argument('start-maximized')
option.add_argument('disable-infobars')
option.add_argument('--disable-extensions')
option.add_argument('--disable-dev-shm-usage')

import os
os.chmod('Test/chromedriver', 0o755)
global driver
driver = webdriver.Chrome(executable_path= r'./Test/chromedriver' options=option)

def test_Features():
    driver.implicitly_wait(10)
    driver.get('http://localhost:80')
    print(driver.title)
def test_title_check():
    assert (driver.title == 'BudgetApp'), 'title not matched'
    driver.close()
