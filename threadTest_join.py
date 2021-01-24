'''
Description: Threading practice
Version: 1.0
Autor: Arvin
Date: 2021-01-23 08:10:14
LastEditors: Arvin
LastEditTime: 2021-01-23 08:25:08
'''
import threading
import time


def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finished\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job, name='T1') #Threading naming
    thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()
    added_thread.join()
    
    thread2.start()
    thread2.join()
    
    print('All Done\n')

if __name__ == "__main__":
    main()