import multiprocessing
import time
from multiprocessing import Process, Queue
import random

q = Queue()
process = []
pre_dict = {}


def f(q, index_num):
    x = (index_num + 1) * 100
    time.sleep(random.uniform(0, 1))
    outset = {
        index_num: x
    }
    q.put(outset)


for i in range(20):
    p = multiprocessing.Process(target=f, args=(q, i))
    p.start()
    process.append(p)

for p in process:
    p.join()

for i in range(20):
    pre_dict = {**pre_dict, **q.get()}

print(f'This is the unsorted return Dictionary:\n{pre_dict}')

key = list(pre_dict.keys())
key.sort()
sort_dict = {i: pre_dict[i] for i in key}

print(f'\nThese are the sorted Dictionary values:\n{sort_dict.values()}')

print(f'\n\nThis is the returned values from the different process in order\n')
for i in range(20):
    print(sort_dict.get(i))
