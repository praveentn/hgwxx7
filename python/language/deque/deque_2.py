# print last n lines based on error code
# collections.deque is implemented in C and lock-free

# import libraries
from collections import deque

# deque of max size = required lines count 
line_history = deque(maxlen=25)

# read file
with open(file, 'r') as input:
    for line in input:
        if "error code" in line: 
            print(*line_history, line, sep='')
            # Clear history so if two errors seen in close proximity, we don't
            # echo some lines twice
            line_history.clear()
        else:
            # When deque reaches 25 lines, will automatically evict oldest
            line_history.append(line)
            
