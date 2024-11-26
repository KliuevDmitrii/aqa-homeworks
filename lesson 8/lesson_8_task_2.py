from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalculatorPage import CalculatorPage

def test_displayed_result():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calculator_page = CalculatorPage(browser)
    calculator_page.get()
    calculator_page.clear_input()
    calculator_page.input_value()
    calculator_page.input_num()
    result = calculator_page.timer_result()
    
    assert result == True

    browser.quit()