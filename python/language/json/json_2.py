# load json

json_map = {'a': 23, 'b': 42, 'c': 0xc0ffee, 'd': True}
>>> json_map
{'a': 23, 'b': 42, 'c': 12648430, 'd': True}

# writing to file
with open('data.json', 'w') as outfile:
    json.dump(json_map, outfile)

with open('data.json', 'r') as infile:
    f = json.load(infile)

>>> f
{'a': 23, 'b': 42, 'c': 12648430, 'd': True}


# enable_ascii
# 
