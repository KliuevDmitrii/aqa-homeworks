import allure
from selenium.webdriver.common.by import By

class FormPage:
    """
    Этот класс предоставляет методы для выполнения действий на странице ввода почтовых данных
    """

    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Ввести имя {first_name}")
    def enter_first_name(self, first_name: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='first-name']")
        element.clear()
        element.send_keys(first_name)
    
    @allure.step("Ввести фамилию {last_name}")
    def enter_last_name(self, last_name: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='last-name']")
        element.clear()
        element.send_keys(last_name)
    
    @allure.step("Ввести адрес {address}")
    def enter_address(self, address: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='address']")
        element.clear()
        element.send_keys(address)
        
    @allure.step("Ввести индекс {zip}")
    def enter_zip(self, zip: int):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='zip-code']")
        element.clear()
        element.send_keys(zip)

    @allure.step("Ввести город {city}")
    def enter_city(self, city: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='city']")
        element.clear()
        element.send_keys(city)

    @allure.step("Ввести страну {country}")
    def enter_country(self, country):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='country']")
        element.clear()
        element.send_keys(country)

    @allure.step("Ввести адрес электронной почты {mail}")
    def enter_mail(self, mail: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='email' and @class='form-control' and @name='e-mail']")
        element.clear()
        element.send_keys(mail)
    
    @allure.step("Ввести телефонный номер {phone}")
    def enter_phone(self, phone: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='phone']")
        element.clear()
        element.send_keys(phone)

    @allure.step("Ввести вакансию {job_position}")
    def enter_job_position(self, job_position: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='job-position']")
        element.clear()
        element.send_keys(job_position)
    
    @allure.step("Ввести название компании {company}")
    def enter_company(self, company: str):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='company']")
        element.clear()
        element.send_keys(company)

    @allure.step("Нажать кнопку Применить")
    def click_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    
    @allure.step("Получить список всех пустых полей")
    def get_empty_fild(self) -> dict:
       elements = self._driver.find_elements(By.XPATH, "//div[contains(@class, 'alert') and text()='N/A']")
       empty_fields = {}
       for elem in elements:
            field_id = elem.get_attribute("id")
            field_text = elem.text.strip()
            empty_fields[field_id] = field_text
       return empty_fields