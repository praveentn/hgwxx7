import sys

l1 = [None] * 10
l2 = [None for _ in range(10)]

print('Size of l1 =', sys.getsizeof(l1))
# 144
print('Size of l2 =', sys.getsizeof(l2))
# 192

'''
When you write [None] * 10, Python knows that it will need a list of exactly 10 objects, 
so it allocates exactly that.

When you use a list comprehension, Python doesn't know how much it will need. 
So it gradually grows the list as elements are added. 

For each reallocation it allocates more room than is immediately needed, 
so that it doesn't have to reallocate for each element. 

The resulting list is likely to be somewhat bigger than needed.

list-comprehension uses list.append under the hood, 
so it will call the list-resize method, which overallocates.
'''

code = compile('[x for x in iterable]', '', 'eval')
import dis
dis.dis(code)

'''
  1           0 LOAD_CONST               0 (<code object <listcomp> at 0x10560b810, file "", line 1>)
              2 LOAD_CONST               1 ('<listcomp>')
              4 MAKE_FUNCTION            0
              6 LOAD_NAME                0 (iterable)
              8 GET_ITER
             10 CALL_FUNCTION            1
             12 RETURN_VALUE

Disassembly of <code object <listcomp> at 0x10560b810, file "", line 1>:
  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (x)
              8 LOAD_FAST                1 (x)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE
'''
