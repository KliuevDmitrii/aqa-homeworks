from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


class EmployeeTable:

    __scripts = {
        "select": "select * from employee "
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self, id):
        with self.db.connect() as connection:
            result = connection.execute(
                text("select * from employee where id = :select_id"), 
                {"select_id": id}).mappings().fetchall()
            connection.commit()
        return result
    
    def get_employees_in_company(self, company_id):
        with self.db.connect() as connection:
            result = connection.execute(
                text("select * from employee where company_id = :select_id"),
                {"select_id": company_id}).mappings().fetchall()
            connection.commit()
        return result
    
    def delete(self, id):
        with self.db.connect() as connection:
            result = connection.execute(
                text("DELETE FROM employee  WHERE id = :id_to_delete"),
                {"id_to_delete": id})
            connection.commit()
        return result
    
    def create_employee(self, first_name, last_name, middle_name, company_id, email, phone, birth_date, is_active=True):
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
    
    def get_max_id_employee(self, company_id):
        with self.db.connect() as connection:
            result = connection.execute(
            text('select MAX("id") from employee where company_id = :company_id'),
            {
            "company_id": company_id
                }
            ).scalar()
        return result
