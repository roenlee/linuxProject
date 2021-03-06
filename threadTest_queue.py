'''
Description: Threading practice
Version: 1.0
Autor: Arvin
Date: 2021-01-23 08:10:14
LastEditors: Arvin
LastEditTime: 2021-01-23 08:39:23
'''
import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading(data):
    q = Queue()
    threads = []
    data = data
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i],q))
  
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__ == "__main__":
    data = [[1,2,3], [3,4,5], [4,4,4],[5,5,5]]
    multithreading(data)