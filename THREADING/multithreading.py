# threads can be created by using the threading module
# each thread runs in its own memory space
# each thread has its own call stack
# the global memory space is shared between threads, so only one thread can run at a time
# threads are lightweight processes
# threads are used to run multiple tasks concurrently
# threads can be cpu bonded meaning that the program spends most of its time waiting for the cpu to finish internal events
# threads can be io bonded meaning that the program spends most of its time waiting for input/output operations to complete 
# using multiple threads can improve the performance of the program

import threading
import time



# if we wanted to create a program that runs while waiting for user input, we could use a thread to run the program while waiting for input on the main thread

# this program will run on the main thread and take about 12 seconds to complete
def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You studied")

# these are completed squentially not concurrently
# eat_breakfast()
# drink_coffee()
# study()

# if we want to run these concurrently, we can use threads
# this program will run in about 5 seconds
thread1 = threading.Thread(target=eat_breakfast)
thread1.start()
thread2 = threading.Thread(target=drink_coffee)
thread2.start()
thread3 = threading.Thread(target=study)
thread3.start()

# we can use thread.join() to wait for a thread to complete before continuing
thread1.join() 
thread2.join() # our main thread will wait for thread1 to complete before continuing

# these will run on the main thread, so they will run concurrently with the threads
print((threading. active_count())) # this will return the number of threads currently running
print(threading.enumerate()) # this will return a list of all the threads currently running

print(time.perf_counter()) # this will return the time in seconds since the program started running