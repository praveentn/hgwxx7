# extended slice or step or stride or jump
# seq[i:j:k] is "slice of s from i to j with step k"
# seq[::k] is a sequence of each k-th item in the entire sequence

s = 'hello'
s[-1] 
# o

s[1:2]
# e

s[1:-2]
# el

s[:-1]
# hell

s[::]
# hello

s[::-1]
# olleh

for x in range(100)[::10]:
    print(x)

#  0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90

