import multiprocessing
import math
import sys
import time

#Increase the maximum number of digits for Integer conversion

sys.set_int_max_str_digits(10000)

def fact(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[40,50,60]
    start_time=time.time()

    # create a pool of worker processes

    with multiprocessing.Pool() as pool:
        results=pool.map(fact,numbers)

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time Taken : {end_time-start_time} seconds")