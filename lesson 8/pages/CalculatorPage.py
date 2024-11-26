from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def clear_input(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    def input_value(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)

    def input_num(self):
        self._driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

    def timer_result(self):
       result = WebDriverWait(self._driver, 50).until(
           EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
       )
       return result