from collections import Counter

def checkout(items):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    special_offers = {
        'A': {'quantity': 3, 'price': 130},
        'A_5': {'quantity': 5, 'price': 200},
        'B': {'quantity': 2, 'price': 45},
        'E': {'quantity': 2, 'free': 'B'}
    }

    item_counts = Counter(items)
    total_price = 0

    for item, count in item_counts.items():
        if item in special_offers:
            offer = special_offers[item]
            quantity = offer['quantity']
            if count >= quantity:
                if 'free' in offer:
                    free_item = offer['free']
                    free_count = count // quantity
                    item_counts[free_item] += free_count

            if item == 'A' and count >= quantity:
                if count >= offer['quantity']:
                    total_price += (count // quantity) * offer['price']
                    count %= quantity

        total_price += count * prices.get(item, 0)

    return total_price

