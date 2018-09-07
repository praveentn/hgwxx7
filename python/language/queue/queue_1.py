# Queues (FIFO) are not built-in Python methods

import queue

q = queue.Queue()

q.empty()
True

q = queue.Queue(2)

q.empty()
True

q.put(1)
q.full()
False

q.put(2)
q.full()
True

q.put_nowait()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: put_nowait() missing 1 required positional argument: 'item'


q.get()
1

q.get()
2

q.get_nowait()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "E:\Python\lib\queue.py", line 192, in get_nowait
    return self.get(block=False)
  File "E:\Python\lib\queue.py", line 161, in get
    raise Empty
queue.Empty

q.empty()
True
