import threading
import os

def task1():
    print("\nTask 1 assigned to thread: {}".format(threading.current_thread().name))
    print("\nID of process running task 1: {}".format(os.getpid()))
    print("\nThread ID of task 1: {}".format(threading.get_ident()))

def task2():
    print("\nTask 2 assigned to thread: {}".format(threading.current_thread().name))
    print("\nID of process running task 2: {}".format(os.getpid()))
    print("\nThread ID of task 2: {}".format(threading.get_ident()))

if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')   

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()