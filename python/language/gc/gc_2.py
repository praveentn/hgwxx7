# gc stats

import gc

>>> gc.isenabled()
True

>>> gc.get_stats()
[{'collections': 158, 'collected': 755, 'uncollectable': 0}, 
{'collections': 14, 'collected': 952, 'uncollectable': 0}, 
{'collections': 4, 'collected': 616, 'uncollectable': 0}]

>>> gc.get_objects()
...
...


>>> gc.garbage
[]

