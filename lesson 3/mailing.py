class Mailing:
    cost = 0
    track = "no track"
    
    def __init__(self, cost, track, to_address, from_address):
        self.cost = cost
        self.track = track
        self.to_address = to_address
        self.from_address = from_address

    def addTo_address(self, to_address):
        self.to_address = to_address
    
    def addFrom_address(self, from_address):
        self.from_address = from_address

    def display_info(self):
        print(f"Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей.")
