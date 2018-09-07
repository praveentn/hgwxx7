name = 'John'

#1 basic method
print('Hello, his name is ' + name)

#2 .format method
print('Hello, his name is {}'.format(name))

#3 f-string literal method
print(f'Hello, his name is {name}')

#4 Template
from string import Template
s = Template('$who likes $what')
s.substitute(who='tim', what='kung pao')
# 'tim likes kung pao'


#1: won't work if name isn't a string.

#2: is fine on any version but is a little unwieldy to type. 
# Generally the best for compatibility across python versions.

#3: If the best option in terms of readability (and performance). 
# But it only works on python3.6+, so not a good idea if you want your code to be backwards compatible.

#4: Template strings support $-based substitutions

#5: old style formatting ala %s, %d, etc, which are now discouraged in favour for str.format.
