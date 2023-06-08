from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = skus.upper()
    if not skus:
        return 0
    if not isinstance(skus, str):
        return -1
    # if not all([sku in 'ABCD' for sku in skus]):
    #     return -1
    # count frequency of each sku
    sku_count = Counter(skus)
    # check if any sku is invalid
    if any([sku not in 'ABCD' for sku in sku_count.keys()]):
        return -1
    

