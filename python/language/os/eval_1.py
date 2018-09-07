from os import cpu_count
eval('[1,cores]', {'__builtins__': None}, {'cores': cpu_count()})
# [1, 4]
