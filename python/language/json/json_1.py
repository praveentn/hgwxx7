# using the "json" module
import json

# The standard string repr for dicts is hard to read:
json_map = {'a': 23, 'b': 42, 'c': 0xc0ffee}
>>> json_map
{'a': 23, 'b': 42, 'c': 12648430} # normal printing

print(json.dumps(json_map, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
# pretty print!
