# sample use case for counter

from collections import Counter

# check if a word is an anagram of another
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


print(is_anagram('praveen', 'vanpeer'))
# True

print(is_anagram('vapeven', 'neevarp'))
# False

>>> Counter('praveen')
Counter({'e': 2, 'p': 1, 'r': 1, 'a': 1, 'v': 1, 'n': 1})
