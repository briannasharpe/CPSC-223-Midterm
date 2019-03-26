"""
889418042
Brianna Sharpe
3
"""

from problem_2 import ShoppingCart

filename = input("Enter file name containing unit prices: ")

# read file
f = open(filename, mode='r')
data = f.read()
f.close()

# split data into sections
data_list = data.split(':')
        
for e in data_list:
    # separate key and value from data sections
    key, value = e.split('=')
    # remove \n if present
    value = value.strip('\n')
    # add to dictionary
    ShoppingCart.unitPrices[key] = value
# ---------- end for loop (data_list) ----------

print(ShoppingCart.unitPrices)


filename = input("Enter file name containing a shopping cart order: ")

cart = ShoppingCart()
cart.empty_cart()

# read file
f = open(filename, mode='r')
data = f.read()
f.close()

# split data into sections
data_list = data.split(':')
        
for e in data_list:
    # separate key and value from data sections
    key, value = e.split('=')
    # remove \n if present
    value = value.strip('\n')
    # add to dictionary
    cart.addOrder(key, value)
# ---------- end for loop (data_list) ----------

# print(cart)

























#3
#reduce(lambda x,y:x+y, obj_list)