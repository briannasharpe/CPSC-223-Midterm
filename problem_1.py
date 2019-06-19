"""
Brianna Sharpe
1
"""

# merge keys from two dictionary objects into a list
def merge_keys(dict1, dict2):
    # define variables
    key_list = set() # set for no duplicates
    
    # turn keys into set
    dict1_keys = list(set((dict1.keys())))
    dict2_keys = list(set((dict2.keys())))
    
    # add to list of all keys
    for a in range(len(dict1_keys)):
        key_list.add(dict1_keys[a])
    for b in range(len(dict2_keys)):
        key_list.add(dict2_keys[b])
    
    # turn to list
    key_list = list(key_list)
    
    return key_list

'''
dicta = {'a k1': 'a v1', 'a k2': 'a v2'}
dictb = {'b k1': 'b v1', 'a k2': 'b v2'}

print(merge_keys(dicta, dictb))


def func(d1, d2):
    
    key1s = d1.keys()
    key2s = d2.keys()
    s1 = set(key1s)
    s2 = set(key2s)
    s3 = s1.union(s2)
    return s3
    
    # or
    
    s = set()
    for k in d1:
        s.add(k)
    
    

print(func(dicta, dictb))
'''






