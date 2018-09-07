# Copying two files of 1GB each
# with and without threading
# threads can be used for parallel filesystem IO

# load libraries
import time
import shutil
import threading
from queue import Queue

# without threading
start = time.time()
shutil.copy('v1.7z', 'wot_v1.7z')
shutil.copy('v2.7z', 'wot_v2.7z')
print("Execution time without threading = {0:.5f}".format(time.time() - start))

# threading lock
print_lock = threading.Lock()

# function to copy using shutil
def copy_op(file_data):
    with print_lock:
        print("Starting thread : {}".format(threading.current_thread().name))

    mydata = threading.local()
    mydata.ip, mydata.op = next(iter(file_data.items()))

    shutil.copy(mydata.ip, mydata.op)

    with print_lock:
        print("Finished thread : {}".format(threading.current_thread().name))

# process queuing
def process_queue():
    while True:
        file_data = compress_queue.get()
        copy_op(file_data)
        compress_queue.task_done()

# A queue is used to store the files that need to be processed.
compress_queue = Queue()

# file names mapping
output_names = [{'v1.7z': 'wt_v1.7z'}, {'v2.7z': 'wt_v2.7z'}]

# threading
for i in range(2):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

# noting time
start = time.time()

for file_data in output_names:
    compress_queue.put(file_data)

compress_queue.join()

print("Execution time = {0:.5f}".format(time.time() - start))

# Output

# Execution time without threading = 17.47281

# Starting thread : Thread-1
# Starting thread : Thread-2
# Finished thread : Thread-2
# Finished thread : Thread-1
# Execution time = 5.71958
