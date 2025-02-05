import allure
from selenium.webdriver.common.by import By

class ProductPage:
    """
    Этот класс предоставляет методы для добавлению товаров в корзину
    """

    def __init__(self, driver):
        self._driver = driver
    
    def get(self):
        self._driver.get("https://www.saucedemo.com/inventory.html")
    
    @allure.step("Добавить товары в корзину")
    def add_product(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    @allure.step("Кликнуть на корзину")
    def click_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()