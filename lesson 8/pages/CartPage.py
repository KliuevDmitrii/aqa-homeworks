import allure
from selenium.webdriver.common.by import By

class CartPage:
    """
    Этот класс предоставляет методы для выполнения действий в корзине
    """

    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://www.saucedemo.com/cart.html")
    
    @allure.step("Нажать на кнопку Сheckout")
    def click_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()