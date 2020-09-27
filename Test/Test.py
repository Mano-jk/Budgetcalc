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

def test_title_check():
    assert (driver.title == 'BudgetApp'), 'title not matched'

    class Budget(unittest.TestCase):
    
    def test_budget(self):
        driver = self.driver
        driver.get("http://localhost:80")
        driver.find_element_by_name("amount").click()
        driver.find_element_by_name("amount").clear()
        driver.find_element_by_name("amount").send_keys("1000")
        driver.find_element_by_name("description").click()
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys("Salary")
        driver.find_element_by_xpath("//button/p").click()
        driver.find_element_by_name("amount").click()
        driver.find_element_by_name("amount").clear()
        driver.find_element_by_name("amount").send_keys("-100")
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys("Rent")
        driver.find_element_by_xpath("//button/p").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
driver.close()
