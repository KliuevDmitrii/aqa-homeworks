
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.fixture
def browser(browser):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html.
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# 2. Заполните форму значениями:
#  - First name - Иван
#  - Last name - Петров
#  - Address - Ленина, 55-3
#  - Email - test@skypro.com
#  - Phone number - +7985899998787
#  - Zip code - оставить пустым
#  - City - Москва
#  - Country - Россия
#  - Job position - QA
#  - Company - SkyPro
    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")
    
    address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address.send_keys("Ленина, 55-3")
    
    email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email.send_keys("test@skypro.com")
    
    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")
    
    city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city.send_keys("Москва")
    
    country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country.send_keys("Россия")
    
    job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
    job_position.send_keys("QA")
    
    company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company.send_keys("SkyPro")

# 3. Нажмите кнопку Submit.
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

# 4. Проверьте (assert), что поле Zip code подсвечено красным.

    element_red = driver.find_element(By.CSS_SELECTOR, ".alert.py-2.alert-danger")
    assert element_red.is_displayed()

# 5. Проверьте (assert), что остальные поля подсвечены зеленым.

    element_green = driver.find_element(By.CSS_SELECTOR, ".alert.py-2.alert-success")
    assert element_green.is_displayed()

