def bank(X, Y):
    deposit_amount = X * (1 + (10 * Y) / 100)
    return deposit_amount
    
sum = bank(100, 2)
print(sum)