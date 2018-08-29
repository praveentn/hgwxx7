# set n_jobs = cpu count 
# to take advantage of parallel computing

# n_jobs: Number of cores used for the training process
# If set to -1, all cores will be used
n_jobs = -1

# alternately,

import multiprocessing

n_jobs = multiprocessing.cpu_count()

>>> n_jobs
4
