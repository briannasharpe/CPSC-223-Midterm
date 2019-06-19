"""
Brianna Sharpe
2
"""

from problem_1 import merge_keys

class ShoppingCart(dict):
    # define variables
    unitPrices = {}
    
    def get_totalSales(self):
        return self._totalSales
    def set_totalSales(self, totalSales):
        self._totalSales = totalSales
    totalSales = property(get_totalSales, set_totalSales)
    
    # reset cart
    def empty_cart(self):
        ShoppingCart.unitPrices = {}
        ShoppingCart.totalSales = 0.0
        
    # add to cart
    def addOrder(self, itemName, quantity):
        if itemName in self: # item is already in cart
            self[itemName] += quantity # update quantity
            ShoppingCart.totalSales += ShoppingCart.unitPrices[itemName] * quantity # add item total to total sales
        else: # item is not in cart
            self[itemName] = quantity # add new item
            ShoppingCart.totalSales = ShoppingCart.unitPrices[itemName] * quantity # add item total to total sales
    
    # add content of two carts
    '''via cart = cart0 + cart1'''
    '''def __add__(self, cart1, cart2):
        ShoppingCart = merge_keys(cart1, cart2)
        ShoppingCart.totalSales = cart1.totalSales + cart2.totalSales
        return cart3'''
'''
carts = list()

cart = ShoppingCart()
cart.unitPrices['milk'] = 1.50
cart.addOrder('milk', 2)
cart.addOrder('milk', 2)

print(cart)
print(cart.totalSales)

cart2 = ShoppingCart()
cart2.unitPrices['cereal'] = 2
cart2.addOrder('cereal', 2)
cart2.addOrder('cereal', 2)

print(cart)
print(cart.totalSales)

carts.append(cart)
carts.append(cart2)

cart3 = cart + cart2
print(cart3)
print(cart3.totalSales)'''




'''
def mergeKeys(dict1, dict2):
    r_list = []
    return r_list

class ShoppingCart(dict):
    def __init__(self):
        super().__init() # call parent dict to empty itself
        self._totalSales = 0.0

    def __add__(self, other):
        sCart = ShoppingCart()    
        
        # adding orders
        keyList = mergeKeys(self, other)
        for k in keyList:
            q1 = self.get(k, 0.0)
            q2 = other.get(k, 0.0)
            q = q1 + q2
            sCart[k] = q
        
        # adding totalSales
        sCart._totalSales = self._totalSales + other._totalSales
        return sCart
'''
