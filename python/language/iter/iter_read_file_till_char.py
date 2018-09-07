# read file till condition/char is met
'''
# mydata.txt
1
2
3

4
5
'''

l = []

# read file, use iter with condition as '\n'
# this will read till '\n' is reached
with open('mydata.txt') as f:
    for line in iter(f.readline, '\n'):
        l.append(line)

l
# ['1\n', '2\n', '3\n']
