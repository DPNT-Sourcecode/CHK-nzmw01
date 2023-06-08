from collections import Counter

def checkout(items):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50,
    }

    special_double_offers = {
        'A': [{'quantity': 3, 'price': 130}, {'quantity': 5, 'price': 200}],
        'H': [{'quantity': 5, 'price': 45}, {'quantity': 10, 'price': 80}],
        'V': [{'quantity': 2, 'price': 90}, {'quantity': 3, 'price': 130}],
    }
    special_price_offers = {
        'B': {'quantity': 2, 'price': 45},
        'F': {'quantity': 2, 'free': 'F'},
        'K': {'quantity': 2, 'price': 150},
        'P': {'quantity': 5, 'price': 200},
        'Q': {'quantity': 3, 'price': 80},
        'R': {'quantity': 3, 'free': 'Q'},
    }
    special_free_offers = {
        'E': {'quantity': 2, 'free': 'B'},
        'N': {'quantity': 3, 'free': 'M'},
        'P': {'quantity': 5, 'price': 200},
        'Q': {'quantity': 3, 'price': 80},
        'R': {'quantity': 3, 'free': 'Q'},
        'U': {'quantity': 3, 'free': 'U'},
        'V': [{'quantity': 2, 'price': 90}, {'quantity': 3, 'price': 130}],
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

    # select E items first if available
    if 'E' in item_counts.keys() and 'B' in item_counts.keys():
        count = item_counts['E']
        offer = special_offers['E']
        total_free = count // 2
        if total_free >= 1:
            item_counts[offer['free']] -= total_free
            if item_counts[offer['free']] < 0:
                item_counts[offer['free']] = 0

    for item, count in item_counts.items():
        # apply special offers
        if item in special_offers:
            offer = special_offers[item]
            if item == 'A':
                if count >= 5:
                    total_price += (count // 5) * 200
                    count %= 5
                if count >= 3:
                    total_price += (count // 3) * 130
                    count %= 3
            
            if item == 'B' and count >= 2:
                total_price += (count // 2) * 45
                count %= 2

            if item == 'F' and count >= 3:
                free_f_count = count // 3
                remainder_f_count = count % 3
                if remainder_f_count == 1:
                    free_f_count += 1
                count = count - free_f_count + remainder_f_count

            
             
        # add the price of the remaining items
        total_price += count * prices.get(item, 0)

    return total_price

