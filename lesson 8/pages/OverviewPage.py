from selenium.webdriver.common.by import By

class OverviewPage:
    def __init__(self, driver):
        self._driver = driver
    
    def get(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def check_price_total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        full_text = total.text
        price = full_text.split(":")[-1].strip()
        return price