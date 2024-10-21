from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 1. Откройте страницу http://uitestingplayground.com/classattr.
firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
firefox_driver.get("http://uitestingplayground.com/classattr")

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get("http://uitestingplayground.com/classattr")

# 2. Кликните на синюю кнопку.
button_blue = "//button[contains(@class, 'btn-test')]"

firefox_button_blue = firefox_driver.find_element(By.XPATH, button_blue)
chrome_button_blue = chrome_driver.find_element(By.XPATH, button_blue)

# 3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
for button_blue in range(3):
    firefox_button_blue.click()
    chrome_button_blue.click()

sleep(5)

firefox_driver.quit()
chrome_driver.quit()