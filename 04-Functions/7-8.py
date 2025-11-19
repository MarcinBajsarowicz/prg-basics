def f(amount_to_pay):
    coins = [5, 2, 1]
    for coin in coins:
        while amount_to_pay >= coin:
            number_of_coins =+ 1
            amount_to_pay -= coin
    return number_of_coins
print(f(7))
