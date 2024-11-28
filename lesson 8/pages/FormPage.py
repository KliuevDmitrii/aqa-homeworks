from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def enter_first_name(self, first_name):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='first-name']")
        element.clear()
        element.send_keys(first_name)
    
    def enter_last_name(self, last_name):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='last-name']")
        element.clear()
        element.send_keys(last_name)

    def enter_address(self, address):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='address']")
        element.clear()
        element.send_keys(address)
        
    def enter_zip(self, zip):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='zip-code']")
        element.clear()
        element.send_keys(zip)

    def enter_city(self, city):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='city']")
        element.clear()
        element.send_keys(city)

    def enter_country(self, country):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='country']")
        element.clear()
        element.send_keys(country)

    def enter_mail(self, mail):
        element = self._driver.find_element(By.XPATH, "//input[@type='email' and @class='form-control' and @name='e-mail']")
        element.clear()
        element.send_keys(mail)

    def enter_phone(self, phone):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='phone']")
        element.clear()
        element.send_keys(phone)

    def enter_job_position(self, job_position):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='job-position']")
        element.clear()
        element.send_keys(job_position)

    def enter_company(self, company):
        element = self._driver.find_element(By.XPATH, "//input[@type='text' and @class='form-control' and @name='company']")
        element.clear()
        element.send_keys(company)

    def click_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        
    def get_empty_fild(self):
       elements = self._driver.find_elements(By.XPATH, "//div[contains(@class, 'alert') and text()='N/A']")
       empty_fields = {}
       for elem in elements:
            field_id = elem.get_attribute("id")
            field_text = elem.text.strip()
            empty_fields[field_id] = field_text
       return empty_fields