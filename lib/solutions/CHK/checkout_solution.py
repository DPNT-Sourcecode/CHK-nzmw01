

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = skus.upper()
    if not skus:
        return 0
    if not isinstance(skus, str):
        return -1
    if not all([sku in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for sku in skus]):
        return -1
    if any([skus.count(sku) > 9 for sku in 'STXYZ']):
        return -1
    if any([skus.count(sku) > 1 for sku in 'STXYZ']):
        return -1
    if 
