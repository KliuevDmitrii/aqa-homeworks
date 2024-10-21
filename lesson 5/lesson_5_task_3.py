from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# 1. Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/

firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
firefox_driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# 2. Пять раз кликните на кнопку Add Element

button_locator = "[onclick='addElement()']"

firefox_button_add_element = firefox_driver.find_element(By.CSS_SELECTOR, button_locator)
chrome_button_add_element = chrome_driver.find_element(By.CSS_SELECTOR, button_locator)

for button_locator in range(5): 
    firefox_button_add_element.click()
    chrome_button_add_element.click()


# 3. Соберите со страницы список кнопок Delete
search_button_delete = "[onclick='deleteElement()']"

firefox_search_button_delete = firefox_driver.find_elements(By.CSS_SELECTOR, search_button_delete)
chrome_search_button_delete = chrome_driver.find_elements(By.CSS_SELECTOR, search_button_delete)

print(len(firefox_search_button_delete))
print(len(chrome_search_button_delete))

sleep(10)

firefox_driver.quit()
chrome_driver.quit()