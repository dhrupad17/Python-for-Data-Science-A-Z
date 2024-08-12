import logging

#Logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("Arithmetic Operations")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Substracting {a} - {b} = {result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def division(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None


add(10,15)
subtract(15,10)
multiply(10,12)
division(20,0)