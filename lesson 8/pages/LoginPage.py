from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://www.saucedemo.com/")

    def credentials(self):
        input_username = self._driver.find_element(By.CSS_SELECTOR, "#user-name")
        input_username.send_keys("standard_user")

        input_password = self._driver.find_element(By.CSS_SELECTOR, "#password")
        input_password.send_keys("secret_sauce")

    def click_button(self):
        button_login = "#login-button"
        self._driver.find_element(By.CSS_SELECTOR, button_login).click()