from smartphone import Smartphone
catalog = []

phone1 = Smartphone("Nokia", "3310", "+79002314356")
catalog.append(phone1)
phone2 = Smartphone("Iphone", "XR", "+79235468425")
catalog.append(phone2)
phone3 = Smartphone("Redmi", "12", "+79561369753")
catalog.append(phone3)
phone4 = Smartphone("Samsung", "Z-flip", "+79022462311")
catalog.append(phone4)
phone5 = Smartphone("Motorola", "c350", "+73215436777")
catalog.append(phone5)

for obj in catalog:
    print(obj.brand_phone, "-", obj.model_phone, ",", obj.subscriber_number)