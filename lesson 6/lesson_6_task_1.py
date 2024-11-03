from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 1. Перейдите на страницу http://uitestingplayground.com/ajax.

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

# 2. Нажмите на синюю кнопку.
blue_button = "#ajaxButton"
blue_button_click = driver.find_element(By.CSS_SELECTOR, blue_button).click()

# 3. Получите текст из зеленой плашки.
driver.implicitly_wait(20)
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# 4. Выведите его в консоль (”Data loaded with AJAX get request.”).
print(txt)

driver.quit()