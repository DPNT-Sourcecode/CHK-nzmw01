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

    # check if skus is empty
    if not items:
        return 0
    
    # check if skus is a string
    if not isinstance(items, str):
        return -1
    
    # count the frequency of each sku
    item_counts = Counter(items)
    total_price = 0

    # check if skus contains only valid skus
    if any([sku not in prices.keys() for sku in item_counts.keys()]):
        return -1

    for item, count in item_counts.items():
        # apply special offers
        if item in special_offers:
            offer = special_offers[item]
            quantity = offer['quantity']
            if count >= quantity:
                if item == 'A' and count >= quantity:
                    if count >= offer['quantity']:
                        total_price += (count // quantity) * offer['price']
                        count %= quantity
                elif item == 'A' and count >= special_offers['A_5']['quantity']:
                    total_price += (count // special_offers['A_5']['quantity']) * special_offers['A_5']['price']
                    count %= special_offers['A_5']['quantity']

                if item == 'E' and offer['free'] in item_counts:
                    free_item = offer['free']
                    free_count = count // quantity
                    if item_counts[free_item] >= free_count:
                        item_counts[free_item] -= free_count
                    else:
                        item_counts[free_item] = 0

                
                if item == 'B' and count >= quantity:
                    total_price += (count // quantity) * offer['price']
                    count %= quantity
                
        total_price += count * prices.get(item, 0)

    return total_price


