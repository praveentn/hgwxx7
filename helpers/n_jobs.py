# set n_jobs = cpu count 
# to take advantage of parallel computing

import multiprocessing

n_jobs = multiprocessing.cpu_count()

>>> n_jobs
4
