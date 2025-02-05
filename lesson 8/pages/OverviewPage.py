import allure
from selenium.webdriver.common.by import By

class OverviewPage:
    """
    Этот класс предоставляет методы для проверки данных на странице заказа
    """
    
    def __init__(self, driver):
        self._driver = driver
    
    def get(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
    
    @allure.step("Получение итоговой суммы заказа")
    def check_price_total(self) -> str:
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        full_text = total.text
        price = full_text.split(":")[-1].strip()
        return price