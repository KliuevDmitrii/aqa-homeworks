from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 1. Откройте страницу http://the-internet.herokuapp.com/entry_ad.
firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
firefox_driver.get("http://the-internet.herokuapp.com/entry_ad")

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get("http://the-internet.herokuapp.com/entry_ad")

# 2. В модальном окне нажмите на кнопку Сlose.
button_close = ".modal-footer"

firefox_button_close = firefox_driver.find_element(By.CSS_SELECTOR, button_close)
chrome_button_close = chrome_driver.find_element(By.CSS_SELECTOR, button_close)

sleep(5)

firefox_driver.quit()
chrome_driver.quit()