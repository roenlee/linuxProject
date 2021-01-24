'''
Description: Threading practice
Version: 1.0
Autor: Arvin
Date: 2021-01-23 08:10:14
LastEditors: Arvin
LastEditTime: 2021-01-23 08:15:14
'''
import threading


def thread_job():
    print("This is added Threadig job! number is % s" % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())

if __name__ == "__main__":
    main()