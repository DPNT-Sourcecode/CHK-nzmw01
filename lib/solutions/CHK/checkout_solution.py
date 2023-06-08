from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    defined_skus = 'ABCDE'
    # if not skus:
    #     return 0
    if not isinstance(skus, str):
        return -1
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
                total_price += (sku_count[sku] // 5) * 200 + (sku_count[sku] // 3) * 130 + (sku_count[sku] % 5) * 50
            if sku_count[sku] >= 3:
                total_price += (sku_count[sku] // 3) * 130 + (sku_count[sku] % 3) * 50
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

                # check if there are multiples of B's
                if sku_count['B'] >= sku_count[sku] // 2:
                    sku_count['B'] -= sku_count[sku] // 2
                    sku_count[sku] = 0
                else:
                    sku_count[sku] -= sku_count['B'] * 2
                    sku_count['B'] = 0
        elif sku == 'B':
            if sku_count[sku] >= 2:
                total_price += (sku_count[sku] // 2) * 45 + (sku_count[sku] % 2) * 30
            else:
                total_price += sku_count[sku] * 30

    return total_price

    
    





