from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # if not skus:
    #     return 0
    if not isinstance(skus, str):
        return -1
    skus = skus.upper()
   # if not all([sku in 'ABCD' for sku in skus]):
    #     return -1
    # count frequency of each sku
    sku_count = Counter(skus)
    # check if any sku is invalid
    if any([sku not in 'ABCD' for sku in sku_count.keys()]):
        return -1
    # check the count of each sku
    if any([sku_count[sku] < 0 for sku in sku_count.keys()]):
        return -1
    # calculate the total price
    total_price = 0
    for sku in sku_count.keys():
        if sku == 'A':
            total_price += (sku_count[sku] // 3) * 130 + (sku_count[sku] % 3) * 50
        elif sku == 'B':
            total_price += (sku_count[sku] // 2) * 45 + (sku_count[sku] % 2) * 30
        elif sku == 'C':
            total_price += sku_count[sku] * 20
        elif sku == 'D':
            total_price += sku_count[sku] * 15
    return total_price

    
    



