import allure
from faker import Faker
from EmployeeAPI import EmployeeApi
from EmployeeTable import EmployeeTable


api = EmployeeApi("http://5.101.50.27:8000")
db = EmployeeTable("postgresql+psycopg2://qa:skyqa@5.101.50.27:5432/x_clients")
fake = Faker()

@allure.title("Получение информации о сотруднике в компании")
@allure.description("Тест проверяет, что количество сотрудников, полученных через API, совпадает с количеством сотрудников, полученных из базы данных для компании с id = 2.")
@allure.feature("READ")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_employees_in_company():
    api_result = api.get_employees_in_company(2)
    db_result = db.get_employees_in_company(2)

    with allure.step("Сравнить размеры 2х списков"):
        assert len(api_result) == len(db_result) 

@allure.title("Получение информации о сотруднике")
@allure.description("Тест проверяет, что информация о сотруднике, полученная через API, совпадает с информацией о сотруднике, полученной из базы данных")
@allure.feature("READ")
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee():
    api_result = api.get_employee(2)
    db_result = db.get_employee(2)

    api_result_list = [api_result]

    with allure.step("Сравнить размеры 2х списков"):
        assert len(api_result_list) == len(db_result)

@allure.title("Добавление нового сотрудника")
@allure.description("Тест проверяет создание нового сотрудника и соответствие данных из API и базы данных.")
@allure.feature("CREATE")
@allure.severity(allure.severity_level.NORMAL)
def test_add_new_employee():
    body = api.get_employees_in_company(2)
    first_name = fake.first_name()
    last_name = fake.last_name()
    middle_name = fake.first_name()
    company_id = 2
    email = fake.email()
    phone = fake.phone_number()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat()

    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date)
    new_id = result["id"]

    with allure.step("Проверить поля нового сотрудника. Корректно заполнены"):
        for employee in body:
            if employee["id"] == new_id:
                assert employee["first_name"] == first_name
                assert employee["last_name"] == last_name
                assert employee["company_id"] == company_id
                assert employee["email"] == email
                assert employee["phone"] == phone
                assert employee["birthdate"] == birth_date
                assert employee["id"] == new_id
                assert employee["is_active"] is True

    db.delete(new_id)

@allure.title("Редактирование информации о сотруднике")
@allure.description("Тест проверяет возможность редактирования информации о сотруднике (email и телефон).")
@allure.feature("UPDATE")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_employee():
    first_name = fake.first_name()[:15]
    last_name = fake.last_name()[:15]
    middle_name = "Игоревич"
    company_id = 2
    email = fake.email()
    phone = fake.phone_number()[:15]
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat()
    is_active = True

    db.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date, is_active)

    company_id = 2
    max_id = db.get_max_id_employee(company_id)

    new_email = fake.email()
    new_phone = fake.phone_number()[:15]

    edited = api.edit_employee(max_id, new_email, new_phone)

    db.delete(max_id)
    
    with allure.step("Проверить данные для полей изменены"):
        assert edited["email"] == new_email
        assert edited["phone"] == new_phone

@allure.title("Деактивация сотрудника")
@allure.description("Тест проверяет возможность деактивации сотрудника через API, изменяя его статус is_active на False.")
@allure.feature("UPDATE")
@allure.severity(allure.severity_level.CRITICAL)
def test_deactivate_employee():
    first_name = "Ivan1"
    last_name = "Ivanov"
    middle_name = "Ivanovich"
    company_id = 2
    email = "dima@example.com"
    phone = "12341223"
    birth_date = "2020-12-28"
    is_active = True

    db.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date, is_active)

    company_id = 2
    max_id = db.get_max_id_employee(company_id)

    body = api.set_employee_active_state(max_id, False)

    db.delete(max_id)

    with allure.step("Проверить что сотрудник имеет статус деактивирован"):
        assert body["is_active"] is False

@allure.title("Деактивация и повторная активация сотрудника")
@allure.description("Тест проверяет возможность деактивации сотрудника через API, а затем повторной активации его статуса.")
@allure.feature("UPDATE")
@allure.severity(allure.severity_level.CRITICAL)
def test_deactivate_and_activate_back_employee():
    first_name = "Ivan1"
    last_name = "Ivanov"
    middle_name = "Ivanovich"
    company_id = 2
    email = "dima@example.com"
    phone = "12341223"
    birth_date = "2020-12-28"
    is_active = True

    db.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date, is_active)

    company_id = 2
    max_id = db.get_max_id_employee(company_id)
    api.set_employee_active_state(max_id, False)
    body = api.set_employee_active_state(max_id, True)

    db.delete(max_id)

    with allure.step("Проверить что сотрудник имеет статус активирован"):
        assert body["is_active"] is True