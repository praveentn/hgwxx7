# switch-case

def fun1(x):
    return x**x

def fun2(x):
    return x**(x**x)

switch_case = {
	'xpx': fun1,
	'xpxpx': fun2,
	'default': None
}

print(switch_case.get('xpx')(2))
# 4
print(switch_case.get('xpxpx')(2))
# 16
