from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def enter_value(self):
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

    def click_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def is_correct_values(self):
        success = self._driver.find_elements(By.CSS_SELECTOR, ".alert-success")
        for fields in success:
            success = fields.find_elements(By.CSS_SELECTOR, ".alert-success")
            return success

    def is_not_correct_values(self):
        danger = self._driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
        for fields in danger:
            danger = fields.find_elements(By.CSS_SELECTOR, ".alert-danger")
            return danger