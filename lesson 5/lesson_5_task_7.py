from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Откройте страницу http://the-internet.herokuapp.com/inputs.
firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
firefox_driver.get("http://the-internet.herokuapp.com/inputs")

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get("http://the-internet.herokuapp.com/inputs")

# 2. Введите в поле текст 1000.
firefox_input = firefox_driver.find_element(By.CSS_SELECTOR, "[type='number']")
chrome_input = chrome_driver.find_element(By.CSS_SELECTOR, "[type='number']")

firefox_input.send_keys("1000")
chrome_input.send_keys("1000")

# 3. Очистите это поле (метод clear).
firefox_input.clear()
chrome_input.clear()

# 4. Введите в это же поле текст 999.
firefox_input.send_keys("999")
chrome_input.send_keys("999")

sleep(5)
firefox_driver.quit()
chrome_driver.quit()
