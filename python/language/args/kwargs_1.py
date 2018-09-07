# **kwargs

def fun_(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

fun_(*tuple_vec)
1 0 1
fun_(**dict_vec)
1 0 1
