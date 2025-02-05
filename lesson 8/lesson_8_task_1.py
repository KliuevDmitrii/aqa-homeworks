import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.FormPage import FormPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@allure.title("Проверка валидации пустого поля Zip Code")
@allure.description("Заполнение формы без указания индекса и проверка ошибки.")
@allure.feature("Validation")
@allure.severity(allure.severity_level.NORMAL)

@pytest.mark.parametrize("first_name, last_name, address, zip_code, city, country, mail, phone, job_position, company", [
    ("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "test@skypro.com", "+7985899998787", "QA", "SkyPro")
])
def test_empty_fild(browser, first_name, last_name, address, zip_code, city, country, mail, phone, job_position, company):
    form_page = FormPage(browser)
    form_page.get()
    form_page.enter_first_name(first_name)
    form_page.enter_last_name(last_name)
    form_page.enter_address(address)
    form_page.enter_zip(zip_code)
    form_page.enter_city(city)
    form_page.enter_country(country)
    form_page.enter_mail(mail)
    form_page.enter_phone(phone)
    form_page.enter_job_position(job_position)
    form_page.enter_company(company)
    form_page.click_button()
    empty_fields = form_page.get_empty_fild()
    
    with allure.step("Проверка наличия zip-code в списке пустых полей"):
        assert "zip-code" in empty_fields, "Поле 'Zip Code' отмечено как пустое."