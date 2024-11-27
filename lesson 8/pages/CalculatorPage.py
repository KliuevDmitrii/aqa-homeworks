from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def clear_input(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    def input_delay(self, delay_value):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def input_num(self, num):
        self._driver.find_element(By.XPATH, f"//span[@class='btn btn-outline-primary' and text()='{num}']").click()
        

    def input_operator(self, operator):
        self._driver.find_element(By.XPATH, f"//span[@class='operator btn btn-outline-success' and text()='{operator}']").click()

    def click_equals(self):
        self._driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

    def get_result(self, expected_result, timeout=50):
        WebDriverWait(self._driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_result)
        )
        result_element = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text.strip() 