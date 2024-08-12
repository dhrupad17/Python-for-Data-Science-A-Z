from logger import logging

def add(a,b):
    logging.debug("This addition will take place now")
    return a+b

logging.debug("The addition function is called")
add(10,15)