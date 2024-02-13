def month_to_season(month_num):
    if month_num < 1:
        return 'номер месяца не должен быть меньше 1'
    
    if month_num > 12:
        return 'номер месяца не должен быть больше 12'
        

    if month_num < 3 or month_num == 12:
        return 'Зима'
        
    if month_num < 6:
        return 'Весна'
        
    if month_num < 9:
        return 'Лето'
        
    elif month_num < 12:
        return 'Осень'

month_num = int(input('Введите номер месяца: '))
res = month_to_season(month_num)
print(res)