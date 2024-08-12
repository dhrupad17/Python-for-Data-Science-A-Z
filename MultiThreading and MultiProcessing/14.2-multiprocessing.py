import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Square : {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")

if __name__=="__main__":

    ## Create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    # Start the process
    p1.start()
    p2.start()

    #wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)

## Output
'''
Cube : 0
Square : 0
Cube : 1
Square : 1
Cube : 8
Square : 4
Cube : 27
Cube : 64
Square : 9
Square : 16
10.155908584594727
'''
