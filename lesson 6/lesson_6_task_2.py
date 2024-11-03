from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1. Перейдите на сайт: http://uitestingplayground.com/textinput.
driver.get("http://uitestingplayground.com/textinput")

# 2. Укажите в поле ввода текст SkyPro.
input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.send_keys("SkyPro")

# 3. Нажмите на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# 4. Получите текст кнопки и выведите в консоль (“SkyPro”).
driver.find_element(By.CSS_SELECTOR, "#updatingButton")
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)

driver.quit()