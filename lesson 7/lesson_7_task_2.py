import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_displayed_result(browser):

# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# 2. В поле ввода по локатору #delay введите значение 45.
    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    input = driver.find_element(By.CSS_SELECTOR, "#delay")
    input.send_keys(45)

# 3. Нажмите на кнопки:
#  - 7
#  - '+'
#  - 8
#  - '='
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
    driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

# 4. Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    waiter = WebDriverWait(driver, 50)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)

    result = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert result.text == "15"
