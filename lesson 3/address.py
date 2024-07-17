class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house}, - {self.apartment}"

    def __repr__(self):
        return f"Address(index={self.index}, city={self.city}, street={self.street}, house={self.house}, apartment={self.apartment})"