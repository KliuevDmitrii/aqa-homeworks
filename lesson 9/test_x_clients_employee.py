from EmployeeAPI import EmployeeApi

api = EmployeeApi("http://5.101.50.27:8000")

def test_get_employees_in_company():
    body = api.get_employees_in_company(2)

    assert len(body) > 0

def test_get_employee():
    body = api.get_employee(24)

    assert len(body) > 0

def test_add_new_employee():
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanovich"
    company_id = 2
    email = "dima@example.com"
    phone = "12341223"
    birth_date = "2020-12-28"

    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date)
    new_id = result["id"]

    assert result["first_name"] == first_name
    assert result["last_name"] == last_name
    assert result["company_id"] == company_id
    assert result["email"] == email
    assert result["phone"] == phone
    assert result["birthdate"] == birth_date
    assert result["id"] == new_id
    assert result["is_active"] is True

def test_edit_employee():
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanovich"
    company_id = 2
    email = "dima@example.com"
    phone = "12341223"
    birth_date = "2020-12-28"
    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date)
    new_id = result["id"]

    new_last_name = "Peter"
    new_email = "dima@example.com"
    new_phone = "567498"

    edited = api.edit_employee(new_id, new_last_name, new_email, new_phone)
    
    assert edited["last_name"] == new_last_name
    assert edited["email"] == new_email
    assert edited["phone"] == new_phone

def test_deactivate_employee():
    first_name = "Dima"
    last_name = "Ivanov"
    middle_name = "Ivanovich"
    company_id = 2
    email = "dima@example.com"
    phone = "12341223"
    birth_date = "2020-12-28"
    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date)
    new_id = result["id"]
    body = api.set_employee_active_state(new_id, False)
    assert body["is_active"] is False

def test_deactivate_and_activate_back_employee():
    first_name = "test"
    last_name = "test2"
    middle_name = "Ivanovich"
    company_id = 2
    email = "test@example.com"
    phone = "12341223"
    birth_date = "2020-12-28"
    result = api.create_employee(first_name, last_name, middle_name, company_id, email, phone, birth_date)
    new_id = result["id"]
    body_d = api.set_employee_active_state(new_id, False)
    assert body_d["is_active"] is False
    body_a = api.set_employee_active_state(new_id, True)
    assert body_a["is_active"] is True