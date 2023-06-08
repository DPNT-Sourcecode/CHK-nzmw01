from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # define the prices of each sku
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    special_offers = {
        'A': {'quantity': 3, 'price': 130},
        'A_5': {'quantity': 5, 'price': 200},
        'B': {'quantity': 2, 'price': 45},
        'E': {'quantity': 2, 'price': 0}
    }
    # check if skus is empty
    if not skus:
        return -1
    
    # check if skus is a string
    if not isinstance(skus, str):
        return -1
    
    # count the frequency of each sku
    sku_count = Counter(skus)
    total_price = 0

    # check if skus contains only valid skus
    if any([sku not in prices.keys() for sku in sku_count.keys()]):
        return -1
    
    for item, count in sku_count.items():
        if item in special_offers:
            offer = special_offers[item]
            quantity = offer['quantity']
            if count >= quantity:
                if 'free' in offer:
                    free_item = offer['free']
                    free_item_count = count // quantity
                    sku_count[free_item] += free_item_count
            
            if item == 'A' and count >= quantity:
                if count >= offer['quantity']:
                    total_price += (count // quantity) * offer['price']
                    count = count % quantity
            
            if item == 'B' and count >= quantity:





def checkout(skus):
    defined_skus = 'ABCDE'
    # if not skus:
    #     return 0
    # skus = skus.upper()
   # if not all([sku in 'ABCD' for sku in skus]):
    #     return -1
    # count frequency of each sku
    sku_count = Counter(skus)
    # check if any sku is invalid
    if any([sku not in defined_skus for sku in sku_count.keys()]):
        return -1
    # check the count of each sku
    if any([sku_count[sku] < 0 for sku in sku_count.keys()]):
        return -1
    # calculate the total price
    total_price = 0
    for sku in sku_count.keys():
        if sku == 'A':
            if sku_count[sku] >= 5:
                total_price += (sku_count[sku] // 5) * 200 
                # reduce the count of A's by 5
                sku_count[sku] -= (sku_count[sku] // 5)
            if sku_count[sku] >= 3:
                total_price += (sku_count[sku] // 3) * 130 
                # reduce the count of A's by 3
                sku_count[sku] -= (sku_count[sku] // 3)
            if sku_count[sku] < 3:
                total_price += sku_count[sku] * 50
        elif sku == 'C':
            total_price += sku_count[sku] * 20
        elif sku == 'D':
            total_price += sku_count[sku] * 15
        elif sku == 'E':
            total_price += sku_count[sku] * 40
            # check how many multiples of 2E's
            if sku_count[sku] >= 2 and 'B' in sku_count.keys():
                # check how many multiples of E's
                sku_E_count = sku_count[sku] // 2
                # reduce the multiples of B's by the number of multiples of E's
                sku_count['B'] -= sku_E_count
                if sku_count['B'] < 0:
                    sku_count['B'] = 0


                # # check if there are multiples of B's
                # if sku_count['B'] >= sku_count[sku] // 2:
                #     sku_count['B'] -= sku_count[sku] // 2
                #     sku_count[sku] = 0
                # else:
                #     sku_count[sku] -= sku_count['B'] * 2
                #     sku_count['B'] = 0
        elif sku == 'B':
            if sku_count[sku] >= 2:
                total_price += (sku_count[sku] // 2) * 45 + (sku_count[sku] % 2) * 30
            else:
                total_price += sku_count[sku] * 30

    return total_price

    
    





