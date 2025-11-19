def f(card_number):
    return card_number[:2] + '*' * (int(len(card_number)) - 6) + card_number[-4:]

print(f(card_number="5290312400019022"))