def square(a):
    return a ** 2

a = float(input('Введите сторону квадрата: '))

m2 = square(a)

if (m2 % 1 != 0):
    import math
    rounded_m2 = math.ceil(m2)
    print(f'Площадь квадрата равна {rounded_m2}')

else:
    m2 = int(square(a))
    print(f'Площадь квадрата равна {m2}')

