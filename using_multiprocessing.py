#multiprocessing is the act of running tasks in parallel on different cpu cores, bypassing the GIL
# the multiprocessing module allows us to create multiple processes that run concurrently
# each process runs in its own memory space
# multiprocesssing is better for cpu bound tasks
# multithreading is better for io bound tasks


from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    
    
    a = Process(target=counter, args=(125000000,)) 
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,)) 
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,)) 
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,)) 
    h = Process(target=counter, args=(125000000,)) 
    
    start_time = time.perf_counter()

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__': # if running on windows this line is required. When we create a process, a new python interpreter is created and the code is run from the top. This line ensures that the code is only run if the script is run directly, and not if it is imported as a module.
    main()