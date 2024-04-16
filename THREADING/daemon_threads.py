# a daemon thread = a thread that runs in the background, not important for the program to run
# the program will not wait for a daemon thread to complete before exiting
# non-daemon threads are important for the program to run
# the program will wait for a non-daemon thread to complete before exiting

# daemon threads are used for tasks that are not important for the program to run ex. garbage collection, waiting for user input, long running tasks


import threading
import time

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, " seconds")

x = threading.Thread(target=timer, daemon=True) # add the daemon=True argument to make the thread a daemon thread
x.start()

answer = input("Do you wish to exit? ") # the program will exit even if the timer is still running because the timer is a daemon thread