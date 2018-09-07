# run a script from the commandline using the Python debugger
python -m pdb debug_script.py

# load library
import pdb

# sample function
def make_bread():
    ''' pdb set_trace() '''
    pdb.set_trace()
    return "I don't have time"

print(make_bread())

# Command Line Interpreter output
>>> make_bread()
> <stdin>(3)make_bread()
(Pdb) 2
2

(Pdb) 3
3

(Pdb) 0
0

(Pdb) pr
*** NameError: name 'pr' is not defined

(Pdb) 'van peer'
'van peer'

# use of c, s, w, a, n (pdb-cswan)
>>> make_bread()
> <stdin>(3)make_bread()
(Pdb) 'pears'
'pears'

(Pdb) a                         # prints the arguments if any

(Pdb) s                         # execute the current line and 
--Return--                      # stop at the first possible occasion
> <stdin>(3)make_bread()->"I don't have time"

(Pdb) w                         # shows the executing line context 
  <stdin>(1)<module>()
> <stdin>(3)make_bread()->"I don't have time"

(Pdb) n                         # Continue execution until the next line 
"I don't have time"             # in the current function is reached or 
--Return--                      # it returns
> <stdin>(1)<module>()->None

(Pdb) c                         # continue execution
>>>
