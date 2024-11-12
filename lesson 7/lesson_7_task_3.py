from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1. Откройте сайт магазина: https://www.saucedemo.com/.
driver.get("https://www.saucedemo.com/")

# 2. Авторизуйтесь как пользователь standard_user.
input_username = driver.find_element(By.CSS_SELECTOR, "#user-name")
input_username.send_keys("standard_user")

input_password = driver.find_element(By.CSS_SELECTOR, "#password")
input_password.send_keys("secret_sauce")

button_login = "#login-button"
driver.find_element(By.CSS_SELECTOR, button_login).click()

# 3. Добавьте в корзину товары:
#  - Sauce Labs Backpack
#  - Sauce Labs Bolt T-Shirt
#  - Sauce Labs Onesie
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

# 4. Перейдите в корзину.
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()

# 5. Нажмите Checkout.
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# 6. Заполните форму своими данными:
#  - имя,
#  - фамилия,
#  - почтовый индекс.
first_name = "#first-name"
last_name = "#last-name"
zip_code =  "#postal-code"

input_first_name = driver.find_element(By.CSS_SELECTOR, first_name)
input_first_name.send_keys("Dmitrii")
input_last_name = driver.find_element(By.CSS_SELECTOR, last_name)
input_last_name.send_keys("Kliuev")
input_zip_code = driver.find_element(By.CSS_SELECTOR, zip_code)
input_zip_code.send_keys("123321")

# 7. Нажмите кнопку Continue.
driver.find_element(By.CSS_SELECTOR, "#continue").click()

# 8. Прочитайте со страницы итоговую стоимость (Total).
total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
text_total = total.text
print(text_total)

# 9. Закройте браузер.
driver.quit()

# 10. Проверьте, что итоговая сумма равна $58.29.

