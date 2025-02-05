import pytest
import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalculatorPage import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@allure.title("Проверка отображаемого результата вычисления по истечению заданного времени")
@allure.description("Тест проверяет, отображается результат вычисления в калькуляторе по истечени заданного времени")
@allure.feature("Calculator Functionality")
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.parametrize("num1, operator, num2, expected_result", [
    ("7", "+", "8", "15")
])
def test_displayed_result(browser, num1, operator, num2, expected_result):
    calculator_page = CalculatorPage(browser)
    calculator_page.clear_input()
    calculator_page.input_delay(45)
    calculator_page.input_num(num1)
    calculator_page.input_operator(operator) 
    calculator_page.input_num(num2)
    calculator_page.click_equals()

    result = calculator_page.get_result(expected_result)

    with allure.step("Проверка соответствия отображаемого результата ожидаемому"):
        assert result == expected_result