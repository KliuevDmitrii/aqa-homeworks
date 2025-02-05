import allure
import requests
from typing import Optional

class EmployeeApi:
    """
    API-класс для управления сотрудниками.

    Этот класс предоставляет методы для выполнения CRUD-операций (создание, чтение, обновление, удаление) 
    над сущностями сотрудников.
    """

    def __init__(self, url: str):
        self.url = url
    
    @allure.step("api. Получить токен авторизации")
    def get_token(self, user: str = 'ginny', password: str = 'batbogey') -> str:
        """
        Получение токена авторизации
        """

        creds = {
        'username': user,
        'password': password
    }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]
    
    @allure.step("api. Получить информацию о сотруднике через API")
    def get_employee(self, id: int) -> dict:
        """
        Получение списка информации о сотруднике
        """

        resp = requests.get(self.url + '/employee/info/' + str(id))
        return resp.json()
    
    @allure.step("api. Получить список сотрудников конкретной компании по id {id} через API")
    def get_employees_in_company(self, id: int) -> dict:
        """
        Получение списка сотрудников по id конкретной компании
        """

        resp = requests.get(self.url + '/employee/list/' + str(id))
        print(resp)
        return resp.json()
    
    @allure.step("api. Создать сотрудника {first_name}, {last_name} в компании с id {company_id} через API")
    def create_employee(
            self, 
            first_name: str = "", 
            last_name: str = "", 
            middle_name: str = "", 
            company_id: Optional[int] = None, 
            email: str ="", 
            phone: str = "", 
            birth_date: str = ""
            ) -> dict:
        """
        Создание сотрудника
        """

        employee = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birth_date
        }
        
        resp = requests.post(self.url + '/employee/create', json=employee)
        return resp.json()
    
    @allure.step("api. Редактировать сотрудника через API")
    def edit_employee(self, new_id: int, new_email: str, new_phone: str) -> dict:
        """
        Редактирование сотрудника
        """

        client_token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{new_id}?client_token={client_token}"

        employee = {
            "email": new_email,
            "phone": new_phone
        }

        resp = requests.patch(url_with_token, json=employee)
        return resp.json()

    @allure.step("api. (Де)активировать сотрудника с id {id}")
    def set_employee_active_state(self, id: int, is_active: bool) -> dict:
        """
        Измение активации сотрудника
        """

        client_token = self.get_token()

        url_with_token = f"{self.url}/employee/change/{id}?client_token={client_token}"
        resp = requests.patch(url_with_token, json={"is_active": is_active})
        return resp.json()