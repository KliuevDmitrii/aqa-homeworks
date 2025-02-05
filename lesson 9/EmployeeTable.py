from typing import Optional
import allure
from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


class EmployeeTable:
    """
    Класс для управления таблицей сотрудников.

    Этот класс предоставляет функциональность для работы с данными сотрудников, 
    включая добавление, удаление, обновление и получение записей.
    """

    def __init__(self, connection_string: str):
        self.db = create_engine(connection_string)
    
    @allure.step("БД. Запросить информацию о сотруднике {id}")
    def get_employee(self, id: int) -> list:
        """
        Получение информации о сотруднике по его id
        """

        with self.db.connect() as connection:
            result = connection.execute(
                text("select * from employee where id = :select_id"), 
                {"select_id": id}).mappings().fetchall()
            connection.commit()
        return result
    
    @allure.step("БД. Запросить список сотрудников в компании с номером {company_id}")
    def get_employees_in_company(self, company_id: int) -> list:
        """
        Получение списка сотрудников по id компании
        """

        with self.db.connect() as connection:
            result = connection.execute(
                text("select * from employee where company_id = :select_id"),
                {"select_id": company_id}).mappings().fetchall()
            connection.commit()
        return result
    
    @allure.step("БД. Удалить сотрудника {id}")
    def delete(self, id: int) -> Optional[int]:
        """
        Удаление сотрудника
        """

        with self.db.connect() as connection:
            result = connection.execute(
                text("DELETE FROM employee  WHERE id = :id_to_delete"),
                {"id_to_delete": id})
            connection.commit()
        return result
    
    @allure.step("БД. Создание нового сотрудника {first_name}, {last_name}, в компании {company_id}")
    def create_employee(
            self, 
            first_name: str, 
            last_name: str, 
            middle_name: str, 
            company_id: int, 
            email: str, 
            phone: str, 
            birth_date: str, 
            is_active: bool = True
            ) -> Optional[int]:
        """
        Создание сотрудника
        """

        with self.db.begin() as connection:
            result = connection.execute(
            text("""
                INSERT INTO employee 
                ("first_name", "last_name", "middle_name", "company_id", "email", "phone", "birthdate", "is_active") 
                VALUES (:new_first_name, :new_last_name, :new_middle_name, :new_company_id, :new_email, :new_phone, :new_birth_date, :new_is_active)
            """),
            {
                "new_first_name": first_name,
                "new_last_name": last_name,
                "new_middle_name": middle_name,
                "new_company_id": company_id,
                "new_email": email,
                "new_phone": phone,
                "new_birth_date": birth_date,
                "new_is_active": is_active
             
             })
        return result
    
    @allure.step("БД. Получить сотрудника с максимальным id в компании {company_id}")
    def get_max_id_employee(self, company_id: int) -> Optional[int]:
        """
        Получение сотрудника с максимальным id (созданного последним)
        """

        with self.db.connect() as connection:
            result = connection.execute(
            text('select MAX("id") from employee where company_id = :company_id'),
            {
            "company_id": company_id
                }
            ).scalar()
        return result
