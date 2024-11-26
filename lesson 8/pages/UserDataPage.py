from selenium.webdriver.common.by import By

class UserDataPage:
    def __init__(self, driver):
        self._driver = driver
    
    def get(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def data_entry(self):
       first_name = "#first-name"
       last_name = "#last-name"
       zip_code =  "#postal-code"

       input_first_name = self._driver.find_element(By.CSS_SELECTOR, first_name)
       input_first_name.send_keys("Dmitrii")
       input_last_name = self._driver.find_element(By.CSS_SELECTOR, last_name)
       input_last_name.send_keys("Kliuev")
       input_zip_code = self._driver.find_element(By.CSS_SELECTOR, zip_code)
       input_zip_code.send_keys("123321")

    def click_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()