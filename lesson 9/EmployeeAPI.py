import requests

class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_token(self, user='ginny' , password='batbogey'):
        creds = {
        'username': user,
        'password': password
    }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]
    
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/info' + str(id))
        return resp.json()
    
    def get_employees_in_company(self, id):
        resp = requests.get(self.url + '/employee/list/' + str(id))
        print(resp)
        return resp.json()
    
    def create_employee(self, first_name, last_name="", middle_name="", company_id="", email="", phone="", birth_date=""):
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
    
    def edit_employee(self, new_id, new_email, new_phone):
        client_token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{new_id}?client_token={client_token}"

        employee = {
            "email": new_email,
            "phone": new_phone
        }

        resp = requests.patch(url_with_token, json=employee)
        return resp.json()

    
    def set_employee_active_state(self, id, is_active):
        client_token = self.get_token()

        url_with_token = f"{self.url}/employee/change/{id}?client_token={client_token}"
        resp = requests.patch(url_with_token, json={"is_active": is_active})
        return resp.json()
    