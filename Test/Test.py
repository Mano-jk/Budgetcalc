from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
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

class Budget(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.ChromeOptions()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
 def test_title_check():
    assert (driver.title == 'BudgetApp'), 'title not matched'       
 
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
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
driver.close()
