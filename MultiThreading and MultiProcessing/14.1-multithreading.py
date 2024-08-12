import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter : {letter}")

## Creating 2 threads

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
# Start the thread
t1.start()
t2.start()

## wait for the threads to complete

t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)

## Output
'''
Number : 0
Letter : a
Number : 1
Letter : b
Letter : c
Number : 2
Number : 3
Letter : d
Number : 4
Letter : e        
10.061254501342773'''