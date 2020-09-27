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

global driver
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome-stable"
chrome_driver_binary = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, options=option)

import os
os.chmod('Test/chromedriver', 0o755)

def test_Features():
    driver.implicitly_wait(10)
    driver.get('http://localhost:80')
    print(driver.title)
def test_title_check():
    assert (driver.title == 'BudgetApp'), 'title not matched'
    driver.close()
