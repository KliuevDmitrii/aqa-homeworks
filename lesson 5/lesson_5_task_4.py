from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 1. Откройте страницу http://uitestingplayground.com/dynamicid.
firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
firefox_driver.get("http://uitestingplayground.com/dynamicid")

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get("http://uitestingplayground.com/dynamicid")


# 2. Кликните на синюю кнопку.
button = ".btn.btn-primary"

firefox_button = firefox_driver.find_element(By.CSS_SELECTOR, button)
chrome_button = chrome_driver.find_element(By.CSS_SELECTOR, button)

# 3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
for button in range(3):
    firefox_button.click()
    chrome_button.click()
    

sleep(5)

firefox_driver.quit()
chrome_driver.quit()