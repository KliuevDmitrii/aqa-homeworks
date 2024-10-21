from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 1. Откройте страницу http://the-internet.herokuapp.com/login.
firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
firefox_driver.get("http://the-internet.herokuapp.com/login")

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get("http://the-internet.herokuapp.com/login")

# 2. В поле username введите значение tomsmith.
firefox_input_username = firefox_driver.find_element(By.CSS_SELECTOR, "#username")
chrome_input_username = chrome_driver.find_element(By.CSS_SELECTOR, "#username")

firefox_input_username.send_keys("tomsmith")
chrome_input_username.send_keys("tomsmith")

# 3. В поле password введите значение SuperSecretPassword!.
firefox_input_password = firefox_driver.find_element(By.CSS_SELECTOR, "#password")
chrome_input_password = chrome_driver.find_element(By.CSS_SELECTOR, "#password")

firefox_input_password.send_keys("SuperSecretPassword!")
chrome_input_password.send_keys("SuperSecretPassword!")

# 4. Нажмите кнопку Login.
button_login = ".fa-sign-in"

firefox_button_login = firefox_driver.find_element(By.CSS_SELECTOR, button_login)
chrome_button_login = chrome_driver.find_element(By.CSS_SELECTOR, button_login)

firefox_button_login.click()
chrome_button_login.click()

sleep(5)
firefox_driver.quit()
chrome_driver.quit()