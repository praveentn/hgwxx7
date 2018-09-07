# *args

def fun_args(arg1, *argv):
    print("usual argument:", arg1)
    for arg in argv:
        print("args:", *argv)

fun_args('praveen', 'python', 'args', 'kwargs')

# output
usual argument: praveen
args: python args kwargs
args: python args kwargs
args: python args kwargs
