from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from PT_Pool import PT_Pool
import time

def f(x):
    time.sleep(1)
    for i in range(10*6):
        pass
    return x
max_workers = 500
tasks_number = max_workers

pt_pool = PT_Pool(threads_limit = max_workers)
def get_pt_pool(max_workers, tasks_number):
    def on_result(res):
        pass
    def completed(_):
        print( time.time() - start_time )
    pt_pool.apply_async(f, range(tasks), on_result=on_result)
    pt_pool.apply_async(f, [-1], on_result=completed)

start_time = time.time()
with ThreadPoolExecutor(max_workers = max_workers) as executor:
    list( executor.map(f, range(tasks) ) )
print( time.time() - start_time )



