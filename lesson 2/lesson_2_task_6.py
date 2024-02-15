lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
sorted_lst = sorted(lst)
for n in sorted_lst:
    if (n < 30) and (n % 3 == 0):
        print(n)
