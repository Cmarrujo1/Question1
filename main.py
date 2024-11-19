def cards(n):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    suits = ['C', 'D', 'H', 'S']


    suit = suits[n // len(ranks)]
    rank = ranks[n % len(ranks)]

    return rank + suit


print(cards(0))
print(cards(34))
