# OrderedDict
# Python 3.6+ preserves insertion order

# `dict` is not explicitly meant to be an ordered collection, 
# so if you want to stay consistent and 
# not rely on a side effect of the new implementation 
# you should stick with `OrderedDict`


from collections import OrderedDict
print("This is a Dict:\n")
# This is a Dict:

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

a 1
b 2
c 3
d 4

print("\nThis is an Ordered Dict:\n")
# This is an Ordered Dict:

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)

a 1
b 2
c 3
d 4

# Changing the value of a key preserves the order in OrderedDict
# Deleting a key and adding it again sends the key to the last
