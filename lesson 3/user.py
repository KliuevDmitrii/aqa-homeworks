class User:
    first_name = "No First_name"
    last_name = "No Last_name"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirst_name(self):
        print("Моё имя: ", self.first_name)

    def sayLast_name(self):
        print("Моя фамилия: ", self.last_name)

    def sayFull_name(self):
        print("Моё полное имя: ", self.first_name, self.last_name)


